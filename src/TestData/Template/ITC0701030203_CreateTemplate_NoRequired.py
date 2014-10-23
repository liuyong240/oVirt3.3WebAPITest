#encoding:utf-8
from TestAPIs.StorageDomainAPIs import StorageDomainAPIs
from TestData.Template import ITC07_SetUp as ModuleData
from TestAPIs.VirtualMachineAPIs import VirtualMachineAPIs
'''
@note: TestData
'''
'''
@note: 存储域名称应该由该模块的Setup用例初始化获得，这里暂时用字符串代替
'''

vm_id = VirtualMachineAPIs().getVmIdByName(ModuleData.vm_name)
temp_name = 'template-ke'
temp_info='''
<data_driver>
    <template>
        <name>%s</name>                               
    </template>
    <template>
        <vm id = "%s"/>                               
    </template>
</data_driver>
'''%(temp_name,vm_id)
'''
@note: ExpectedData
'''
expected_status_code = 400
expected_info_list = [
'''
<fault>
    <reason>Incomplete parameters</reason>
    <detail>Template [vm.id|name] required for add</detail>
</fault>
'''
,
'''
<fault>
    <reason>Incomplete parameters</reason>
    <detail>Template [name] required for add</detail>
</fault>
'''
]
