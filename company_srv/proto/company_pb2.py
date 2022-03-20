# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: company.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rcompany.proto\x1a\x1bgoogle/protobuf/empty.proto\"*\n\x17GetMyCompanyListRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\"%\n\x17GetCompanyDetailRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"R\n\x15GetCompanyListRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05\x12\x0e\n\x06search\x18\x03 \x01(\t\x12\x0c\n\x04sort\x18\x04 \x01(\t\"D\n\x13\x43ompanyListResponse\x12\x1e\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x10.CompanyResponse\x12\r\n\x05total\x18\x02 \x01(\x05\"\"\n\x14\x44\x65leteCompanyRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"\xc3\x01\n\x14UpdateCompanyRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t\x12\x0f\n\x07website\x18\x04 \x01(\t\x12\x0e\n\x06\x63onfig\x18\x05 \x01(\t\x12\x0c\n\x04tags\x18\x06 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x07 \x01(\t\x12\x0c\n\x04info\x18\x08 \x01(\t\x12\x12\n\ncreator_id\x18\t \x01(\x03\x12\x11\n\tparent_id\x18\n \x01(\x03\x12\x0e\n\x06status\x18\x0b \x01(\x05\"\xbe\x01\n\x0f\x43ompanyResponse\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t\x12\x0f\n\x07website\x18\x04 \x01(\t\x12\x0e\n\x06\x63onfig\x18\x05 \x01(\t\x12\x0c\n\x04tags\x18\x06 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x07 \x01(\t\x12\x0c\n\x04info\x18\x08 \x01(\t\x12\x12\n\ncreator_id\x18\t \x01(\x03\x12\x11\n\tparent_id\x18\n \x01(\x03\x12\x0e\n\x06status\x18\x0b \x01(\x05\"\xb7\x01\n\x14\x43reateCompanyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\x12\x0f\n\x07website\x18\x03 \x01(\t\x12\x0e\n\x06\x63onfig\x18\x04 \x01(\t\x12\x0c\n\x04tags\x18\x05 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x06 \x01(\t\x12\x0c\n\x04info\x18\x07 \x01(\t\x12\x12\n\ncreator_id\x18\x08 \x01(\x03\x12\x11\n\tparent_id\x18\t \x01(\x03\x12\x0e\n\x06status\x18\n \x01(\x05\x32\x87\x03\n\x07\x43ompany\x12>\n\x0eGetCompanyList\x12\x16.GetCompanyListRequest\x1a\x14.CompanyListResponse\x12>\n\x10GetCompanyDetail\x12\x18.GetCompanyDetailRequest\x1a\x10.CompanyResponse\x12\x38\n\rCreateCompany\x12\x15.CreateCompanyRequest\x1a\x10.CompanyResponse\x12>\n\rUpdateCompany\x12\x15.UpdateCompanyRequest\x1a\x16.google.protobuf.Empty\x12>\n\rDeleteCompany\x12\x15.DeleteCompanyRequest\x1a\x16.google.protobuf.Empty\x12\x42\n\x10GetMyCompanyList\x12\x18.GetMyCompanyListRequest\x1a\x14.CompanyListResponseB\nZ\x08../protob\x06proto3')



_GETMYCOMPANYLISTREQUEST = DESCRIPTOR.message_types_by_name['GetMyCompanyListRequest']
_GETCOMPANYDETAILREQUEST = DESCRIPTOR.message_types_by_name['GetCompanyDetailRequest']
_GETCOMPANYLISTREQUEST = DESCRIPTOR.message_types_by_name['GetCompanyListRequest']
_COMPANYLISTRESPONSE = DESCRIPTOR.message_types_by_name['CompanyListResponse']
_DELETECOMPANYREQUEST = DESCRIPTOR.message_types_by_name['DeleteCompanyRequest']
_UPDATECOMPANYREQUEST = DESCRIPTOR.message_types_by_name['UpdateCompanyRequest']
_COMPANYRESPONSE = DESCRIPTOR.message_types_by_name['CompanyResponse']
_CREATECOMPANYREQUEST = DESCRIPTOR.message_types_by_name['CreateCompanyRequest']
GetMyCompanyListRequest = _reflection.GeneratedProtocolMessageType('GetMyCompanyListRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMYCOMPANYLISTREQUEST,
  '__module__' : 'company_pb2'
  # @@protoc_insertion_point(class_scope:GetMyCompanyListRequest)
  })
_sym_db.RegisterMessage(GetMyCompanyListRequest)

GetCompanyDetailRequest = _reflection.GeneratedProtocolMessageType('GetCompanyDetailRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCOMPANYDETAILREQUEST,
  '__module__' : 'company_pb2'
  # @@protoc_insertion_point(class_scope:GetCompanyDetailRequest)
  })
_sym_db.RegisterMessage(GetCompanyDetailRequest)

GetCompanyListRequest = _reflection.GeneratedProtocolMessageType('GetCompanyListRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCOMPANYLISTREQUEST,
  '__module__' : 'company_pb2'
  # @@protoc_insertion_point(class_scope:GetCompanyListRequest)
  })
_sym_db.RegisterMessage(GetCompanyListRequest)

CompanyListResponse = _reflection.GeneratedProtocolMessageType('CompanyListResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMPANYLISTRESPONSE,
  '__module__' : 'company_pb2'
  # @@protoc_insertion_point(class_scope:CompanyListResponse)
  })
_sym_db.RegisterMessage(CompanyListResponse)

DeleteCompanyRequest = _reflection.GeneratedProtocolMessageType('DeleteCompanyRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETECOMPANYREQUEST,
  '__module__' : 'company_pb2'
  # @@protoc_insertion_point(class_scope:DeleteCompanyRequest)
  })
_sym_db.RegisterMessage(DeleteCompanyRequest)

UpdateCompanyRequest = _reflection.GeneratedProtocolMessageType('UpdateCompanyRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECOMPANYREQUEST,
  '__module__' : 'company_pb2'
  # @@protoc_insertion_point(class_scope:UpdateCompanyRequest)
  })
_sym_db.RegisterMessage(UpdateCompanyRequest)

CompanyResponse = _reflection.GeneratedProtocolMessageType('CompanyResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMPANYRESPONSE,
  '__module__' : 'company_pb2'
  # @@protoc_insertion_point(class_scope:CompanyResponse)
  })
_sym_db.RegisterMessage(CompanyResponse)

CreateCompanyRequest = _reflection.GeneratedProtocolMessageType('CreateCompanyRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECOMPANYREQUEST,
  '__module__' : 'company_pb2'
  # @@protoc_insertion_point(class_scope:CreateCompanyRequest)
  })
_sym_db.RegisterMessage(CreateCompanyRequest)

_COMPANY = DESCRIPTOR.services_by_name['Company']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\010../proto'
  _GETMYCOMPANYLISTREQUEST._serialized_start=46
  _GETMYCOMPANYLISTREQUEST._serialized_end=88
  _GETCOMPANYDETAILREQUEST._serialized_start=90
  _GETCOMPANYDETAILREQUEST._serialized_end=127
  _GETCOMPANYLISTREQUEST._serialized_start=129
  _GETCOMPANYLISTREQUEST._serialized_end=211
  _COMPANYLISTRESPONSE._serialized_start=213
  _COMPANYLISTRESPONSE._serialized_end=281
  _DELETECOMPANYREQUEST._serialized_start=283
  _DELETECOMPANYREQUEST._serialized_end=317
  _UPDATECOMPANYREQUEST._serialized_start=320
  _UPDATECOMPANYREQUEST._serialized_end=515
  _COMPANYRESPONSE._serialized_start=518
  _COMPANYRESPONSE._serialized_end=708
  _CREATECOMPANYREQUEST._serialized_start=711
  _CREATECOMPANYREQUEST._serialized_end=894
  _COMPANY._serialized_start=897
  _COMPANY._serialized_end=1288
# @@protoc_insertion_point(module_scope)
