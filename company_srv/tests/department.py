import grpc

from company_srv.model.model import Department
from company_srv.proto import department_pb2, department_pb2_grpc


class DepartmentTest:
    def __init__(self, port=3300):
        # 得用filter/dns发现了
        channel = grpc.insecure_channel(f"192.168.50.1:{port}")
        self.stub = department_pb2_grpc.DepartmentStub(channel)

    def GetDepartmentList(self):
        res = self.stub.GetDepartmentList(department_pb2.GetDepartmentListRequest(limit=1))
        print(res)

    def GetDepartmentDetail(self):
        res = self.stub.GetDepartmentDetail(department_pb2.GetDepartmentDetailRequest(id=1))
        print(res)

    def CreateDepartment(self):
        Department()
        '''
        company_id = IntegerField(verbose_name='公司id')
        parent_id = IntegerField(verbose_name='父级id')
        icon = IntegerField(verbose_name='图标', default=0)
        name = CharField(verbose_name='名称')
        remark = CharField(verbose_name='备注', null=True)
        desc = TextField(verbose_name='简介', null=True)
        size = EnumField(verbose_name='部门规模等级', default=1)
    
        info = JSONField(verbose_name='其他信息', null=True)
        creator_id = IntegerField(verbose_name='负责人')
        status = EnumField(verbose_name='状态', default=1)
        '''
        res = self.stub.CreateDepartment(
            department_pb2.CreateDepartmentRequest(name="测试公司", remark="测试公司备注", icon=111, company_id=2,
                                                   size=2,
                                                   desc="www.www", creator_id=3))
        print(res)

    def UpdateDepartment(self):
        res = self.stub.UpdateDepartment(
            department_pb2.UpdateDepartmentRequest(id=1, name="test2", desc="testt2", size=1))
        print(res)

    def DeleteDepartment(self):
        res = self.stub.DeleteDepartment(department_pb2.DeleteUserDepartmentRequest(id=6))
        print(res)

    def GetMyDepartmentList(self):
        res = self.stub.GetMyDepartmentList(department_pb2.GetMyDepartmentListRequest(user_id=3))
        print(res)

    def GetDepartmentUserIdList(self):
        res = self.stub.GetDepartmentUserIdList(department_pb2.GetDepartmentUserListRequest(department_id=3))
        print(res)

    def CreateUserDepartment(self):
        res = self.stub.CreateUserDepartment(department_pb2.SaveUserDepartmentRequest(department_id=3, user_id=2))
        print(res)

    def UpdateUserDepartment(self):
        res = self.stub.UpdateUserDepartment(
            department_pb2.SaveUserDepartmentRequest(department_id=3, user_id=4, status=3))
        print(res)

    def DeleteUserDepartment(self):
        res = self.stub.DeleteUserDepartment(department_pb2.DeleteUserDepartmentRequest(department_id=3, user_id=2))
        print(res)


if __name__ == '__main__':
    test = DepartmentTest(7702)
    print("--------------create")
    test.CreateDepartment()

    test.GetDepartmentList()
    test.GetDepartmentDetail()

    print("--------------update")
    test.UpdateDepartment()
    print("--------------delete")
    # test.DeleteDepartment()
    test.GetDepartmentList()
    test.GetMyDepartmentList()

    test.GetDepartmentUserIdList()
    test.CreateUserDepartment()

    test.UpdateUserDepartment()
    test.DeleteUserDepartment()
