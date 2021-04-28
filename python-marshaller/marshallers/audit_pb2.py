# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: audit.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import location_proof_pb2 as location__proof__pb2
from . import ledger_pb2 as ledger__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='audit.proto',
  package='pt.ulisboa.tecnico.surethingcore',
  syntax='proto3',
  serialized_options=b'\n&pt.ulisboa.tecnico.surethingcore.auditB\026SureThingAuditEntitiesP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0b\x61udit.proto\x12 pt.ulisboa.tecnico.surethingcore\x1a\x14location-proof.proto\x1a\x0cledger.proto\"\xfd\x01\n\x10\x41uditResultProto\x12V\n\x12merkleTreeElements\x18\x01 \x03(\x0b\x32:.pt.ulisboa.tecnico.surethingcore.SignedLocationProofProto\x12M\n\tauditPath\x18\x02 \x03(\x0b\x32:.pt.ulisboa.tecnico.surethingcore.SignedLocationProofProto\x12\x42\n\x03STH\x18\x03 \x01(\x0b\x32\x35.pt.ulisboa.tecnico.surethingcore.SignedTreeHeadProto\"\x92\x02\n\x1b\x43onsistencyProofResultProto\x12V\n\x12merkleTreeElements\x18\x01 \x03(\x0b\x32:.pt.ulisboa.tecnico.surethingcore.SignedLocationProofProto\x12W\n\x13\x63onsistencyProofLPs\x18\x02 \x03(\x0b\x32:.pt.ulisboa.tecnico.surethingcore.SignedLocationProofProto\x12\x42\n\x03STH\x18\x03 \x01(\x0b\x32\x35.pt.ulisboa.tecnico.surethingcore.SignedTreeHeadProto\"{\n\tSLPTProto\x12\r\n\x05logId\x18\x01 \x01(\x07\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12L\n\x08signedLP\x18\x03 \x01(\x0b\x32:.pt.ulisboa.tecnico.surethingcore.SignedLocationProofProto\"S\n\x12UserSureThingProto\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\r\n\x05token\x18\x04 \x01(\tBB\n&pt.ulisboa.tecnico.surethingcore.auditB\x16SureThingAuditEntitiesP\x01\x62\x06proto3'
  ,
  dependencies=[location__proof__pb2.DESCRIPTOR,ledger__pb2.DESCRIPTOR,])




_AUDITRESULTPROTO = _descriptor.Descriptor(
  name='AuditResultProto',
  full_name='pt.ulisboa.tecnico.surethingcore.AuditResultProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='merkleTreeElements', full_name='pt.ulisboa.tecnico.surethingcore.AuditResultProto.merkleTreeElements', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='auditPath', full_name='pt.ulisboa.tecnico.surethingcore.AuditResultProto.auditPath', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='STH', full_name='pt.ulisboa.tecnico.surethingcore.AuditResultProto.STH', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=339,
)


_CONSISTENCYPROOFRESULTPROTO = _descriptor.Descriptor(
  name='ConsistencyProofResultProto',
  full_name='pt.ulisboa.tecnico.surethingcore.ConsistencyProofResultProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='merkleTreeElements', full_name='pt.ulisboa.tecnico.surethingcore.ConsistencyProofResultProto.merkleTreeElements', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='consistencyProofLPs', full_name='pt.ulisboa.tecnico.surethingcore.ConsistencyProofResultProto.consistencyProofLPs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='STH', full_name='pt.ulisboa.tecnico.surethingcore.ConsistencyProofResultProto.STH', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=342,
  serialized_end=616,
)


_SLPTPROTO = _descriptor.Descriptor(
  name='SLPTProto',
  full_name='pt.ulisboa.tecnico.surethingcore.SLPTProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='logId', full_name='pt.ulisboa.tecnico.surethingcore.SLPTProto.logId', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='pt.ulisboa.tecnico.surethingcore.SLPTProto.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signedLP', full_name='pt.ulisboa.tecnico.surethingcore.SLPTProto.signedLP', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=618,
  serialized_end=741,
)


_USERSURETHINGPROTO = _descriptor.Descriptor(
  name='UserSureThingProto',
  full_name='pt.ulisboa.tecnico.surethingcore.UserSureThingProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pt.ulisboa.tecnico.surethingcore.UserSureThingProto.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='username', full_name='pt.ulisboa.tecnico.surethingcore.UserSureThingProto.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='pt.ulisboa.tecnico.surethingcore.UserSureThingProto.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='pt.ulisboa.tecnico.surethingcore.UserSureThingProto.token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=743,
  serialized_end=826,
)

_AUDITRESULTPROTO.fields_by_name['merkleTreeElements'].message_type = location__proof__pb2._SIGNEDLOCATIONPROOFPROTO
_AUDITRESULTPROTO.fields_by_name['auditPath'].message_type = location__proof__pb2._SIGNEDLOCATIONPROOFPROTO
_AUDITRESULTPROTO.fields_by_name['STH'].message_type = ledger__pb2._SIGNEDTREEHEADPROTO
_CONSISTENCYPROOFRESULTPROTO.fields_by_name['merkleTreeElements'].message_type = location__proof__pb2._SIGNEDLOCATIONPROOFPROTO
_CONSISTENCYPROOFRESULTPROTO.fields_by_name['consistencyProofLPs'].message_type = location__proof__pb2._SIGNEDLOCATIONPROOFPROTO
_CONSISTENCYPROOFRESULTPROTO.fields_by_name['STH'].message_type = ledger__pb2._SIGNEDTREEHEADPROTO
_SLPTPROTO.fields_by_name['signedLP'].message_type = location__proof__pb2._SIGNEDLOCATIONPROOFPROTO
DESCRIPTOR.message_types_by_name['AuditResultProto'] = _AUDITRESULTPROTO
DESCRIPTOR.message_types_by_name['ConsistencyProofResultProto'] = _CONSISTENCYPROOFRESULTPROTO
DESCRIPTOR.message_types_by_name['SLPTProto'] = _SLPTPROTO
DESCRIPTOR.message_types_by_name['UserSureThingProto'] = _USERSURETHINGPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuditResultProto = _reflection.GeneratedProtocolMessageType('AuditResultProto', (_message.Message,), {
  'DESCRIPTOR' : _AUDITRESULTPROTO,
  '__module__' : 'audit_pb2'
  # @@protoc_insertion_point(class_scope:pt.ulisboa.tecnico.surethingcore.AuditResultProto)
  })
_sym_db.RegisterMessage(AuditResultProto)

ConsistencyProofResultProto = _reflection.GeneratedProtocolMessageType('ConsistencyProofResultProto', (_message.Message,), {
  'DESCRIPTOR' : _CONSISTENCYPROOFRESULTPROTO,
  '__module__' : 'audit_pb2'
  # @@protoc_insertion_point(class_scope:pt.ulisboa.tecnico.surethingcore.ConsistencyProofResultProto)
  })
_sym_db.RegisterMessage(ConsistencyProofResultProto)

SLPTProto = _reflection.GeneratedProtocolMessageType('SLPTProto', (_message.Message,), {
  'DESCRIPTOR' : _SLPTPROTO,
  '__module__' : 'audit_pb2'
  # @@protoc_insertion_point(class_scope:pt.ulisboa.tecnico.surethingcore.SLPTProto)
  })
_sym_db.RegisterMessage(SLPTProto)

UserSureThingProto = _reflection.GeneratedProtocolMessageType('UserSureThingProto', (_message.Message,), {
  'DESCRIPTOR' : _USERSURETHINGPROTO,
  '__module__' : 'audit_pb2'
  # @@protoc_insertion_point(class_scope:pt.ulisboa.tecnico.surethingcore.UserSureThingProto)
  })
_sym_db.RegisterMessage(UserSureThingProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
