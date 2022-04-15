import grpc

from company_srv.model.model import Company
from company_srv.proto import company_pb2, company_pb2_grpc


class CompanyTest:
    def __init__(self,port=3300):
        # 得用filter/dns发现了
        channel = grpc.insecure_channel(f"192.168.50.1:{port}")
        self.stub = company_pb2_grpc.CompanyStub(channel)

    def GetCompanyList(self):
        res = self.stub.GetCompanyList(company_pb2.GetCompanyListRequest(limit=5))
        print(res)

    def GetCompanyDetail(self):
        res = self.stub.GetCompanyDetail(company_pb2.GetCompanyDetailRequest(id=1))
        print(res)

    def CreateCompany(self):
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

    def UpdateCompany(self):
        res=self.stub.UpdateCompany(company_pb2.UpdateCompanyRequest(id=5,name="test3",desc="testt2",website="www.github.com",size=1,address="sad"))
        print(res)

    def DeleteCompany(self):
        res = self.stub.DeleteCompany(company_pb2.DeleteCompanyRequest(id=6))
        print(res)

    def GetMyCompanyList(self):
        res = self.stub.GetMyCompanyList(company_pb2.GetMyCompanyListRequest(user_id=3))
        print(res)

    def GetCompanyUserIdList(self):
        pass

    def CreateUserCompany(self):
        pass

    def UpdateUserCompany(self):
        pass

    def DeleteUserCompany(self):
        pass


if __name__ == '__main__':
    test = CompanyTest(7702)

    test.GetCompanyList()

    test.GetCompanyDetail()
    print("--------------create")
    test.CreateCompany()
    print("--------------update")
    test.UpdateCompany()
    print("--------------delete")
    # test.DeleteCompany()
    test.GetCompanyList()
    test.GetMyCompanyList()