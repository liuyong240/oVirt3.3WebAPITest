#encoding:utf-8

__authors__ = ['"Wei Keke" <keke.wei@cs2c.com.cn>']
__version__ = "V0.1"

'''
# ChangeLog:
#---------------------------------------------------------------------------------
# Version        Date                Desc                            Author
#---------------------------------------------------------------------------------
# V0.1           2014/10/09          初始版本                                                           Wei Keke 
#---------------------------------------------------------------------------------
'''

from TestAPIs.StorageDomainAPIs import StorageDomainAPIs
import TestData.Disk.ITC08_SetUp as ModuleData

'''---------------------------------------------------------------------------------------------------
@note: PreData
---------------------------------------------------------------------------------------------------'''
disk_name = 'Disk-test'
sd_id = StorageDomainAPIs().getStorageDomainIdByName(ModuleData.data1_nfs_name)
disk_info = '''
<data_driver>
<disk>
    <alias>Disk-test</alias>
    <name>Disk-test</name>
    <storage_domains>
        <storage_domain id = "%s"/>
    </storage_domains>
    <size>105906176</size>
    <sparse>true</sparse>
    <interface>virtio</interface>
    <format>raw</format>
    <bootable>true</bootable>
    <shareable>false</shareable>
    <wipe_after_delete>false</wipe_after_delete>
</disk>
<disk>
    <alias>Disk-test</alias>
    <name>Disk-test</name>
    <storage_domains>
        <storage_domain id = "%s"/>
    </storage_domains>
    <size>105906176</size>
    <sparse>false</sparse>
    <interface>virtio</interface>
    <format>cow</format>
    <bootable>true</bootable>
    <shareable>true</shareable>
    <wipe_after_delete>false</wipe_after_delete>
</disk>
<disk>
    <alias>Disk-test</alias>
    <name>Disk-test</name>
    <storage_domains>
        <storage_domain id = "%s"/>
    </storage_domains>
    <size>105906176</size>
    <sparse>true</sparse>
    <interface>virtio</interface>
    <format>cow</format>
    <bootable>true</bootable>
    <shareable>true</shareable>
    <wipe_after_delete>false</wipe_after_delete>
</disk>
</data_driver>
''' % (sd_id, sd_id, sd_id)

'''---------------------------------------------------------------------------------------------------
@note: ExpectedData
---------------------------------------------------------------------------------------------------'''
expected_status_code = [400,400,409]
expected_info_list = [
'''
<fault>
    <reason>Operation Failed</reason>
    <detail>[Cannot add Virtual Machine Disk. Disk configuration (RAW Sparse) is incompatible with the storage domain type.]</detail>
</fault>
'''
,
'''
<fault>
    <reason>Operation Failed</reason>
    <detail>[Cannot add Virtual Machine Disk. Disk configuration (COW Preallocated) is incompatible with the storage domain type.]</detail>
</fault>
'''
,
'''
<fault>
    <reason>Operation Failed</reason>
    <detail>[Cannot add Virtual Machine Disk. Disk's volume format is not supported for shareable disk.]</detail>
</fault>
'''
]