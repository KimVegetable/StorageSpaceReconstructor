from SSR.storagespace import StorageSpace
from SSR.reconstructor import Reconstructor
from SSR.define import Define


def test_ss():

    disk1 = StorageSpace(Define.WINDOWS_8, Define.RAID_LEVEL_PARITY)
    disk2 = StorageSpace(Define.WINDOWS_8, Define.RAID_LEVEL_PARITY)
    disk3 = StorageSpace(Define.WINDOWS_8, Define.RAID_LEVEL_PARITY)
    disk4 = StorageSpace(Define.WINDOWS_8, Define.RAID_LEVEL_PARITY)

    if disk1.open_disk("F:\\Windows 8.1\\04. Parity\\Windows_8.1_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("F:\\Windows 8.1\\04. Parity\\Windows_8.1_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("F:\\Windows 8.1\\04. Parity\\Windows_8.1_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk4.open_disk("F:\\Windows 8.1\\04. Parity\\Windows_8.1_Physical_20GB.001"):
        if disk4.parse_disk():
            pass
        else:
            return False
    else:
        return False

    reconstructor = Reconstructor(Define.WINDOWS_8, Define.RAID_LEVEL_PARITY)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)
    reconstructor.add_disk(disk4)

    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()


if __name__ == "__main__":
    test_ss()


