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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rcounter.proto\"\x9f\x01\n\x17\x43ountUserMessageRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x34\n\x06search\x18\x02 \x03(\x0b\x32$.CountUserMessageRequest.SearchEntry\x12\x0e\n\x06status\x18\x03 \x01(\x05\x1a-\n\x0bSearchEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\")\n\x18\x43ountUserMessageResponse\x12\r\n\x05\x63ount\x18\x01 \x01(\x03\x32_\n\x14ResumeCounterService\x12G\n\x10\x43ountUserMessage\x12\x18.CountUserMessageRequest\x1a\x19.CountUserMessageResponseB\nZ\x08../protob\x06proto3')



_COUNTUSERMESSAGEREQUEST = DESCRIPTOR.message_types_by_name['CountUserMessageRequest']
_COUNTUSERMESSAGEREQUEST_SEARCHENTRY = _COUNTUSERMESSAGEREQUEST.nested_types_by_name['SearchEntry']
_COUNTUSERMESSAGERESPONSE = DESCRIPTOR.message_types_by_name['CountUserMessageResponse']
CountUserMessageRequest = _reflection.GeneratedProtocolMessageType('CountUserMessageRequest', (_message.Message,), {

  'SearchEntry' : _reflection.GeneratedProtocolMessageType('SearchEntry', (_message.Message,), {
    'DESCRIPTOR' : _COUNTUSERMESSAGEREQUEST_SEARCHENTRY,
    '__module__' : 'counter_pb2'
    # @@protoc_insertion_point(class_scope:CountUserMessageRequest.SearchEntry)
    })
  ,
  'DESCRIPTOR' : _COUNTUSERMESSAGEREQUEST,
  '__module__' : 'counter_pb2'
  # @@protoc_insertion_point(class_scope:CountUserMessageRequest)
  })
_sym_db.RegisterMessage(CountUserMessageRequest)
_sym_db.RegisterMessage(CountUserMessageRequest.SearchEntry)

CountUserMessageResponse = _reflection.GeneratedProtocolMessageType('CountUserMessageResponse', (_message.Message,), {
  'DESCRIPTOR' : _COUNTUSERMESSAGERESPONSE,
  '__module__' : 'counter_pb2'
  # @@protoc_insertion_point(class_scope:CountUserMessageResponse)
  })
_sym_db.RegisterMessage(CountUserMessageResponse)

_RESUMECOUNTERSERVICE = DESCRIPTOR.services_by_name['ResumeCounterService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\010../proto'
  _COUNTUSERMESSAGEREQUEST_SEARCHENTRY._options = None
  _COUNTUSERMESSAGEREQUEST_SEARCHENTRY._serialized_options = b'8\001'
  _COUNTUSERMESSAGEREQUEST._serialized_start=18
  _COUNTUSERMESSAGEREQUEST._serialized_end=177
  _COUNTUSERMESSAGEREQUEST_SEARCHENTRY._serialized_start=132
  _COUNTUSERMESSAGEREQUEST_SEARCHENTRY._serialized_end=177
  _COUNTUSERMESSAGERESPONSE._serialized_start=179
  _COUNTUSERMESSAGERESPONSE._serialized_end=220
  _RESUMECOUNTERSERVICE._serialized_start=222
  _RESUMECOUNTERSERVICE._serialized_end=317
# @@protoc_insertion_point(module_scope)
