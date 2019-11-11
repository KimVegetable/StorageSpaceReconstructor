"""
@author:    Junho Kim
@license:   None
@contact:   rlawnsgh92(at)korea(dot)ac(dot)kr
@insta:     @dailyjunoat_
"""

import struct

from SSR.disk import Disk
from SSR.util import *
from SSR.define import Define

class Reconstructor:

    def __init__(self, version, level):
        self.version = version
        self.level = level
        self.disk_list = []

        """ physical disks, virtual disks, """
        self.parsed_disks = []


    def __del__(self):
        pass

    def __repr__(self):
        return "Reconstructor"

    def add_disk(self, disk):
        print("[*] Disk Added.")
        self.disk_list.append(disk)

    """ parse_metadata """
    def parse_metadata(self):  # 여기서 메타데이터들을 읽고 디스크들 재구성하기.
        """ Init parsed disks """
        parsed_disks_size = len(self.disk_list[0].sdbb_entry_type2) + len(self.disk_list[0].sdbb_entry_type3)
        for i in range(0, parsed_disks_size + 1):  # +1은 Offset이 0부터 시작해서 1개가 부족하니까 추가.
            self.parsed_disks.append(None)

        if self._parse_entry_type1() == False:
            return False

        if self._parse_entry_type2() == False:
            return False

        if self._parse_entry_type3() == False:
            return False

        if self._parse_entry_type4() == False:
            return False

        return True

    def _parse_entry_type1(self):
        """ SPACEDB의 Pool UUID와 type 1의 UUID를 비교하기. """
        for disk in self.disk_list:
            temp_offset = 0

            for i in range(0, len(disk.sdbb_entry_type1)):
                temp_offset += disk.sdbb_entry_type1[i][temp_offset] + 1
                temp_offset += disk.sdbb_entry_type1[i][temp_offset] + 1
                storage_pool_uuid = disk.sdbb_entry_type1[i][temp_offset : temp_offset + 0x10]

                if storage_pool_uuid != disk.storage_pool_uuid:
                    print("[*] This disk is not member for storage pool")
                    return False

        return True

    def _parse_entry_type2(self):
        temp_disk = self.disk_list[0]
        for i in range(0, len(temp_disk.sdbb_entry_type2)):
            disk = Disk()
            temp_offset = 0
            data_record_len = temp_disk.sdbb_entry_type2[i][temp_offset]
            physical_disk_id = big_endian_to_int(temp_disk.sdbb_entry_type2[i][temp_offset + 1: temp_offset + 1 + data_record_len])


            temp_offset += temp_disk.sdbb_entry_type2[i][temp_offset] + 1
            temp_offset += temp_disk.sdbb_entry_type2[i][temp_offset] + 1

            physical_disk_uuid = temp_disk.sdbb_entry_type2[i][temp_offset: temp_offset + 0x10]
            temp_offset += 0x10

            physical_disk_name_length = struct.unpack('>H', temp_disk.sdbb_entry_type2[i][temp_offset: temp_offset + 0x02])[0]
            temp_offset += 0x02

            physical_disk_name = b''
            temp_physical_disk_name = temp_disk.sdbb_entry_type2[i][temp_offset: temp_offset + physical_disk_name_length * 2]
            temp_offset += physical_disk_name_length * 2
            for j in range(0, physical_disk_name_length * 2, 2):
                physical_disk_name += temp_physical_disk_name[j + 1 : j + 2]
                physical_disk_name += temp_physical_disk_name[j : j + 1]

            temp_offset += temp_disk.sdbb_entry_type2[i][temp_offset] + 1
            temp_offset += temp_disk.sdbb_entry_type2[i][temp_offset] + 1
            temp_offset += temp_disk.sdbb_entry_type2[i][temp_offset] + 1
            temp_offset += temp_disk.sdbb_entry_type2[i][temp_offset] + 1
            temp_offset += temp_disk.sdbb_entry_type2[i][temp_offset] + 1

            data_record_len = temp_disk.sdbb_entry_type2[i][temp_offset]
            physical_disk_block_number = big_endian_to_int(temp_disk.sdbb_entry_type2[i][temp_offset + 1 : temp_offset + 1 + data_record_len])

            disk.id = physical_disk_id
            disk.uuid = physical_disk_uuid
            disk.name = physical_disk_name
            disk.block_number = physical_disk_block_number

            for disk_member in self.disk_list:
                if disk.uuid == disk_member.physical_disk_uuid:
                    disk.dp = disk_member
                    self.parsed_disks[physical_disk_id] = disk
                    break

        return True

    def _parse_entry_type3(self):
        temp_disk = self.disk_list[0]
        for i in range(0, len(temp_disk.sdbb_entry_type3)):
            disk = Disk()
            temp_offset = 0
            data_record_len = temp_disk.sdbb_entry_type3[i][temp_offset]
            virtual_disk_id = big_endian_to_int(temp_disk.sdbb_entry_type3[i][temp_offset + 1: temp_offset + 1 + data_record_len])

            temp_offset += temp_disk.sdbb_entry_type3[i][temp_offset] + 1
            temp_offset += temp_disk.sdbb_entry_type3[i][temp_offset] + 1

            virtual_disk_uuid = temp_disk.sdbb_entry_type3[i][temp_offset: temp_offset + 0x10]
            temp_offset += 0x10

            virtual_disk_name_length = struct.unpack('>H', temp_disk.sdbb_entry_type3[i][temp_offset: temp_offset + 0x02])[0]
            temp_offset += 0x02

            virtual_disk_name = b''
            temp_virtual_disk_name = temp_disk.sdbb_entry_type3[i][temp_offset: temp_offset + virtual_disk_name_length * 2]
            temp_offset += virtual_disk_name_length * 2
            for j in range(0, virtual_disk_name_length * 2, 2):
                virtual_disk_name += temp_virtual_disk_name[j + 1 : j + 2]
                virtual_disk_name += temp_virtual_disk_name[j : j + 1]


            temp_offset += 5

            data_record_len = temp_disk.sdbb_entry_type3[i][temp_offset]
            virtual_disk_block_number = big_endian_to_int(temp_disk.sdbb_entry_type3[i][temp_offset + 1: temp_offset + 1 + data_record_len])


            disk.id = virtual_disk_id
            disk.uuid = virtual_disk_uuid
            disk.name = virtual_disk_name
            disk.block_number = virtual_disk_block_number

            self.parsed_disks[virtual_disk_id] = disk

        return True

    def _parse_entry_type4(self):
        temp_disk = self.disk_list[0]
        for i in range(0, len(temp_disk.sdbb_entry_type4)):
            sdbb_entry_type4_data = {}
            sdbb_entry_type4_data['virtual_disk_id'] = None
            sdbb_entry_type4_data['virtual_disk_block_number'] = None
            sdbb_entry_type4_data['sequence_number'] = None
            sdbb_entry_type4_data['physical_disk_id'] = None
            sdbb_entry_type4_data['physical_disk_block_number'] = None
            temp_offset = 0

            temp_offset += temp_disk.sdbb_entry_type4[i][temp_offset] + 1
            temp_offset += temp_disk.sdbb_entry_type4[i][temp_offset] + 1
            temp_offset += temp_disk.sdbb_entry_type4[i][temp_offset] + 1

            data_record_len = temp_disk.sdbb_entry_type4[i][temp_offset]
            sdbb_entry_type4_data['virtual_disk_id'] = big_endian_to_int(
                temp_disk.sdbb_entry_type4[i][temp_offset + 1: temp_offset + 1 + data_record_len])
            temp_offset += temp_disk.sdbb_entry_type4[i][temp_offset] + 1

            data_record_len = temp_disk.sdbb_entry_type4[i][temp_offset]
            sdbb_entry_type4_data['virtual_disk_block_number'] = big_endian_to_int(
                temp_disk.sdbb_entry_type4[i][temp_offset + 1: temp_offset + 1 + data_record_len])
            temp_offset += temp_disk.sdbb_entry_type4[i][temp_offset] + 1

            data_record_len = temp_disk.sdbb_entry_type4[i][temp_offset]
            sdbb_entry_type4_data['sequence_number'] = big_endian_to_int(
                temp_disk.sdbb_entry_type4[i][temp_offset + 1: temp_offset + 1 + data_record_len])
            temp_offset += temp_disk.sdbb_entry_type4[i][temp_offset] + 1

            data_record_len = temp_disk.sdbb_entry_type4[i][temp_offset]
            sdbb_entry_type4_data['physical_disk_id'] = big_endian_to_int(
                temp_disk.sdbb_entry_type4[i][temp_offset + 1: temp_offset + 1 + data_record_len])
            temp_offset += temp_disk.sdbb_entry_type4[i][temp_offset] + 1

            data_record_len = temp_disk.sdbb_entry_type4[i][temp_offset]
            sdbb_entry_type4_data['physical_disk_block_number'] = big_endian_to_int(
                temp_disk.sdbb_entry_type4[i][temp_offset + 1: temp_offset + 1 + data_record_len])
            temp_offset += temp_disk.sdbb_entry_type4[i][temp_offset] + 1

            self.parsed_disks[sdbb_entry_type4_data['virtual_disk_id']].sdbb_entry_type4.append(sdbb_entry_type4_data)

    """ restore disks """
    def restore_virtual_disk(self):

        for disk in self.parsed_disks:
            if disk == None:  # 0번 skip
                continue

            if repr(disk.dp) == "Storage Space":  # physical disk skip
                continue

            elif disk.dp == None:

                if disk.name == b'':  # Metadata Area(SPACEDB, SDBC, SDBB) skip
                    continue

                disk.dp = open("..\\result\\" + disk.name[:-2].decode('utf-16') + ".dd", 'wb')

                """ Simple, Mirror """
                if self.level == Define.RAID_LEVEL_SIMPLE or self.level == Define.RAID_LEVEL_2MIRROR or \
                        self.level == Define.RAID_LEVEL_3MIRROR :

                    for i in range(0, disk.block_number):
                        is_exist_disk_block = False
                        for j in range(0, len(disk.sdbb_entry_type4)):
                            if disk.sdbb_entry_type4[j]['virtual_disk_block_number'] == i:
                                partition_start_offset = self.parsed_disks[disk.sdbb_entry_type4[j]['physical_disk_id']].dp.partition_start_offset
                                self.parsed_disks[disk.sdbb_entry_type4[j]['physical_disk_id']].dp.dp.seek((disk.sdbb_entry_type4[j]['physical_disk_block_number'] + 2) * 0x10000000 + partition_start_offset)  # SPACEDB 시작 offset을 더해줘야함
                                disk.dp.write(self.parsed_disks[disk.sdbb_entry_type4[j]['physical_disk_id']].dp.dp.read(0x10000000))
                                is_exist_disk_block = True
                                break

                        if is_exist_disk_block == False:
                           buf = b'\x00' * 0x10000000
                           disk.dp.write(buf)

                """ Parity """
                if self.level == Define.RAID_LEVEL_PARITY :
                    for i in range(0, disk.block_number, 2):
                        is_exist_disk_block = False

                        temp_entry_type4_0 = None  # Sequence 0
                        temp_entry_type4_1 = None  # Sequence 1
                        temp_entry_type4_2 = None  # Sequence 2

                        """ Search Sequence Number """
                        for j in range(0, len(disk.sdbb_entry_type4)):
                            if disk.sdbb_entry_type4[j]['virtual_disk_block_number'] == i:
                                if disk.sdbb_entry_type4[j]['sequence_number'] == 0:
                                    temp_entry_type4_0 = disk.sdbb_entry_type4[j]
                                    is_exist_disk_block = True
                                elif disk.sdbb_entry_type4[j]['sequence_number'] == 1:
                                    temp_entry_type4_1 = disk.sdbb_entry_type4[j]
                                    is_exist_disk_block = True
                                elif disk.sdbb_entry_type4[j]['sequence_number'] == 2:
                                    temp_entry_type4_2 = disk.sdbb_entry_type4[j]
                                    is_exist_disk_block = True

                        if is_exist_disk_block == False:
                            buf = b'\x00' * 0x20000000
                            disk.dp.write(buf)
                            continue

                        partition_start_offset_0 = self.parsed_disks[temp_entry_type4_0['physical_disk_id']].dp.partition_start_offset
                        partition_start_offset_1 = self.parsed_disks[temp_entry_type4_0['physical_disk_id']].dp.partition_start_offset
                        partition_start_offset_2 = self.parsed_disks[temp_entry_type4_0['physical_disk_id']].dp.partition_start_offset

                        for j in range(0, 0x400):
                            if j % 3 == 0:
                                self.parsed_disks[temp_entry_type4_0['physical_disk_id']].dp.dp.seek((temp_entry_type4_0['physical_disk_block_number'] + 2) * 0x10000000 + partition_start_offset_0 + j * 0x40000)  # SPACEDB 시작 offset을 더해줘야함
                                self.parsed_disks[temp_entry_type4_1['physical_disk_id']].dp.dp.seek((temp_entry_type4_1['physical_disk_block_number'] + 2) * 0x10000000 + partition_start_offset_0 + j * 0x40000)  # SPACEDB 시작 offset을 더해줘야함
                                disk.dp.write(self.parsed_disks[temp_entry_type4_0['physical_disk_id']].dp.dp.read(0x40000))
                                disk.dp.write(self.parsed_disks[temp_entry_type4_1['physical_disk_id']].dp.dp.read(0x40000))
                            if j % 3 == 1:
                                self.parsed_disks[temp_entry_type4_2['physical_disk_id']].dp.dp.seek((temp_entry_type4_2['physical_disk_block_number'] + 2) * 0x10000000 + partition_start_offset_2 + j * 0x40000)  # SPACEDB 시작 offset을 더해줘야함
                                self.parsed_disks[temp_entry_type4_0['physical_disk_id']].dp.dp.seek((temp_entry_type4_0['physical_disk_block_number'] + 2) * 0x10000000 + partition_start_offset_0 + j * 0x40000)  # SPACEDB 시작 offset을 더해줘야함
                                disk.dp.write(self.parsed_disks[temp_entry_type4_2['physical_disk_id']].dp.dp.read(0x40000))
                                disk.dp.write(self.parsed_disks[temp_entry_type4_0['physical_disk_id']].dp.dp.read(0x40000))
                            if j % 3 == 2:
                                self.parsed_disks[temp_entry_type4_1['physical_disk_id']].dp.dp.seek((temp_entry_type4_1['physical_disk_block_number'] + 2) * 0x10000000 + partition_start_offset_1 + j * 0x40000)  # SPACEDB 시작 offset을 더해줘야함
                                self.parsed_disks[temp_entry_type4_2['physical_disk_id']].dp.dp.seek((temp_entry_type4_2['physical_disk_block_number'] + 2) * 0x10000000 + partition_start_offset_2 + j * 0x40000)  # SPACEDB 시작 offset을 더해줘야함
                                disk.dp.write(self.parsed_disks[temp_entry_type4_1['physical_disk_id']].dp.dp.read(0x40000))
                                disk.dp.write(self.parsed_disks[temp_entry_type4_2['physical_disk_id']].dp.dp.read(0x40000))






                disk.dp.close()
