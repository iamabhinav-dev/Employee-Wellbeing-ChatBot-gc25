# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: SOD.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'SOD.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tSOD.proto\x12\x04user\x1a\x1fgoogle/protobuf/timestamp.proto\"#\n\x12UpdateAtSODRequest\x12\r\n\x05\x65mpid\x18\x01 \x01(\t\"\xce\x01\n\x13UpdateAtSODResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x12\n\nstreakDays\x18\x03 \x01(\x05\x12\x1c\n\x14numberOfParticipants\x18\x04 \x01(\x05\x12\x19\n\x11\x63hatCheckInPoints\x18\x05 \x01(\x05\x12\x19\n\x11streakBonusPoints\x18\x06 \x01(\x05\x12-\n\ttimestamp\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp2Q\n\x0bUserService\x12\x42\n\x0bUpdateAtSOD\x12\x18.user.UpdateAtSODRequest\x1a\x19.user.UpdateAtSODResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'SOD_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_UPDATEATSODREQUEST']._serialized_start=52
  _globals['_UPDATEATSODREQUEST']._serialized_end=87
  _globals['_UPDATEATSODRESPONSE']._serialized_start=90
  _globals['_UPDATEATSODRESPONSE']._serialized_end=296
  _globals['_USERSERVICE']._serialized_start=298
  _globals['_USERSERVICE']._serialized_end=379
# @@protoc_insertion_point(module_scope)
