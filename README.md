# SSR(Storage Space Reconstructor)

## Introduction

Storage Spaces is a technology in Windows and Windows Server that can help protect your data from drive failures. It is conceptually similar to RAID, implemented in software. You can use Storage Spaces to group three or more drives together into a storage pool and then use capacity from that pool to create Storage Spaces. These typically store extra copies of your data so if one of your drives fails, you still have an intact copy of your data. If you run low on capacity, just add more drives to the storage pool.
We developed a tool called Storage Space Reconstructor (SSR). This tool was developed in the form of a standalone application that creates a virtual disk by inputting physical disks. The virtual disk created by the forensic investigator can be used with traditional forensic tools such as AXI-OM, Autopsy, and EnCase. We uploaded the tool and the set of disks for tool-testing.

* Testset : https://drive.google.com/drive/folders/1R2Tew9ptw0OxLUR1DhJzn_3GMGY_-ZN-?usp=sharing

You can download the testset from the above URL. And if you move the testset to the tests folder and run test_storagespace.py, you can use this tool.

##### Other information
* Documentation: 
