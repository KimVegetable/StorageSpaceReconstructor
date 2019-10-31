from SSR.storagespace import StorageSpace
from SSR.reconstructor import Reconstructor

def test_ss():

    disk1 = StorageSpace()
    disk2 = StorageSpace()
    disk3 = StorageSpace()

    if disk1.open_disk("F:\\Windows 8.1\\01. Simple\\Windows_8.1_Physical_5GB.001"):
        disk1.parse_disk()
    else:
        return False

    if disk2.open_disk("F:\\Windows 8.1\\01. Simple\\Windows_8.1_Physical_10GB.001"):
        disk2.parse_disk()
    else:
        return False

    if disk3.open_disk("F:\\Windows 8.1\\01. Simple\\Windows_8.1_Physical_15GB.001"):
        disk3.parse_disk()
    else:
        return False


if __name__ == "__main__":
    test_ss()


