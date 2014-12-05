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

'''---------------------------------------------------------------------------------------------
@note: PreData 
---------------------------------------------------------------------------------------------'''
dc_name = ModuleData.dc_name
dc_id = DataCenterAPIs().getDataCenterIdByName(ModuleData.dc_name)
cluster_name = 'Cluster-ITC020203'
cluster_info='''
<cluster>
        <name>%s</name>
        <cpu id="Intel Penryn Family"/>
        <data_center id="%s"/>
</cluster>
''' % (cluster_name, dc_id)

nw_name = 'network_ITC020203'
nw_info = '''
<network>
    <name>%s</name>
    <data_center id= "%s"/> 
</network>
''' % (nw_name, dc_id)

'''---------------------------------------------------------------------------------------------
@note: ExpectedResult
---------------------------------------------------------------------------------------------'''
status_code = 201