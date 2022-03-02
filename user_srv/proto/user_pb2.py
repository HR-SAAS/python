# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x1a\x1bgoogle/protobuf/empty.proto\"\'\n\x08PageInfo\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05\"\x17\n\tIdRequest\x12\n\n\x02id\x18\x01 \x01(\x03\">\n\x10UserListResponse\x12\x1b\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\r.UserResponse\x12\r\n\x05total\x18\x02 \x01(\x05\"\x1f\n\rMobileRequest\x12\x0e\n\x06mobile\x18\x01 \x01(\t\"\\\n\x0bUserRequest\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06mobile\x18\x03 \x01(\t\x12\x10\n\x08nickName\x18\x04 \x01(\t\x12\x10\n\x08password\x18\x05 \x01(\t\x12\x0b\n\x03sex\x18\x06 \x01(\x05\"n\n\x11UpdateUserRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06mobile\x18\x03 \x01(\t\x12\x10\n\x08nickName\x18\x04 \x01(\t\x12\x10\n\x08password\x18\x05 \x01(\t\x12\x0b\n\x03sex\x18\x06 \x01(\x05\"i\n\x0cUserResponse\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06mobile\x18\x03 \x01(\t\x12\x10\n\x08nickName\x18\x04 \x01(\t\x12\x10\n\x08password\x18\x05 \x01(\t\x12\x0b\n\x03sex\x18\x06 \x01(\x05\x32\xac\x02\n\x04User\x12+\n\x0bGetUserList\x12\t.PageInfo\x1a\x11.UserListResponse\x12\x31\n\x10\x46indUserByMobile\x12\x0e.MobileRequest\x1a\r.UserResponse\x12)\n\x0c\x46indUserById\x12\n.IdRequest\x1a\r.UserResponse\x12)\n\nCreateUser\x12\x0c.UserRequest\x1a\r.UserResponse\x12\x38\n\nUpdateUser\x12\x12.UpdateUserRequest\x1a\x16.google.protobuf.Empty\x12\x34\n\x0e\x44\x65leteUserById\x12\n.IdRequest\x1a\x16.google.protobuf.EmptyB\tZ\x07.;protob\x06proto3')



_PAGEINFO = DESCRIPTOR.message_types_by_name['PageInfo']
_IDREQUEST = DESCRIPTOR.message_types_by_name['IdRequest']
_USERLISTRESPONSE = DESCRIPTOR.message_types_by_name['UserListResponse']
_MOBILEREQUEST = DESCRIPTOR.message_types_by_name['MobileRequest']
_USERREQUEST = DESCRIPTOR.message_types_by_name['UserRequest']
_UPDATEUSERREQUEST = DESCRIPTOR.message_types_by_name['UpdateUserRequest']
_USERRESPONSE = DESCRIPTOR.message_types_by_name['UserResponse']
PageInfo = _reflection.GeneratedProtocolMessageType('PageInfo', (_message.Message,), {
  'DESCRIPTOR' : _PAGEINFO,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:PageInfo)
  })
_sym_db.RegisterMessage(PageInfo)

IdRequest = _reflection.GeneratedProtocolMessageType('IdRequest', (_message.Message,), {
  'DESCRIPTOR' : _IDREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:IdRequest)
  })
_sym_db.RegisterMessage(IdRequest)

UserListResponse = _reflection.GeneratedProtocolMessageType('UserListResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERLISTRESPONSE,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:UserListResponse)
  })
_sym_db.RegisterMessage(UserListResponse)

MobileRequest = _reflection.GeneratedProtocolMessageType('MobileRequest', (_message.Message,), {
  'DESCRIPTOR' : _MOBILEREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:MobileRequest)
  })
_sym_db.RegisterMessage(MobileRequest)

UserRequest = _reflection.GeneratedProtocolMessageType('UserRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:UserRequest)
  })
_sym_db.RegisterMessage(UserRequest)

UpdateUserRequest = _reflection.GeneratedProtocolMessageType('UpdateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEUSERREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:UpdateUserRequest)
  })
_sym_db.RegisterMessage(UpdateUserRequest)

UserResponse = _reflection.GeneratedProtocolMessageType('UserResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERRESPONSE,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:UserResponse)
  })
_sym_db.RegisterMessage(UserResponse)

_USER = DESCRIPTOR.services_by_name['User']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\007.;proto'
  _PAGEINFO._serialized_start=43
  _PAGEINFO._serialized_end=82
  _IDREQUEST._serialized_start=84
  _IDREQUEST._serialized_end=107
  _USERLISTRESPONSE._serialized_start=109
  _USERLISTRESPONSE._serialized_end=171
  _MOBILEREQUEST._serialized_start=173
  _MOBILEREQUEST._serialized_end=204
  _USERREQUEST._serialized_start=206
  _USERREQUEST._serialized_end=298
  _UPDATEUSERREQUEST._serialized_start=300
  _UPDATEUSERREQUEST._serialized_end=410
  _USERRESPONSE._serialized_start=412
  _USERRESPONSE._serialized_end=517
  _USER._serialized_start=520
  _USER._serialized_end=820
# @@protoc_insertion_point(module_scope)
