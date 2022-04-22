# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_post.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fuser_post.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\"&\n\x18GetUserPostDetailRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"[\n\x1a\x42\x61tchUpdateUserPostRequest\x12\n\n\x02id\x18\x01 \x03(\x03\x12\x0e\n\x06remark\x18\x02 \x01(\t\x12\x11\n\treview_id\x18\x03 \x01(\x03\x12\x0e\n\x06status\x18\x04 \x01(\x05\"\xf6\x01\n\x10UserPostResponse\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0f\n\x07post_id\x18\x02 \x01(\x03\x12\x0f\n\x07user_id\x18\x03 \x01(\x03\x12\x11\n\tresume_id\x18\x04 \x01(\x03\x12\x0e\n\x06resume\x18\x05 \x01(\t\x12\x0e\n\x06remark\x18\x06 \x01(\t\x12\x11\n\treview_id\x18\x07 \x01(\x03\x12\x0e\n\x06status\x18\x08 \x01(\x05\x12.\n\ncreated_at\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xf7\x01\n\x16GetUserPostListRequest\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\r\n\x05limit\x18\x03 \x01(\x05\x12/\n\x04sort\x18\x04 \x03(\x0b\x32!.GetUserPostListRequest.SortEntry\x12\x33\n\x06search\x18\x05 \x03(\x0b\x32#.GetUserPostListRequest.SearchEntry\x1a+\n\tSortEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a-\n\x0bSearchEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"F\n\x14UserPostListResponse\x12\x1f\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x11.UserPostResponse\x12\r\n\x05total\x18\x02 \x01(\x05\"\x8f\x01\n\x15\x43reateUserPostRequest\x12\x0f\n\x07post_id\x18\x02 \x01(\x03\x12\x0f\n\x07user_id\x18\x03 \x01(\x03\x12\x11\n\tresume_id\x18\x04 \x01(\x03\x12\x0e\n\x06resume\x18\x05 \x01(\t\x12\x0e\n\x06remark\x18\x06 \x01(\t\x12\x11\n\treview_id\x18\x07 \x01(\x03\x12\x0e\n\x06status\x18\x08 \x01(\x05\"\x9b\x01\n\x15UpdateUserPostRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0f\n\x07post_id\x18\x02 \x01(\x03\x12\x0f\n\x07user_id\x18\x03 \x01(\x03\x12\x11\n\tresume_id\x18\x04 \x01(\x03\x12\x0e\n\x06resume\x18\x05 \x01(\t\x12\x0e\n\x06remark\x18\x06 \x01(\t\x12\x11\n\treview_id\x18\x07 \x01(\x03\x12\x0e\n\x06status\x18\x08 \x01(\x05\"#\n\x15\x44\x65leteUserPostRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x32\x9d\x03\n\x08UserPost\x12\x41\n\x0fGetUserPostList\x12\x17.GetUserPostListRequest\x1a\x15.UserPostListResponse\x12;\n\x0e\x43reateUserPost\x12\x16.CreateUserPostRequest\x1a\x11.UserPostResponse\x12@\n\x0eUpdateUserPost\x12\x16.UpdateUserPostRequest\x1a\x16.google.protobuf.Empty\x12@\n\x0e\x44\x65leteUserPost\x12\x16.DeleteUserPostRequest\x1a\x16.google.protobuf.Empty\x12\x41\n\x11GetUserPostDetail\x12\x19.GetUserPostDetailRequest\x1a\x11.UserPostResponse\x12J\n\x13\x42\x61tchUpdateUserPost\x12\x1b.BatchUpdateUserPostRequest\x1a\x16.google.protobuf.EmptyB\nZ\x08../protob\x06proto3')



_GETUSERPOSTDETAILREQUEST = DESCRIPTOR.message_types_by_name['GetUserPostDetailRequest']
_BATCHUPDATEUSERPOSTREQUEST = DESCRIPTOR.message_types_by_name['BatchUpdateUserPostRequest']
_USERPOSTRESPONSE = DESCRIPTOR.message_types_by_name['UserPostResponse']
_GETUSERPOSTLISTREQUEST = DESCRIPTOR.message_types_by_name['GetUserPostListRequest']
_GETUSERPOSTLISTREQUEST_SORTENTRY = _GETUSERPOSTLISTREQUEST.nested_types_by_name['SortEntry']
_GETUSERPOSTLISTREQUEST_SEARCHENTRY = _GETUSERPOSTLISTREQUEST.nested_types_by_name['SearchEntry']
_USERPOSTLISTRESPONSE = DESCRIPTOR.message_types_by_name['UserPostListResponse']
_CREATEUSERPOSTREQUEST = DESCRIPTOR.message_types_by_name['CreateUserPostRequest']
_UPDATEUSERPOSTREQUEST = DESCRIPTOR.message_types_by_name['UpdateUserPostRequest']
_DELETEUSERPOSTREQUEST = DESCRIPTOR.message_types_by_name['DeleteUserPostRequest']
GetUserPostDetailRequest = _reflection.GeneratedProtocolMessageType('GetUserPostDetailRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERPOSTDETAILREQUEST,
  '__module__' : 'user_post_pb2'
  # @@protoc_insertion_point(class_scope:GetUserPostDetailRequest)
  })
_sym_db.RegisterMessage(GetUserPostDetailRequest)

BatchUpdateUserPostRequest = _reflection.GeneratedProtocolMessageType('BatchUpdateUserPostRequest', (_message.Message,), {
  'DESCRIPTOR' : _BATCHUPDATEUSERPOSTREQUEST,
  '__module__' : 'user_post_pb2'
  # @@protoc_insertion_point(class_scope:BatchUpdateUserPostRequest)
  })
_sym_db.RegisterMessage(BatchUpdateUserPostRequest)

UserPostResponse = _reflection.GeneratedProtocolMessageType('UserPostResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERPOSTRESPONSE,
  '__module__' : 'user_post_pb2'
  # @@protoc_insertion_point(class_scope:UserPostResponse)
  })
_sym_db.RegisterMessage(UserPostResponse)

GetUserPostListRequest = _reflection.GeneratedProtocolMessageType('GetUserPostListRequest', (_message.Message,), {

  'SortEntry' : _reflection.GeneratedProtocolMessageType('SortEntry', (_message.Message,), {
    'DESCRIPTOR' : _GETUSERPOSTLISTREQUEST_SORTENTRY,
    '__module__' : 'user_post_pb2'
    # @@protoc_insertion_point(class_scope:GetUserPostListRequest.SortEntry)
    })
  ,

  'SearchEntry' : _reflection.GeneratedProtocolMessageType('SearchEntry', (_message.Message,), {
    'DESCRIPTOR' : _GETUSERPOSTLISTREQUEST_SEARCHENTRY,
    '__module__' : 'user_post_pb2'
    # @@protoc_insertion_point(class_scope:GetUserPostListRequest.SearchEntry)
    })
  ,
  'DESCRIPTOR' : _GETUSERPOSTLISTREQUEST,
  '__module__' : 'user_post_pb2'
  # @@protoc_insertion_point(class_scope:GetUserPostListRequest)
  })
_sym_db.RegisterMessage(GetUserPostListRequest)
_sym_db.RegisterMessage(GetUserPostListRequest.SortEntry)
_sym_db.RegisterMessage(GetUserPostListRequest.SearchEntry)

UserPostListResponse = _reflection.GeneratedProtocolMessageType('UserPostListResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERPOSTLISTRESPONSE,
  '__module__' : 'user_post_pb2'
  # @@protoc_insertion_point(class_scope:UserPostListResponse)
  })
_sym_db.RegisterMessage(UserPostListResponse)

CreateUserPostRequest = _reflection.GeneratedProtocolMessageType('CreateUserPostRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERPOSTREQUEST,
  '__module__' : 'user_post_pb2'
  # @@protoc_insertion_point(class_scope:CreateUserPostRequest)
  })
_sym_db.RegisterMessage(CreateUserPostRequest)

UpdateUserPostRequest = _reflection.GeneratedProtocolMessageType('UpdateUserPostRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEUSERPOSTREQUEST,
  '__module__' : 'user_post_pb2'
  # @@protoc_insertion_point(class_scope:UpdateUserPostRequest)
  })
_sym_db.RegisterMessage(UpdateUserPostRequest)

DeleteUserPostRequest = _reflection.GeneratedProtocolMessageType('DeleteUserPostRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEUSERPOSTREQUEST,
  '__module__' : 'user_post_pb2'
  # @@protoc_insertion_point(class_scope:DeleteUserPostRequest)
  })
_sym_db.RegisterMessage(DeleteUserPostRequest)

_USERPOST = DESCRIPTOR.services_by_name['UserPost']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\010../proto'
  _GETUSERPOSTLISTREQUEST_SORTENTRY._options = None
  _GETUSERPOSTLISTREQUEST_SORTENTRY._serialized_options = b'8\001'
  _GETUSERPOSTLISTREQUEST_SEARCHENTRY._options = None
  _GETUSERPOSTLISTREQUEST_SEARCHENTRY._serialized_options = b'8\001'
  _GETUSERPOSTDETAILREQUEST._serialized_start=81
  _GETUSERPOSTDETAILREQUEST._serialized_end=119
  _BATCHUPDATEUSERPOSTREQUEST._serialized_start=121
  _BATCHUPDATEUSERPOSTREQUEST._serialized_end=212
  _USERPOSTRESPONSE._serialized_start=215
  _USERPOSTRESPONSE._serialized_end=461
  _GETUSERPOSTLISTREQUEST._serialized_start=464
  _GETUSERPOSTLISTREQUEST._serialized_end=711
  _GETUSERPOSTLISTREQUEST_SORTENTRY._serialized_start=621
  _GETUSERPOSTLISTREQUEST_SORTENTRY._serialized_end=664
  _GETUSERPOSTLISTREQUEST_SEARCHENTRY._serialized_start=666
  _GETUSERPOSTLISTREQUEST_SEARCHENTRY._serialized_end=711
  _USERPOSTLISTRESPONSE._serialized_start=713
  _USERPOSTLISTRESPONSE._serialized_end=783
  _CREATEUSERPOSTREQUEST._serialized_start=786
  _CREATEUSERPOSTREQUEST._serialized_end=929
  _UPDATEUSERPOSTREQUEST._serialized_start=932
  _UPDATEUSERPOSTREQUEST._serialized_end=1087
  _DELETEUSERPOSTREQUEST._serialized_start=1089
  _DELETEUSERPOSTREQUEST._serialized_end=1124
  _USERPOST._serialized_start=1127
  _USERPOST._serialized_end=1540
# @@protoc_insertion_point(module_scope)
