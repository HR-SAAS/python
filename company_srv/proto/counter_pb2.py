# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: counter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rcounter.proto\"\x1e\n\rCountResponse\x12\r\n\x05\x63ount\x18\x01 \x01(\x03\"v\n\x13\x43ountCompanyRequest\x12\x30\n\x06search\x18\x01 \x03(\x0b\x32 .CountCompanyRequest.SearchEntry\x1a-\n\x0bSearchEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"~\n\x17\x43ountCompanyUserRequest\x12\x34\n\x06search\x18\x01 \x03(\x0b\x32$.CountCompanyUserRequest.SearchEntry\x1a-\n\x0bSearchEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"|\n\x16\x43ountDepartmentRequest\x12\x33\n\x06search\x18\x01 \x03(\x0b\x32#.CountDepartmentRequest.SearchEntry\x1a-\n\x0bSearchEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x84\x01\n\x1a\x43ountDepartmentUserRequest\x12\x37\n\x06search\x18\x01 \x03(\x0b\x32\'.CountDepartmentUserRequest.SearchEntry\x1a-\n\x0bSearchEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\xfd\x01\n\x07\x43ounter\x12\x34\n\x0c\x43ountCompany\x12\x14.CountCompanyRequest\x1a\x0e.CountResponse\x12<\n\x10\x43ountCompanyUser\x12\x18.CountCompanyUserRequest\x1a\x0e.CountResponse\x12:\n\x0f\x43ountDepartment\x12\x17.CountDepartmentRequest\x1a\x0e.CountResponse\x12\x42\n\x13\x43ountDepartmentUser\x12\x1b.CountDepartmentUserRequest\x1a\x0e.CountResponseb\x06proto3')



_COUNTRESPONSE = DESCRIPTOR.message_types_by_name['CountResponse']
_COUNTCOMPANYREQUEST = DESCRIPTOR.message_types_by_name['CountCompanyRequest']
_COUNTCOMPANYREQUEST_SEARCHENTRY = _COUNTCOMPANYREQUEST.nested_types_by_name['SearchEntry']
_COUNTCOMPANYUSERREQUEST = DESCRIPTOR.message_types_by_name['CountCompanyUserRequest']
_COUNTCOMPANYUSERREQUEST_SEARCHENTRY = _COUNTCOMPANYUSERREQUEST.nested_types_by_name['SearchEntry']
_COUNTDEPARTMENTREQUEST = DESCRIPTOR.message_types_by_name['CountDepartmentRequest']
_COUNTDEPARTMENTREQUEST_SEARCHENTRY = _COUNTDEPARTMENTREQUEST.nested_types_by_name['SearchEntry']
_COUNTDEPARTMENTUSERREQUEST = DESCRIPTOR.message_types_by_name['CountDepartmentUserRequest']
_COUNTDEPARTMENTUSERREQUEST_SEARCHENTRY = _COUNTDEPARTMENTUSERREQUEST.nested_types_by_name['SearchEntry']
CountResponse = _reflection.GeneratedProtocolMessageType('CountResponse', (_message.Message,), {
  'DESCRIPTOR' : _COUNTRESPONSE,
  '__module__' : 'counter_pb2'
  # @@protoc_insertion_point(class_scope:CountResponse)
  })
_sym_db.RegisterMessage(CountResponse)

CountCompanyRequest = _reflection.GeneratedProtocolMessageType('CountCompanyRequest', (_message.Message,), {

  'SearchEntry' : _reflection.GeneratedProtocolMessageType('SearchEntry', (_message.Message,), {
    'DESCRIPTOR' : _COUNTCOMPANYREQUEST_SEARCHENTRY,
    '__module__' : 'counter_pb2'
    # @@protoc_insertion_point(class_scope:CountCompanyRequest.SearchEntry)
    })
  ,
  'DESCRIPTOR' : _COUNTCOMPANYREQUEST,
  '__module__' : 'counter_pb2'
  # @@protoc_insertion_point(class_scope:CountCompanyRequest)
  })
_sym_db.RegisterMessage(CountCompanyRequest)
_sym_db.RegisterMessage(CountCompanyRequest.SearchEntry)

CountCompanyUserRequest = _reflection.GeneratedProtocolMessageType('CountCompanyUserRequest', (_message.Message,), {

  'SearchEntry' : _reflection.GeneratedProtocolMessageType('SearchEntry', (_message.Message,), {
    'DESCRIPTOR' : _COUNTCOMPANYUSERREQUEST_SEARCHENTRY,
    '__module__' : 'counter_pb2'
    # @@protoc_insertion_point(class_scope:CountCompanyUserRequest.SearchEntry)
    })
  ,
  'DESCRIPTOR' : _COUNTCOMPANYUSERREQUEST,
  '__module__' : 'counter_pb2'
  # @@protoc_insertion_point(class_scope:CountCompanyUserRequest)
  })
_sym_db.RegisterMessage(CountCompanyUserRequest)
_sym_db.RegisterMessage(CountCompanyUserRequest.SearchEntry)

CountDepartmentRequest = _reflection.GeneratedProtocolMessageType('CountDepartmentRequest', (_message.Message,), {

  'SearchEntry' : _reflection.GeneratedProtocolMessageType('SearchEntry', (_message.Message,), {
    'DESCRIPTOR' : _COUNTDEPARTMENTREQUEST_SEARCHENTRY,
    '__module__' : 'counter_pb2'
    # @@protoc_insertion_point(class_scope:CountDepartmentRequest.SearchEntry)
    })
  ,
  'DESCRIPTOR' : _COUNTDEPARTMENTREQUEST,
  '__module__' : 'counter_pb2'
  # @@protoc_insertion_point(class_scope:CountDepartmentRequest)
  })
_sym_db.RegisterMessage(CountDepartmentRequest)
_sym_db.RegisterMessage(CountDepartmentRequest.SearchEntry)

CountDepartmentUserRequest = _reflection.GeneratedProtocolMessageType('CountDepartmentUserRequest', (_message.Message,), {

  'SearchEntry' : _reflection.GeneratedProtocolMessageType('SearchEntry', (_message.Message,), {
    'DESCRIPTOR' : _COUNTDEPARTMENTUSERREQUEST_SEARCHENTRY,
    '__module__' : 'counter_pb2'
    # @@protoc_insertion_point(class_scope:CountDepartmentUserRequest.SearchEntry)
    })
  ,
  'DESCRIPTOR' : _COUNTDEPARTMENTUSERREQUEST,
  '__module__' : 'counter_pb2'
  # @@protoc_insertion_point(class_scope:CountDepartmentUserRequest)
  })
_sym_db.RegisterMessage(CountDepartmentUserRequest)
_sym_db.RegisterMessage(CountDepartmentUserRequest.SearchEntry)

_COUNTER = DESCRIPTOR.services_by_name['Counter']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COUNTCOMPANYREQUEST_SEARCHENTRY._options = None
  _COUNTCOMPANYREQUEST_SEARCHENTRY._serialized_options = b'8\001'
  _COUNTCOMPANYUSERREQUEST_SEARCHENTRY._options = None
  _COUNTCOMPANYUSERREQUEST_SEARCHENTRY._serialized_options = b'8\001'
  _COUNTDEPARTMENTREQUEST_SEARCHENTRY._options = None
  _COUNTDEPARTMENTREQUEST_SEARCHENTRY._serialized_options = b'8\001'
  _COUNTDEPARTMENTUSERREQUEST_SEARCHENTRY._options = None
  _COUNTDEPARTMENTUSERREQUEST_SEARCHENTRY._serialized_options = b'8\001'
  _COUNTRESPONSE._serialized_start=17
  _COUNTRESPONSE._serialized_end=47
  _COUNTCOMPANYREQUEST._serialized_start=49
  _COUNTCOMPANYREQUEST._serialized_end=167
  _COUNTCOMPANYREQUEST_SEARCHENTRY._serialized_start=122
  _COUNTCOMPANYREQUEST_SEARCHENTRY._serialized_end=167
  _COUNTCOMPANYUSERREQUEST._serialized_start=169
  _COUNTCOMPANYUSERREQUEST._serialized_end=295
  _COUNTCOMPANYUSERREQUEST_SEARCHENTRY._serialized_start=122
  _COUNTCOMPANYUSERREQUEST_SEARCHENTRY._serialized_end=167
  _COUNTDEPARTMENTREQUEST._serialized_start=297
  _COUNTDEPARTMENTREQUEST._serialized_end=421
  _COUNTDEPARTMENTREQUEST_SEARCHENTRY._serialized_start=122
  _COUNTDEPARTMENTREQUEST_SEARCHENTRY._serialized_end=167
  _COUNTDEPARTMENTUSERREQUEST._serialized_start=424
  _COUNTDEPARTMENTUSERREQUEST._serialized_end=556
  _COUNTDEPARTMENTUSERREQUEST_SEARCHENTRY._serialized_start=122
  _COUNTDEPARTMENTUSERREQUEST_SEARCHENTRY._serialized_end=167
  _COUNTER._serialized_start=559
  _COUNTER._serialized_end=812
# @@protoc_insertion_point(module_scope)
