# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: login.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0blogin.proto\x12\x0cloginPackage\"5\n\x0cLoginRequest\x12%\n\x04\x66orm\x18\x01 \x01(\x0b\x32\x17.loginPackage.LoginForm\";\n\x0bReservation\x12\r\n\x05movie\x18\x01 \x01(\t\x12\x0f\n\x07theatre\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\t\"\x7f\n\rLoginResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12/\n\x0creservations\x18\x05 \x03(\x0b\x32\x19.loginPackage.Reservation\",\n\tLoginForm\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t2P\n\x0cLoginService\x12@\n\x05Login\x12\x1a.loginPackage.LoginRequest\x1a\x1b.loginPackage.LoginResponseb\x06proto3')



_LOGINREQUEST = DESCRIPTOR.message_types_by_name['LoginRequest']
_RESERVATION = DESCRIPTOR.message_types_by_name['Reservation']
_LOGINRESPONSE = DESCRIPTOR.message_types_by_name['LoginResponse']
_LOGINFORM = DESCRIPTOR.message_types_by_name['LoginForm']
LoginRequest = _reflection.GeneratedProtocolMessageType('LoginRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREQUEST,
  '__module__' : 'login_pb2'
  # @@protoc_insertion_point(class_scope:loginPackage.LoginRequest)
  })
_sym_db.RegisterMessage(LoginRequest)

Reservation = _reflection.GeneratedProtocolMessageType('Reservation', (_message.Message,), {
  'DESCRIPTOR' : _RESERVATION,
  '__module__' : 'login_pb2'
  # @@protoc_insertion_point(class_scope:loginPackage.Reservation)
  })
_sym_db.RegisterMessage(Reservation)

LoginResponse = _reflection.GeneratedProtocolMessageType('LoginResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGINRESPONSE,
  '__module__' : 'login_pb2'
  # @@protoc_insertion_point(class_scope:loginPackage.LoginResponse)
  })
_sym_db.RegisterMessage(LoginResponse)

LoginForm = _reflection.GeneratedProtocolMessageType('LoginForm', (_message.Message,), {
  'DESCRIPTOR' : _LOGINFORM,
  '__module__' : 'login_pb2'
  # @@protoc_insertion_point(class_scope:loginPackage.LoginForm)
  })
_sym_db.RegisterMessage(LoginForm)

_LOGINSERVICE = DESCRIPTOR.services_by_name['LoginService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOGINREQUEST._serialized_start=29
  _LOGINREQUEST._serialized_end=82
  _RESERVATION._serialized_start=84
  _RESERVATION._serialized_end=143
  _LOGINRESPONSE._serialized_start=145
  _LOGINRESPONSE._serialized_end=272
  _LOGINFORM._serialized_start=274
  _LOGINFORM._serialized_end=318
  _LOGINSERVICE._serialized_start=320
  _LOGINSERVICE._serialized_end=400
# @@protoc_insertion_point(module_scope)