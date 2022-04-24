import grpc

from company_srv.model.model import Company
from company_srv.proto import company_pb2, company_pb2_grpc


class CompanyTest:
    def __init__(self,host='192.168.50.1',port=3300):
        # 得用filter/dns发现了
        print(f'{host}:{port}')
        channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = company_pb2_grpc.CompanyStub(channel)

    def GetList(self):
        res = self.stub.GetCompanyList(company_pb2.GetCompanyListRequest(limit=1))
        print(res)

    def Get(self,id):
        res = self.stub.GetCompanyDetail(company_pb2.GetCompanyDetailRequest(id=id))
        print(res)

    def Create(self):
        Company()
        '''
         name = CharField(verbose_name='名称')
        desc = TextField(verbose_name='简介')
        website = CharField(verbose_name='官网', null=True)
        config = TextField(verbose_name='配置信息', null=True)
        size = EnumField(verbose_name='企业规模等级', default=1)
        tags = JSONField(verbose_name='标签', null=True)
    
        address = CharField(verbose_name='地址')
        info = JSONField(verbose_name='其他信息', null=True)
    
        creator_id = IntegerField(verbose_name='创建者,群主')
        parent_id = IntegerField(verbose_name='父id,子公司', default=0)
        status = EnumField(verbose_name='状态', default=1)
        '''
        res = self.stub.CreateCompany(company_pb2.CreateCompanyRequest(name="测试公司",desc="测试公司简介",website="http://www.baidu.com",config="",size=2,
                                                                        address="www.www",creator_id=3))
        print(res)
        return res.id

    def Update(self,id):
        res=self.stub.UpdateCompany(company_pb2.UpdateCompanyRequest(id=id,name="test3",desc="testt2",website="www.github.com",size=1,address="sad"))
        print(res)

    def Delete(self,id):
        res = self.stub.DeleteCompany(company_pb2.DeleteCompanyRequest(id=id))
        print(res)

    def GetMyCompanyList(self):
        res = self.stub.GetMyCompanyList(company_pb2.GetMyCompanyListRequest(user_id=3))
        print(res)

    def GetCompanyUserIdList(self):
        res = self.stub.GetCompanyUserIdList(company_pb2.GetCompanyUserListRequest(company_id=3))
        print(res)

    def CreateUserCompany(self):
        res = self.stub.CreateUserCompany(company_pb2.SaveUserCompanyRequest(company_id=3,user_id=2))
        print(res)

    def UpdateUserCompany(self):
        res = self.stub.UpdateUserCompany(company_pb2.SaveUserCompanyRequest(company_id=3, user_id=2,status=3))
        print(res)

    def DeleteUserCompany(self):
        res = self.stub.DeleteUserCompany(company_pb2.DeleteUserCompanyRequest(company_id=3, user_id=2))
        print(res)

    def GetListByIds(self):
        res = self.stub.GetCompanyListByIds(company_pb2.GetCompanyListByIdsRequest(ids=[1,2,3,4]))
        print(res)


if __name__ == '__main__':
    test = CompanyTest('192.168.50.1',8003)
    print("--------------create")
    id = test.Create()

    test.GetList()
    test.Get(id)

    print("--------------update")
    test.Update(id)
    print("--------------delete")
    # test.DeleteCompany()
    test.GetList()
    test.Get(id)

    test.GetCompanyUserIdList()
    test.CreateUserCompany()

    test.UpdateUserCompany()
    test.DeleteUserCompany()

    test.GetListByIds()