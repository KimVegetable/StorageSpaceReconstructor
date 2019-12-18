from SSR.storagespace import StorageSpace
from SSR.reconstructor import Reconstructor
from SSR.define import Define

def test_windows8_simple():

    disk1 = StorageSpace(Define.WINDOWS_8, Define.RAID_LEVEL_SIMPLE)
    disk2 = StorageSpace(Define.WINDOWS_8, Define.RAID_LEVEL_SIMPLE)
    disk3 = StorageSpace(Define.WINDOWS_8, Define.RAID_LEVEL_SIMPLE)

    if disk1.open_disk("F:\\Windows 8.1\\01. Simple\\Windows_8.1_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("F:\\Windows 8.1\\01. Simple\\Windows_8.1_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("F:\\Windows 8.1\\01. Simple\\Windows_8.1_Physical_15GB.001"):
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

    if disk1.open_disk("F:\\Windows 8.1\\02. 2Mirror\\Windows_8.1_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("F:\\Windows 8.1\\02. 2Mirror\\Windows_8.1_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("F:\\Windows 8.1\\02. 2Mirror\\Windows_8.1_Physical_15GB.001"):
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

    if disk1.open_disk("F:\\Windows 8.1\\03. 3Mirror\\Windows_8.1_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("F:\\Windows 8.1\\03. 3Mirror\\Windows_8.1_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("F:\\Windows 8.1\\03. 3Mirror\\Windows_8.1_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk4.open_disk("F:\\Windows 8.1\\03. 3Mirror\\Windows_8.1_Physical_20GB.001"):
        if disk4.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk5.open_disk("F:\\Windows 8.1\\03. 3Mirror\\Windows_8.1_Physical_25GB.001"):
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

def test_windows10_simple():

    disk1 = StorageSpace(Define.WINDOWS_10, Define.RAID_LEVEL_SIMPLE)
    disk2 = StorageSpace(Define.WINDOWS_10, Define.RAID_LEVEL_SIMPLE)
    disk3 = StorageSpace(Define.WINDOWS_10, Define.RAID_LEVEL_SIMPLE)

    if disk1.open_disk("F:\\Windows 10\\01. Simple\\Windows_10_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("F:\\Windows 10\\01. Simple\\Windows_10_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("F:\\Windows 10\\01. Simple\\Windows_10_Physical_15GB.001"):
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


    if disk1.open_disk("F:\\Windows 10\\02. 2Mirror\\Windows_10_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("F:\\Windows 10\\02. 2Mirror\\Windows_10_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("F:\\Windows 10\\02. 2Mirror\\Windows_10_Physical_15GB.001"):
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

    if disk1.open_disk("F:\\Windows 10\\03. 3Mirror\\Windows_10_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("F:\\Windows 10\\03. 3Mirror\\Windows_10_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("F:\\Windows 10\\03. 3Mirror\\Windows_10_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk4.open_disk("F:\\Windows 10\\03. 3Mirror\\Windows_10_Physical_20GB.001"):
        if disk4.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk5.open_disk("F:\\Windows 10\\03. 3Mirror\\Windows_10_Physical_25GB.001"):
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

    if disk1.open_disk("F:\\Windows 10\\04. Parity\\Windows_10_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("F:\\Windows 10\\04. Parity\\Windows_10_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("F:\\Windows 10\\04. Parity\\Windows_10_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk4.open_disk("F:\\Windows 10\\04. Parity\\Windows_10_Physical_20GB.001"):
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

    if disk1.open_disk("F:\\Windows Server 2012\\01. Simple\\Windows_Server_2012_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("F:\\Windows Server 2012\\01. Simple\\Windows_Server_2012_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("F:\\Windows Server 2012\\01. Simple\\Windows_Server_2012_Physical_15GB.001"):
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

    if disk1.open_disk("F:\\Windows Server 2012\\02. 2Mirror\\Windows_Server_2012_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("F:\\Windows Server 2012\\02. 2Mirror\\Windows_Server_2012_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("F:\\Windows Server 2012\\02. 2Mirror\\Windows_Server_2012_Physical_15GB.001"):
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

    if disk1.open_disk("F:\\Windows Server 2012\\03. 3Mirror\\Windows_Server_2012_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("F:\\Windows Server 2012\\03. 3Mirror\\Windows_Server_2012_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("F:\\Windows Server 2012\\03. 3Mirror\\Windows_Server_2012_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk4.open_disk("F:\\Windows Server 2012\\03. 3Mirror\\Windows_Server_2012_Physical_20GB.001"):
        if disk4.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk5.open_disk("F:\\Windows Server 2012\\03. 3Mirror\\Windows_Server_2012_Physical_25GB.001"):
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

    if disk1.open_disk("F:\\Windows Server 2012\\04. Parity\\Windows_Server_2012_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("F:\\Windows Server 2012\\04. Parity\\Windows_Server_2012_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("F:\\Windows Server 2012\\04. Parity\\Windows_Server_2012_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk4.open_disk("F:\\Windows Server 2012\\04. Parity\\Windows_Server_2012_Physical_20GB.001"):
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

    if disk1.open_disk("F:\\Windows Server 2016\\01. Simple\\Windows_Server_2016_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("F:\\Windows Server 2016\\01. Simple\\Windows_Server_2016_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("F:\\Windows Server 2016\\01. Simple\\Windows_Server_2016_Physical_15GB.001"):
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

    if disk1.open_disk("F:\\Windows Server 2016\\02. 2Mirror\\Windows_Server_2016_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("F:\\Windows Server 2016\\02. 2Mirror\\Windows_Server_2016_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("F:\\Windows Server 2016\\02. 2Mirror\\Windows_Server_2016_Physical_15GB.001"):
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

    if disk1.open_disk("F:\\Windows Server 2016\\03. 3Mirror\\Windows_Server_2016_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("F:\\Windows Server 2016\\03. 3Mirror\\Windows_Server_2016_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("F:\\Windows Server 2016\\03. 3Mirror\\Windows_Server_2016_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk4.open_disk("F:\\Windows Server 2016\\03. 3Mirror\\Windows_Server_2016_Physical_20GB.001"):
        if disk4.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk5.open_disk("F:\\Windows Server 2016\\03. 3Mirror\\Windows_Server_2016_Physical_25GB.001"):
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

    disk1 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_PARITY)
    disk2 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_PARITY)
    disk3 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_PARITY)
    disk4 = StorageSpace(Define.WINDOWS_SERVER_2016, Define.RAID_LEVEL_PARITY)

    if disk1.open_disk("F:\\Windows Server 2016\\04. Parity\\Windows_Server_2016_Physical_5GB.001"):
        if disk1.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk2.open_disk("F:\\Windows Server 2016\\04. Parity\\Windows_Server_2016_Physical_10GB.001"):
        if disk2.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk3.open_disk("F:\\Windows Server 2016\\04. Parity\\Windows_Server_2016_Physical_15GB.001"):
        if disk3.parse_disk():
            pass
        else:
            return False
    else:
        return False

    if disk4.open_disk("F:\\Windows Server 2016\\04. Parity\\Windows_Server_2016_Physical_20GB.001"):
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
    test_windows_server_2016_parity()
