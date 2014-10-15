#encoding:utf-8


from Configs import GlobalConfig
import ITC03_SetUp as DataModule

'''
@note: Pre-TestData
'''
host_name = 'node-ITC03010702'
# 前提1：创建一个主机
xml_host_info = '''
<host>
    <name>%s</name>
    <address>%s</address>
    <root_password>%s</root_password>
    <cluster>
        <name>%s</name>
    </cluster>
</host>
''' % (host_name, GlobalConfig.Hosts['node4']['ip'], GlobalConfig.Hosts['node4']['password'], DataModule.cluster_name)

'''
@note: Test-Data
'''


'''
@note: Post-TestData
'''
xml_host_del_option = '''
<action>
    <force>true</force>
    <async>false</async>
</action>
'''

'''
@note: ExpectedResult
'''
expected_status_code_create_host = 201          # 创建主机操作成功，状态码
expected_status_code_deactive_host_fail = 409   # 维护主机操作失败，状态码
expected_info_deactive_host_fail = '''
<action>
    <status>
        <state>failed</state>
    </status>
    <fault>
        <reason>Operation Failed</reason>
        <detail>[Cannot switch Host to Maintenance mode. Host is already in Maintenance mode.]</detail>
    </fault>
</action>
'''
expected_status_code_del_host = 200             # 删除主机操作成功，状态码
