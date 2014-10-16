#encoding:utf-8


from Configs import GlobalConfig
import ITC03_SetUp as DM

'''
@note: Pre-TestData
'''
# 配置电源管理选项的host的相关信息
host1 = GlobalConfig.Hosts['node1']
host2 = GlobalConfig.Hosts['node4']
host1_name = 'node-ITC03011301-1'
host2_name = 'node-ITC03011301-2'
xml_host1_info = '''
<host>
    <name>%s</name>
    <address>%s</address>
    <root_password>%s</root_password>
    <cluster>
        <name>%s</name>
    </cluster>
</host>
''' % (host1_name, host1['ip'], host1['password'], DM.cluster_name)
xml_host2_info = '''
<host>
    <name>%s</name>
    <address>%s</address>
    <root_password>%s</root_password>
    <cluster>
        <name>%s</name>
    </cluster>
    <power_management type="%s">
        <enabled>true</enabled>
        <address>%s</address>
        <username>%s</username>
        <password>%s</password>
    </power_management>
</host>
''' % (host2_name, \
       host2['ip'], \
       host2['password'], \
       DM.cluster_name, \
       host2['IMM']['type'], \
       host2['IMM']['ip'], \
       host2['IMM']['user'], \
       host2['IMM']['password']
       )

'''
@note: Test-Data
'''


'''
@note: Post-TestData
'''
# 资源清理时删除host所用的选项（强制删除/同步）
xml_host_del_option = '''
<action>
    <force>true</force>
    <async>false</async>
</action>
'''

'''
@note: ExpectedResult
'''
expected_status_code_create_host = 201          # 创建主机操作的期望状态码
expected_status_code_select_spm = 200           # 手动设置SPM操作成功，返回状态码
expected_status_code_deactive_host = 200        # 维护主机操作的期望状态码
expected_status_code_del_host = 200             # 删除主机操作的期望状态码
