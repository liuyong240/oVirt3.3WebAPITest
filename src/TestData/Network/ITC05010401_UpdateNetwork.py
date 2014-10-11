#encoding:utf-8

nw_name = 'network001'
dc_name = 'Default'


'''
@note: PreData
'''
nw_info = '''
<network>
    <name>%s</name>
    <data_center id= "5849b030-626e-47cb-ad90-3ce782d831b3"/>    
</network>
''' %nw_name

'''
@note:TestData 
'''
new_nw_name = 'network002'
update_info = '''
<network>
    <name>%s</name>
    <description>lalala</description>   
    <mtu>2000</mtu>
</network>
'''%new_nw_name

'''
@note: ExpectedData
'''
expected_status_code = 200