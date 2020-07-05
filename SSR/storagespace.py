"""
@author:    Junho Kim
@license:   None
@contact:   rlawnsgh92(at)korea(dot)ac(dot)kr
"""

import os
import struct

from SSR.define import Define


class StorageSpace:

    def __init__(self, version, level):
        """

        :param version:
        :param level:
        """

        self.dp = None  # disk pointer
        self.partition_start_offset = None
        self.version = version
        self.level = level

        """ for SPACEDB """
        self.storage_pool_uuid = None
        self.physical_disk_uuid = None
        self.physical_disk_format_time = None

        """ for SDBC """
        self.sdbb_entry_size = None
        self.next_sdbb_entry_number = None
        self.sdbb_entry_modified_time = None

        """ for SDBB """
        self.sdbb_entry_type1 = []
        self.sdbb_entry_type2 = []
        self.sdbb_entry_type3 = []
        self.sdbb_entry_type4 = []


    def __del__(self):
        #if (self.dp is not None) and (not self.dp.closed):
        #    self.dp.close()
        pass

    def __repr__(self):
        return "Storage Space"

    def open_disk(self, file_path):
        """

        :param file_path: Disk Image Path
        :return: True / False
        """

        """ disk open """
        if (os.path.exists(file_path)):
            self.dp = open(file_path, 'rb')
            print(f"[*] \"{file_path}\" Disk open!")
            return True
        else:
            print("[*] \"" + file_path + "\" File not exist!")
            return False

    def parse_disk(self):

        """ MBR """
        self.dp.seek(0)
        mbr = self.dp.read(512)
        boot_code = struct.unpack("<446B", mbr[0:446])
        self.partitions = []
        self.partitions.append(mbr[446:462])
        self.partitions.append(mbr[462:478])
        self.partitions.append(mbr[478:494])
        self.partitions.append(mbr[494:510])
        self.signature = struct.unpack("<H", mbr[510:])[0]

        if self.partitions[0][4] == 0xEE:
            self.dp.seek(0x200)  # 추후에 GPT 넘어가게 변경

        """ GPT """
        if self.dp.read(0x08) != b'\x45\x46\x49\x20\x50\x41\x52\x54':
            print("[*] Not GPT!")
            return False

        self.dp.seek(0x4A0)  # GPT Entry 2번째의 LBA 주소로 강제로 이동(reserved 제외)
        partition_start_offset = struct.unpack('<Q', self.dp.read(0x08))[0] * 0x200
        partition_sector_count = struct.unpack('<Q', self.dp.read(0x08))[0]

        self.partition_start_offset = partition_start_offset

        self.dp.seek(partition_start_offset)
        spacedb = self.dp.read(0x1000)
        if self.__parse_spacedb(spacedb):
            print("[*] SPACEDB Parsing Success.")
        else:
            print("[*] SPACEDB Parsing Fail.")
            return False

        sdbc = self.dp.read(0x200)
        if self.__parse_sdbc(sdbc):
            print("[*] SDBC Parsing Success.")
        else:
            print("[*] SDBC Parsing Fail.")
            #return False
            return True  # 임시

        sdbb = self.dp.read(0x10000)
        if self.__parse_sdbb(sdbb):
            print("[*] SDBB Parsing Success.")
        else:
            print("[*] SDBB Parsing Fail.")
            #return False
            return True  # 임시

        print("[*] Disk Parsing Success.")
        return True

    def __parse_spacedb(self, data):
        """

        :param data: SPACEDB raw data(4096 bytes)
        :return: True / False
        """

        """ Signature Check """
        if data[0:8] != b'SPACEDB ':
            print("[*] SPACEDB Signature is not matching.")
            return False

        """ Version Check """
        if self.version == Define.WINDOWS_8 or self.version == Define.WINDOWS_SERVER_2012:  # Windows 8.1, Windows Server 2012
            self.storage_pool_uuid = data[0x10:0x20]
            self.physical_disk_uuid = data[0x20:0x30]
            self.physical_disk_format_time = struct.unpack('>Q', data[0x58:0x60])[0]
        elif self.version == Define.WINDOWS_10 or self.version == Define.WINDOWS_SERVER_2016 or self.version == Define.WINDOWS_SERVER_2019:  # Windows 10, Windows Server 2016, 2019
            self.physical_disk_format_time = struct.unpack('>Q', data[0x18:0x20])[0]
            self.storage_pool_uuid = data[0x20:0x30]
            self.physical_disk_uuid = data[0x30:0x40]
        else:
            print("[*] SPACEDB version is abnormal.")
            return False

        return True

    def __parse_sdbc(self, data):
        """

        :param data: SDBC raw data(512 bytes)
        :return: True / False
        """

        """ Signature Check """
        if data[0:8] != b'SDBC    ':
            print("[*] SDBC Signature is not matching.")
            return False

        """ Storage Pool UUID Check"""
        if data[0x10:0x20] != self.storage_pool_uuid:
            print("[*] Storage Pool UUID is not matching with SPACEDB's Storage Pool UUID")
            return False

        self.sdbb_entry_size = struct.unpack('>I', data[0x24:0x28])[0]
        self.next_sdbb_entry_number = struct.unpack('>I', data[0x28:0x2C])[0]
        self.sdbb_entry_modified_time = struct.unpack('>Q', data[0x48:0x50])[0]

        return True

    def __parse_sdbb(self, data):
        """

        :param data: SDBB raw data(0x10000 bytes) temporary size
        :return: True / False
        """

        temp_list = []
        """ Init list """
        for i in range(0, self.next_sdbb_entry_number):  # Init
            temp_list.append(b'')

        """ Insert to list """
        for i in range(0x08, self.next_sdbb_entry_number):
            temp_offset = (i - 8) * 0x40
            if data[temp_offset + 0x0E : temp_offset + 0x10] == b'\x00\x00':  # Empty Entry
                continue

            temp_list_index = struct.unpack('>I', data[temp_offset + 0x08 : temp_offset + 0x0C])[0]
            temp_list[temp_list_index] += data[temp_offset + 0x10 : temp_offset + 0x40]

        """ Sort Entries """
        for i in range(0x08, self.next_sdbb_entry_number):
            if temp_list[i] == b'':
                continue

            entry_length = struct.unpack('>I', temp_list[i][0x04: 0x08])[0]

            if temp_list[i][0] == 0x01:
                self.sdbb_entry_type1.append(temp_list[i][0x08 : 0x08 + entry_length])
            elif temp_list[i][0] == 0x02:
                self.sdbb_entry_type2.append(temp_list[i][0x08: 0x08 + entry_length])
            elif temp_list[i][0] == 0x03:
                self.sdbb_entry_type3.append(temp_list[i][0x08: 0x08 + entry_length])
            elif temp_list[i][0] == 0x04:
                self.sdbb_entry_type4.append(temp_list[i][0x08: 0x08 + entry_length])

        return True


