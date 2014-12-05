#encoding:utf-8

__authors__ = ['"Wei Keke" <keke.wei@cs2c.com.cn>']
__version__ = "V0.1"

'''
# ChangeLog:
#---------------------------------------------------------------------------------
# Version        Date                Desc                            Author
#---------------------------------------------------------------------------------
# V0.1           2014/10/09          初始版本                                                            Wei Keke 
#---------------------------------------------------------------------------------
'''

import TestData.Disk.ITC08_SetUp as ModuleData

'''---------------------------------------------------------------------------------------------------
@note: PreData
---------------------------------------------------------------------------------------------------'''
sd_name = ModuleData.data1_nfs_name
cluster_name = ModuleData.cluster_nfs_name
vm_name = 'VM-ITC080402'
vm_info = '''
<vm>
        <name>%s</name>
        <description>Virtual Machine 2</description>
        <type>server</type>
        <memory>536870912</memory>
        <cluster>
            <name>%s</name>
        </cluster>
        <template>
            <name>Blank</name>
        </template>
        <cpu>
            <topology sockets="2" cores="1"/>
        </cpu>
        <os>
            <boot dev="cdrom"/>
            <boot dev="hd"/>
        </os>
    </vm>
''' % (vm_name, cluster_name)

disk_name = 'DISK-ITC080402'
disk_info = '''
<disk>
    <alias>%s</alias>
    <name>DISK-ITC080402</name>
    <storage_domains>
        <storage_domain>
            <name>%s</name>
        </storage_domain>
    </storage_domains>
    <size>114748364</size>
    <sparse>false</sparse>
    <interface>virtio</interface>
    <format>raw</format>
    <bootable>true</bootable>
    <shareable>false</shareable>
    <wipe_after_delete>false</wipe_after_delete>
</disk>
''' % (disk_name, sd_name)

temp_name = 'Template-ITC080402'
temp_info = '''
<template>
    <name>Template-ITC080402</name>
    <vm id="%s"/>
</template>
'''

'''---------------------------------------------------------------------------------------------------
@note: ExpectedData
---------------------------------------------------------------------------------------------------'''
expected_status_code = 400
expected_info = '''
<fault>
    <reason>Operation Failed</reason>
    <detail>[Cannot remove Virtual Machine Disk. Provided wrong storage domain, which is not related to disk.]</detail>
</fault>
'''