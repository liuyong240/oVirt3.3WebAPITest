#encoding:utf-8

__authors__ = ['wei keke']
__version__ = "V0.1"

'''
# ChangeLog:
#---------------------------------------------------------------------------------
# Version        Date                Desc                            Author
#---------------------------------------------------------------------------------
# V0.1           2014/10/17          初始版本                                                         
#---------------------------------------------------------------------------------
'''

import TestData.Cluster.ITC02_Setup as ModuleData
from TestAPIs.DataCenterAPIs import DataCenterAPIs
from Configs.GlobalConfig import Hosts

'''--------------------------------------------------------------------------------------
更新集群-01集群内有主机时更改cpu类型
--------------------------------------------------------------------------------------'''
dc_id = DataCenterAPIs().getDataCenterIdByName(ModuleData.dc_name)
cluster_name = 'Cluster-ITC0201040202'

'''--------------------------------------------------------------------------------------
@note: PreData
--------------------------------------------------------------------------------------'''
cluster_info = '''
<cluster>
        <name>%s</name>
        <cpu id="Intel Conroe Family"/>
        <data_center  id="%s"/>
</cluster>
''' % (cluster_name, dc_id)

host = Hosts['node2']
host_name = 'node-ITC0201040202'
host_ip = host['ip']
host_password = host['password']
host_info = '''
    <host>
        <cluster>
            <name>%s</name>
        </cluster>
        <name>%s</name>
        <address>%s</address>
        <root_password>%s</root_password>
    </host>
''' % (cluster_name, host_name, host_ip, host_password)

'''--------------------------------------------------------------------------------------
@note: TestData
--------------------------------------------------------------------------------------'''
cluster_info_new = '''
<cluster>
        <name>%s</name>
        <cpu id="Intel Haswell Family"/>
        <data_center  id="%s"/>
</cluster>
''' %(cluster_name,dc_id)

host_del_option = '''
<action>
    <force>true</force>
    <async>false</async>
</action>
'''

'''--------------------------------------------------------------------------------------
@note: ExpectedData
--------------------------------------------------------------------------------------'''
status_code = 409
expected_info = '''
<fault>
    <reason>Operation Failed</reason>
    <detail>[Cannot change Cluster CPU to higher CPU type when there are active Hosts with lower CPU type.\n-Please move Hosts with lower CPU to maintenance first.]</detail>
</fault>
'''