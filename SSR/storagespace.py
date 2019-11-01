"""
@author:    Junho Kim
@license:   None
@contact:   rlawnsgh92(at)korea(dot)ac(dot)kr
@insta:     @dailyjunoat_
"""

import os
import struct


class StorageSpace:

    def __init__(self):
        __dp = None  # disk pointer
        __is_parsed = False

        """ for SPACEDB """
        self.storage_pool_uuid = None
        self.physical_disk_uuid = None
        self.physical_disk_format_time = None

        """ for SDBC """
        self.sdbb_entry_size = None
        self.next_sdbb_entry_number = None
        self.sdbb_entry_modified_time = None

        """ for SDBB """

    def __del__(self):
        if (self.__dp is not None) and (not self.__dp.closed):
            self.__dp.close()

    def __repr__(self):
        return "Storage Space"

    def open_disk(self, file_path):
        """

        :param file_path: Disk Image Path
        :return: True / False
        """

        """ disk open """
        if (os.path.exists(file_path)):
            self.__dp = open(file_path, 'rb')
            print(f"[*] \"{file_path}\" Disk open!")
            return True
        else:
            print("[*] \"" + file_path + "\" File not exist!")
            return False

    def parse_disk(self):
        """

        :return: None
        """

        """ MBR """
        self.__dp.seek(0)
        mbr = self.__dp.read(512)
        boot_code = struct.unpack("<446B", mbr[0:446])
        self.partitions = []
        self.partitions.append(mbr[446:462])
        self.partitions.append(mbr[462:478])
        self.partitions.append(mbr[478:494])
        self.partitions.append(mbr[494:510])
        self.signature = struct.unpack("<H", mbr[510:])[0]

        if self.partitions[0][4] == 0xEE:
            self.__dp.seek(0x200)  # 추후에 GPT 넘어가게 변경


        """ GPT """
        if self.__dp.read(0x08) != b'\x45\x46\x49\x20\x50\x41\x52\x54':
            print("[*] Not GPT!")
            return False

        self.__dp.seek(0x4A0)  # GPT Entry 2번째의 LBA 주소로 강제로 이동(reserved 제외)
        partition_start_offset = struct.unpack('<Q', self.__dp.read(0x08))[0] * 0x200
        partition_sector_count = struct.unpack('<Q', self.__dp.read(0x08))[0]

        self.__dp.seek(partition_start_offset)
        spacedb = self.__dp.read(0x1000)
        if self.__parse_spacedb(spacedb):
            print("[*] SPACEDB Parsing Success.")
        else:
            print("[*] SPACEDB Parsing Fail.")
            return False

        sdbc = self.__dp.read(0x200)
        if self.__parse_sdbc(sdbc):
            print("[*] SDBC Parsing Success.")
        else:
            print("[*] SDBC Parsing Fail.")
            return False

        sdbb = self.__dp.read(0x10000)
        if self.__parse_sdbb(sdbb):
            print("[*] SDBB Parsing Success.")
        else:
            print("[*] SDBB Parsing Fail.")
            return False

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
        version = data[0x09]
        if version == 0x01:  # Windows 8.1, Windows Server 2012
            self.storage_pool_uuid = data[0x10:0x20]
            self.physical_disk_uuid = data[0x20:0x30]
            self.physical_disk_format_time = struct.unpack('<Q', data[0x58:0x60])[0]
        elif version == 0x02:  # Windows 10, Windows Server 2016
            self.physical_disk_format_time = struct.unpack('<Q', data[0x18:0x20])[0]
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

        self.sdbb_entry_size = struct.unpack('<I', data[0x24:0x28])[0]
        self.next_sdbb_entry_number = struct.unpack('<I', data[0x28:0x2C])[0]
        self.sdbb_entry_modified_time = struct.unpack('<Q', data[0x48:0x50])[0]

        return True




    def __parse_sdbb(self, data):
        """

        :param data: SDBB raw data(0x10000 bytes) temporary size
        :return: True / False
        """

        temp_list = []

        for i in range(0x00, self.next_sdbb_entry_number - 8):
            temp_offset = i * 0x40
            if data[temp_offset + 0x0C : temp_offset + 0x0E] == b'\x00\x00':
                temp_list.insert(b'')

            temp_list[i] += data[temp_offset + 0x10 : temp_offset + 0x40]

        print("test")


        return True


