import os
import struct


class StorageSpace:

    def __init__(self):
        __dp = None  # disk pointer
        __is_parsed = False

    def __del__(self):
        if (self.__dp is not None) and (not self.__dp.closed):
            self.__dp.close()

    def __repr__(self):
        return f"Storage Space <>"

    def open_disk(self, file_path):

        # mmap 사용 확인해보긔
        # File Open
        if (os.path.exists(file_path)):
            self.__dp = open(file_path, 'rb')
            print(f"[*] \"{file_path}\" Disk open!")
            return True
        else:
            print("[*] \"" + file_path + "\" File not exist!")
            return False

    def parse_disk(self):

        ########### MBR ###########
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
            self.__dp.seek(0x200)               # 추후에 GPT 넘어가게 변경


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
            print("[*] SPACEDB Parsing Success")
        else:
            print("[*] SPACEDB Parsing Fail")
            return False

        sdbc = self.__dp.read(0x200)
        self.__parse_sdbc(sdbc)

        sdbb = self.__dp.read(0x10000)
        self.__parse_sdbb(sdbb)

    def __parse_spacedb(self, data):
        if data[0:8] is not b'SPACEDB\x20':
            return False


        pass

    def __parse_sdbc(self, data):
        print(data)
        pass

    def __parse_sdbb(self, data):
        print(data)
        pass


