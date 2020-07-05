from SSR.storagespace import StorageSpace
from SSR.reconstructor import Reconstructor
from SSR.define import Define

def test_windows8_simple():

    disk1 = StorageSpace(Define.WINDOWS_8, Define.RAID_LEVEL_SIMPLE)
    disk2 = StorageSpace(Define.WINDOWS_8, Define.RAID_LEVEL_SIMPLE)
    disk3 = StorageSpace(Define.WINDOWS_8, Define.RAID_LEVEL_SIMPLE)

    if disk1.open_disk("D:\\Windows 8.1\\01. Simple\\Windows_8.1_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\Windows 8.1\\01. Simple\\Windows_8.1_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\Windows 8.1\\01. Simple\\Windows_8.1_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    reconstructor = Reconstructor(Define.WINDOWS_8, Define.RAID_LEVEL_SIMPLE)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)

    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()

def test_windows8_2mirror():

    disk1 = StorageSpace(Define.WINDOWS_8, Define.RAID_LEVEL_2MIRROR)
    disk2 = StorageSpace(Define.WINDOWS_8, Define.RAID_LEVEL_2MIRROR)
    disk3 = StorageSpace(Define.WINDOWS_8, Define.RAID_LEVEL_2MIRROR)

    if disk1.open_disk("D:\\Windows 8.1\\02. 2Mirror\\Windows_8.1_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\Windows 8.1\\02. 2Mirror\\Windows_8.1_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\Windows 8.1\\02. 2Mirror\\Windows_8.1_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    reconstructor = Reconstructor(Define.WINDOWS_8, Define.RAID_LEVEL_2MIRROR)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)

    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()

def test_windows8_3mirror():

    disk1 = StorageSpace(Define.WINDOWS_8, Define.RAID_LEVEL_3MIRROR)
    disk2 = StorageSpace(Define.WINDOWS_8, Define.RAID_LEVEL_3MIRROR)
    disk3 = StorageSpace(Define.WINDOWS_8, Define.RAID_LEVEL_3MIRROR)
    disk4 = StorageSpace(Define.WINDOWS_8, Define.RAID_LEVEL_3MIRROR)
    disk5 = StorageSpace(Define.WINDOWS_8, Define.RAID_LEVEL_3MIRROR)

    if disk1.open_disk("D:\\Windows 8.1\\03. 3Mirror\\Windows_8.1_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\Windows 8.1\\03. 3Mirror\\Windows_8.1_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\Windows 8.1\\03. 3Mirror\\Windows_8.1_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk4.open_disk("D:\\Windows 8.1\\03. 3Mirror\\Windows_8.1_Physical_20GB.001"):
        if disk4.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk5.open_disk("D:\\Windows 8.1\\03. 3Mirror\\Windows_8.1_Physical_25GB.001"):
        if disk5.parse_disk():
            pass
        else:
            return False
    else:
        return False

    reconstructor = Reconstructor(Define.WINDOWS_8, Define.RAID_LEVEL_3MIRROR)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)
    reconstructor.add_disk(disk4)
    reconstructor.add_disk(disk5)

    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()

def test_windows8_parity():

    disk1 = StorageSpace(Define.WINDOWS_8, Define.RAID_LEVEL_PARITY)
    disk2 = StorageSpace(Define.WINDOWS_8, Define.RAID_LEVEL_PARITY)
    disk3 = StorageSpace(Define.WINDOWS_8, Define.RAID_LEVEL_PARITY)
    disk4 = StorageSpace(Define.WINDOWS_8, Define.RAID_LEVEL_PARITY)

    if disk1.open_disk("D:\\Windows 8.1\\04. Parity\\Windows_8.1_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\Windows 8.1\\04. Parity\\Windows_8.1_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\Windows 8.1\\04. Parity\\Windows_8.1_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk4.open_disk("D:\\Windows 8.1\\04. Parity\\Windows_8.1_Physical_20GB.001"):
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

def test_windows10_simple():

    disk1 = StorageSpace(Define.WINDOWS_10, Define.RAID_LEVEL_SIMPLE)
    disk2 = StorageSpace(Define.WINDOWS_10, Define.RAID_LEVEL_SIMPLE)
    disk3 = StorageSpace(Define.WINDOWS_10, Define.RAID_LEVEL_SIMPLE)

    if disk1.open_disk("D:\\Windows 10\\01. Simple\\Windows_10_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\Windows 10\\01. Simple\\Windows_10_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\Windows 10\\01. Simple\\Windows_10_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    reconstructor = Reconstructor(Define.WINDOWS_10, Define.RAID_LEVEL_SIMPLE)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)

    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()

def test_windows10_2mirror():

    disk1 = StorageSpace(Define.WINDOWS_10, Define.RAID_LEVEL_2MIRROR)
    disk2 = StorageSpace(Define.WINDOWS_10, Define.RAID_LEVEL_2MIRROR)
    disk3 = StorageSpace(Define.WINDOWS_10, Define.RAID_LEVEL_2MIRROR)


    if disk1.open_disk("D:\\Windows 10\\02. 2Mirror\\Windows_10_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\Windows 10\\02. 2Mirror\\Windows_10_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\Windows 10\\02. 2Mirror\\Windows_10_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    reconstructor = Reconstructor(Define.WINDOWS_10, Define.RAID_LEVEL_2MIRROR)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)

    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()

def test_windows10_3mirror():

    disk1 = StorageSpace(Define.WINDOWS_10, Define.RAID_LEVEL_3MIRROR)
    disk2 = StorageSpace(Define.WINDOWS_10, Define.RAID_LEVEL_3MIRROR)
    disk3 = StorageSpace(Define.WINDOWS_10, Define.RAID_LEVEL_3MIRROR)
    disk4 = StorageSpace(Define.WINDOWS_10, Define.RAID_LEVEL_3MIRROR)
    disk5 = StorageSpace(Define.WINDOWS_10, Define.RAID_LEVEL_3MIRROR)

    if disk1.open_disk("D:\\Windows 10\\03. 3Mirror\\Windows_10_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\Windows 10\\03. 3Mirror\\Windows_10_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\Windows 10\\03. 3Mirror\\Windows_10_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk4.open_disk("D:\\Windows 10\\03. 3Mirror\\Windows_10_Physical_20GB.001"):
        if disk4.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk5.open_disk("D:\\Windows 10\\03. 3Mirror\\Windows_10_Physical_25GB.001"):
        if disk5.parse_disk():
            pass
        else:
            return False
    else:
        return False

    reconstructor = Reconstructor(Define.WINDOWS_10, Define.RAID_LEVEL_3MIRROR)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)
    reconstructor.add_disk(disk4)
    reconstructor.add_disk(disk5)

    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()

def test_windows10_parity():

    disk1 = StorageSpace(Define.WINDOWS_10, Define.RAID_LEVEL_PARITY)
    disk2 = StorageSpace(Define.WINDOWS_10, Define.RAID_LEVEL_PARITY)
    disk3 = StorageSpace(Define.WINDOWS_10, Define.RAID_LEVEL_PARITY)
    disk4 = StorageSpace(Define.WINDOWS_10, Define.RAID_LEVEL_PARITY)

    if disk1.open_disk("D:\\Windows 10\\04. Parity\\Windows_10_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\Windows 10\\04. Parity\\Windows_10_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\Windows 10\\04. Parity\\Windows_10_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk4.open_disk("D:\\Windows 10\\04. Parity\\Windows_10_Physical_20GB.001"):
        if disk4.parse_disk():
            pass
        else:
            return False
    else:
        return False

    reconstructor = Reconstructor(Define.WINDOWS_10, Define.RAID_LEVEL_PARITY)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)
    reconstructor.add_disk(disk4)

    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()

def test_windows_server_2012_simple():

    disk1 = StorageSpace(Define.WINDOWS_SERVER_2012, Define.RAID_LEVEL_SIMPLE)
    disk2 = StorageSpace(Define.WINDOWS_SERVER_2012, Define.RAID_LEVEL_SIMPLE)
    disk3 = StorageSpace(Define.WINDOWS_SERVER_2012, Define.RAID_LEVEL_SIMPLE)

    if disk1.open_disk("D:\\Windows Server 2012\\01. Simple\\Windows_Server_2012_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\Windows Server 2012\\01. Simple\\Windows_Server_2012_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\Windows Server 2012\\01. Simple\\Windows_Server_2012_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    reconstructor = Reconstructor(Define.WINDOWS_SERVER_2012, Define.RAID_LEVEL_SIMPLE)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)

    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()

def test_windows_server_2012_2mirror():

    disk1 = StorageSpace(Define.WINDOWS_SERVER_2012, Define.RAID_LEVEL_2MIRROR)
    disk2 = StorageSpace(Define.WINDOWS_SERVER_2012, Define.RAID_LEVEL_2MIRROR)
    disk3 = StorageSpace(Define.WINDOWS_SERVER_2012, Define.RAID_LEVEL_2MIRROR)

    if disk1.open_disk("D:\\Windows Server 2012\\02. 2Mirror\\Windows_Server_2012_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\Windows Server 2012\\02. 2Mirror\\Windows_Server_2012_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\Windows Server 2012\\02. 2Mirror\\Windows_Server_2012_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    reconstructor = Reconstructor(Define.WINDOWS_SERVER_2012, Define.RAID_LEVEL_2MIRROR)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)

    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()

def test_windows_server_2012_3mirror():

    disk1 = StorageSpace(Define.WINDOWS_SERVER_2012, Define.RAID_LEVEL_3MIRROR)
    disk2 = StorageSpace(Define.WINDOWS_SERVER_2012, Define.RAID_LEVEL_3MIRROR)
    disk3 = StorageSpace(Define.WINDOWS_SERVER_2012, Define.RAID_LEVEL_3MIRROR)
    disk4 = StorageSpace(Define.WINDOWS_SERVER_2012, Define.RAID_LEVEL_3MIRROR)
    disk5 = StorageSpace(Define.WINDOWS_SERVER_2012, Define.RAID_LEVEL_3MIRROR)

    if disk1.open_disk("D:\\Windows Server 2012\\03. 3Mirror\\Windows_Server_2012_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\Windows Server 2012\\03. 3Mirror\\Windows_Server_2012_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\Windows Server 2012\\03. 3Mirror\\Windows_Server_2012_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk4.open_disk("D:\\Windows Server 2012\\03. 3Mirror\\Windows_Server_2012_Physical_20GB.001"):
        if disk4.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk5.open_disk("D:\\Windows Server 2012\\03. 3Mirror\\Windows_Server_2012_Physical_25GB.001"):
        if disk5.parse_disk():
            pass
        else:
            return False
    else:
        return False

    reconstructor = Reconstructor(Define.WINDOWS_SERVER_2012, Define.RAID_LEVEL_3MIRROR)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)
    reconstructor.add_disk(disk4)
    reconstructor.add_disk(disk5)

    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()

def test_windows_server_2012_parity():

    disk1 = StorageSpace(Define.WINDOWS_SERVER_2012, Define.RAID_LEVEL_PARITY)
    disk2 = StorageSpace(Define.WINDOWS_SERVER_2012, Define.RAID_LEVEL_PARITY)
    disk3 = StorageSpace(Define.WINDOWS_SERVER_2012, Define.RAID_LEVEL_PARITY)
    disk4 = StorageSpace(Define.WINDOWS_SERVER_2012, Define.RAID_LEVEL_PARITY)

    if disk1.open_disk("D:\\Windows Server 2012\\04. Parity\\Windows_Server_2012_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\Windows Server 2012\\04. Parity\\Windows_Server_2012_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\Windows Server 2012\\04. Parity\\Windows_Server_2012_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk4.open_disk("D:\\Windows Server 2012\\04. Parity\\Windows_Server_2012_Physical_20GB.001"):
        if disk4.parse_disk():
            pass
        else:
            return False
    else:
        return False

    reconstructor = Reconstructor(Define.WINDOWS_SERVER_2012, Define.RAID_LEVEL_PARITY)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)
    reconstructor.add_disk(disk4)

    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()

def test_windows_server_2016_simple():

    disk1 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_SIMPLE)
    disk2 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_SIMPLE)
    disk3 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_SIMPLE)

    if disk1.open_disk("D:\\Windows Server 2016\\01. Simple\\Windows_Server_2016_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\Windows Server 2016\\01. Simple\\Windows_Server_2016_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\Windows Server 2016\\01. Simple\\Windows_Server_2016_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    reconstructor = Reconstructor(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_SIMPLE)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)

    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()

def test_windows_server_2016_2mirror():

    disk1 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_2MIRROR)
    disk2 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_2MIRROR)
    disk3 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_2MIRROR)

    if disk1.open_disk("D:\\Windows Server 2016\\02. 2Mirror\\Windows_Server_2016_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\Windows Server 2016\\02. 2Mirror\\Windows_Server_2016_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\Windows Server 2016\\02. 2Mirror\\Windows_Server_2016_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    reconstructor = Reconstructor(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_2MIRROR)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)

    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()

def test_windows_server_2016_3mirror():

    disk1 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_3MIRROR)
    disk2 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_3MIRROR)
    disk3 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_3MIRROR)
    disk4 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_3MIRROR)
    disk5 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_3MIRROR)

    if disk1.open_disk("D:\\Windows Server 2016\\03. 3Mirror\\Windows_Server_2016_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\Windows Server 2016\\03. 3Mirror\\Windows_Server_2016_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\Windows Server 2016\\03. 3Mirror\\Windows_Server_2016_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk4.open_disk("D:\\Windows Server 2016\\03. 3Mirror\\Windows_Server_2016_Physical_20GB.001"):
        if disk4.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk5.open_disk("D:\\Windows Server 2016\\03. 3Mirror\\Windows_Server_2016_Physical_25GB.001"):
        if disk5.parse_disk():
            pass
        else:
            return False
    else:
        return False

    reconstructor = Reconstructor(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_3MIRROR)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)
    reconstructor.add_disk(disk4)
    reconstructor.add_disk(disk5)

    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()

def test_windows_server_2016_parity():

    # disk1 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_PARITY)
    # disk2 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_PARITY)
    # disk3 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_PARITY)
    # disk4 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_PARITY)
    #
    # if disk1.open_disk("D:\\Windows Server 2016\\04. Parity\\Windows_Server_2016_Physical_5GB.001"):
    #     if disk1.parse_disk():
    #         pass
    #     else:
    #         return False
    # else:
    #     return False
    #
    # if disk2.open_disk("D:\\Windows Server 2016\\04. Parity\\Windows_Server_2016_Physical_10GB.001"):
    #     if disk2.parse_disk():
    #         pass
    #     else:
    #         return False
    # else:
    #     return False
    #
    # if disk3.open_disk("D:\\Windows Server 2016\\04. Parity\\Windows_Server_2016_Physical_15GB.001"):
    #     if disk3.parse_disk():
    #         pass
    #     else:
    #         return False
    # else:
    #     return False
    #
    # if disk4.open_disk("D:\\Windows Server 2016\\04. Parity\\Windows_Server_2016_Physical_20GB.001"):
    #     if disk4.parse_disk():
    #         pass
    #     else:
    #         return False
    # else:
    #     return False
    #
    #
    #
    # reconstructor = Reconstructor(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_PARITY)
    # reconstructor.add_disk(disk1)
    # reconstructor.add_disk(disk2)
    # reconstructor.add_disk(disk3)
    # reconstructor.add_disk(disk4)
    #
    # reconstructor.parse_metadata()
    #
    # reconstructor.restore_virtual_disk()

    disk1 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_PARITY)
    disk2 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_PARITY)
    disk3 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_PARITY)
    disk4 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_PARITY)

    if disk1.open_disk("D:\\challenge\\5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\challenge\\6GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\challenge\\6GB_2.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk4.open_disk("D:\\challenge\\6GB_3.001"):
        if disk4.parse_disk():
            pass
        else:
            return False
    else:
        return False

    reconstructor = Reconstructor(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_PARITY)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)
    reconstructor.add_disk(disk4)

    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()

def test_windows_server_2016_2parity():

    disk1 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_2PARITY)
    disk2 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_2PARITY)
    disk3 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_2PARITY)
    disk4 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_2PARITY)
    disk5 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_2PARITY)
    disk6 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_2PARITY)
    disk7 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_2PARITY)
    """
    if disk1.open_disk("D:\\Windows Server 2016\\05. DualParity\\Parity_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\Windows Server 2016\\05. DualParity\\Parity_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\Windows Server 2016\\05. DualParity\\Parity_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk4.open_disk("D:\\Windows Server 2016\\05. DualParity\\Parity_20GB.001"):
        if disk4.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk5.open_disk("D:\\Windows Server 2016\\05. DualParity\\Parity_25GB.001"):
        if disk5.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk6.open_disk("D:\\Windows Server 2016\\05. DualParity\\Parity_30GB.001"):
        if disk6.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk7.open_disk("D:\\Windows Server 2016\\05. DualParity\\Parity_35GB.001"):
        if disk7.parse_disk():
            pass
        else:
            return False
    else:
        return False"""

    if disk1.open_disk("D:\\Windows Server 2016\\dualParity_New\\5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\Windows Server 2016\\dualParity_New\\10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\Windows Server 2016\\dualParity_New\\15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk4.open_disk("D:\\Windows Server 2016\\dualParity_New\\20GB.001"):
        if disk4.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk5.open_disk("D:\\Windows Server 2016\\dualParity_New\\25GB.001"):
        if disk5.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk6.open_disk("D:\\Windows Server 2016\\dualParity_New\\30GB.001"):
        if disk6.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk7.open_disk("D:\\Windows Server 2016\\dualParity_New\\35GB.001"):
        if disk7.parse_disk():
            pass
        else:
            return False
    else:
        return False

    reconstructor = Reconstructor(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_2PARITY)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)
    reconstructor.add_disk(disk4)
    reconstructor.add_disk(disk5)
    reconstructor.add_disk(disk6)
    reconstructor.add_disk(disk7)


    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()

def test_windows_server_2019_simple():

    disk1 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_SIMPLE)
    disk2 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_SIMPLE)
    disk3 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_SIMPLE)

    if disk1.open_disk("D:\\Windows Server 2019\\01. Simple\\Windows_Server_2019_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\Windows Server 2019\\01. Simple\\Windows_Server_2019_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\Windows Server 2019\\01. Simple\\Windows_Server_2019_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    reconstructor = Reconstructor(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_SIMPLE)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)

    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()

def test_windows_server_2019_2mirror():

    disk1 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_2MIRROR)
    disk2 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_2MIRROR)
    disk3 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_2MIRROR)

    if disk1.open_disk("D:\\Windows Server 2019\\02. 2Mirror\\Windows_Server_2019_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\Windows Server 2019\\02. 2Mirror\\Windows_Server_2019_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\Windows Server 2019\\02. 2Mirror\\Windows_Server_2019_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    reconstructor = Reconstructor(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_2MIRROR)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)

    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()

def test_windows_server_2019_3mirror():

    disk1 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_3MIRROR)
    disk2 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_3MIRROR)
    disk3 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_3MIRROR)
    disk4 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_3MIRROR)
    disk5 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_3MIRROR)

    if disk1.open_disk("D:\\Windows Server 2019\\03. 3Mirror\\Windows_Server_2019_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\Windows Server 2019\\03. 3Mirror\\Windows_Server_2019_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\Windows Server 2019\\03. 3Mirror\\Windows_Server_2019_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk4.open_disk("D:\\Windows Server 2019\\03. 3Mirror\\Windows_Server_2019_Physical_20GB.001"):
        if disk4.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk5.open_disk("D:\\Windows Server 2019\\03. 3Mirror\\Windows_Server_2019_Physical_25GB.001"):
        if disk5.parse_disk():
            pass
        else:
            return False
    else:
        return False

    reconstructor = Reconstructor(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_3MIRROR)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)
    reconstructor.add_disk(disk4)
    reconstructor.add_disk(disk5)

    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()

def test_windows_server_2019_parity():

    disk1 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_PARITY)
    disk2 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_PARITY)
    disk3 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_PARITY)
    disk4 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_PARITY)
    disk5 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_PARITY)
    disk6 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_PARITY)
    disk7 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_PARITY)

    if disk1.open_disk("D:\\Windows Server 2019\\04. Parity\\Windows_Server_2019_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\Windows Server 2019\\04. Parity\\Windows_Server_2019_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\Windows Server 2019\\04. Parity\\Windows_Server_2019_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk4.open_disk("D:\\Windows Server 2019\\04. Parity\\Windows_Server_2019_Physical_20GB.001"):
        if disk4.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk5.open_disk("D:\\Windows Server 2019\\04. Parity\\Windows_Server_2019_Physical_25GB.001"):
        if disk5.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk6.open_disk("D:\\Windows Server 2019\\04. Parity\\Windows_Server_2019_Physical_30GB.001"):
        if disk6.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk7.open_disk("D:\\Windows Server 2019\\04. Parity\\Windows_Server_2019_Physical_35GB.001"):
        if disk7.parse_disk():
            pass
        else:
            return False
    else:
        return False


    reconstructor = Reconstructor(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_PARITY)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)
    reconstructor.add_disk(disk4)
    reconstructor.add_disk(disk5)
    reconstructor.add_disk(disk6)
    reconstructor.add_disk(disk7)

    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()

def test_windows_server_2019_2parity():

    disk1 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_2PARITY)
    disk2 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_2PARITY)
    disk3 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_2PARITY)
    disk4 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_2PARITY)
    disk5 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_2PARITY)
    disk6 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_2PARITY)
    disk7 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_2PARITY)

    if disk1.open_disk("D:\\Windows Server 2019\\05. DualParity\\Parity_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\Windows Server 2019\\05. DualParity\\Parity_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\Windows Server 2019\\05. DualParity\\Parity_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk4.open_disk("D:\\Windows Server 2019\\05. DualParity\\Parity_20GB.001"):
        if disk4.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk5.open_disk("D:\\Windows Server 2019\\05. DualParity\\Parity_25GB.001"):
        if disk5.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk6.open_disk("D:\\Windows Server 2019\\05. DualParity\\Parity_30GB.001"):
        if disk6.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk7.open_disk("D:\\Windows Server 2019\\05. DualParity\\Parity_35GB.001"):
        if disk7.parse_disk():
            pass
        else:
            return False
    else:
        return False



    reconstructor = Reconstructor(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_2PARITY)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)
    reconstructor.add_disk(disk4)
    reconstructor.add_disk(disk5)
    reconstructor.add_disk(disk6)
    reconstructor.add_disk(disk7)


    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()

def test_windows_server_2019_challenge():

    disk1 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_SIMPLE)
    disk2 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_SIMPLE)
    disk3 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_SIMPLE)
    disk4 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_SIMPLE)

    if disk1.open_disk("D:\\disk1_image.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\disk2_image.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\disk3_image.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk4.open_disk("D:\\disk4_image.001"):
        if disk4.parse_disk():
            pass
        else:
            return False
    else:
        return False

    reconstructor = Reconstructor(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_SIMPLE)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)
    reconstructor.add_disk(disk4)

    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()

def test_windows_server_2019_simple2():

    disk1 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_SIMPLE)
    disk2 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_SIMPLE)
    disk3 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_SIMPLE)

    if disk1.open_disk("D:\\Windows Server 2019\\new_simple\\5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\Windows Server 2019\\new_simple\\10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\Windows Server 2019\\new_simple\\15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    reconstructor = Reconstructor(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_SIMPLE)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)

    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()


def test_windows_server_2019_parity2():

    disk1 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_PARITY)
    disk2 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_PARITY)
    disk3 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_PARITY)
    disk4 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_PARITY)
    disk5 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_PARITY)
    disk6 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_PARITY)
    disk7 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_PARITY)

    if disk1.open_disk("D:\\Windows Server 2019\\new_parity\\5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\Windows Server 2019\\new_parity\\5GB_2.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\Windows Server 2019\\new_parity\\5GB_3.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk4.open_disk("D:\\Windows Server 2019\\new_parity\\5GB_4.001"):
        if disk4.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk5.open_disk("D:\\Windows Server 2019\\new_parity\\5GB_5.001"):
        if disk5.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk6.open_disk("D:\\Windows Server 2019\\new_parity\\5GB_6.001"):
        if disk6.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk7.open_disk("D:\\Windows Server 2019\\new_parity\\5GB_7.001"):
        if disk7.parse_disk():
            pass
        else:
            return False
    else:
        return False


    reconstructor = Reconstructor(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_PARITY)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)
    reconstructor.add_disk(disk4)
    reconstructor.add_disk(disk5)
    reconstructor.add_disk(disk6)
    reconstructor.add_disk(disk7)

    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()

def test_windows_server_2019_2parity2():

    disk1 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_2PARITY)
    disk2 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_2PARITY)
    disk3 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_2PARITY)
    disk4 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_2PARITY)
    disk5 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_2PARITY)
    disk6 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_2PARITY)
    disk7 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_2PARITY)
    disk8 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_2PARITY)
    disk9 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_2PARITY)
    disk10 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_2PARITY)
    disk11 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_2PARITY)
    disk12 = StorageSpace(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_2PARITY)

    if disk1.open_disk("D:\\Windows Server 2019\\05. 2Parity\\5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("D:\\Windows Server 2019\\05. 2Parity\\10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("D:\\Windows Server 2019\\05. 2Parity\\10GB_2.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk4.open_disk("D:\\Windows Server 2019\\05. 2Parity\\10GB_3.001"):
        if disk4.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk5.open_disk("D:\\Windows Server 2019\\05. 2Parity\\10GB_4.001"):
        if disk5.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk6.open_disk("D:\\Windows Server 2019\\05. 2Parity\\10GB_5.001"):
        if disk6.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk7.open_disk("D:\\Windows Server 2019\\05. 2Parity\\10GB_6.001"):
        if disk7.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk8.open_disk("D:\\Windows Server 2019\\05. 2Parity\\10GB_7.001"):
        if disk8.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk9.open_disk("D:\\Windows Server 2019\\05. 2Parity\\10GB_8.001"):
        if disk9.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk10.open_disk("D:\\Windows Server 2019\\05. 2Parity\\10GB_9.001"):
        if disk10.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk11.open_disk("D:\\Windows Server 2019\\05. 2Parity\\15GB.001"):
        if disk11.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk12.open_disk("D:\\Windows Server 2019\\05. 2Parity\\20GB.001"):
        if disk12.parse_disk():
            pass
        else:
            return False
    else:
        return False

    reconstructor = Reconstructor(Define.WINDOWS_SERVER_2019, Define.RAID_LEVEL_2PARITY)
    reconstructor.add_disk(disk1)
    reconstructor.add_disk(disk2)
    reconstructor.add_disk(disk3)
    reconstructor.add_disk(disk4)
    reconstructor.add_disk(disk5)
    reconstructor.add_disk(disk6)
    reconstructor.add_disk(disk7)
    reconstructor.add_disk(disk8)
    reconstructor.add_disk(disk9)
    reconstructor.add_disk(disk10)
    reconstructor.add_disk(disk11)
    reconstructor.add_disk(disk12)

    reconstructor.parse_metadata()

    reconstructor.restore_virtual_disk()

if __name__ == "__main__":
    #test_windows8_simple()
    #test_windows8_2mirror()
    #test_windows8_3mirror()
    #test_windows8_parity()

    #test_windows_server_2012_simple()
    #test_windows_server_2012_2mirror()
    #test_windows_server_2012_3mirror()
    #test_windows_server_2012_parity()

    #test_windows10_simple()
    #test_windows10_2mirror()
    #test_windows10_3mirror()
    #test_windows10_parity()

    #test_windows_server_2016_simple()
    #test_windows_server_2016_2mirror()
    #test_windows_server_2016_3mirror()
    #test_windows_server_2016_parity()
    #test_windows_server_2016_2parity()

    #test_windows_server_2019_simple()
    #test_windows_server_2019_2mirror()
    #test_windows_server_2019_3mirror()
    #test_windows_server_2019_parity()
    #test_windows_server_2019_2parity()

    #test_windows_server_2019_challenge()
    #test_windows_server_2019_simple2()
    #test_windows_server_2019_parity2()
    test_windows_server_2019_2parity2()

