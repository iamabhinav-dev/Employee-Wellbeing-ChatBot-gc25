# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: teamMessages.proto
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
    'teamMessages.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12teamMessages.proto\x12\x0cteammessages\"H\n\x19UpdateTeamMessagesRequest\x12\r\n\x05\x65mpid\x18\x01 \x01(\t\x12\x1c\n\x14numberOfteamMessages\x18\x02 \x01(\x05\">\n\x1aUpdateTeamMessagesResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2v\n\x0bUserService\x12g\n\x12UpdateTeamMessages\x12\'.teammessages.UpdateTeamMessagesRequest\x1a(.teammessages.UpdateTeamMessagesResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'teamMessages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_UPDATETEAMMESSAGESREQUEST']._serialized_start=36
  _globals['_UPDATETEAMMESSAGESREQUEST']._serialized_end=108
  _globals['_UPDATETEAMMESSAGESRESPONSE']._serialized_start=110
  _globals['_UPDATETEAMMESSAGESRESPONSE']._serialized_end=172
  _globals['_USERSERVICE']._serialized_start=174
  _globals['_USERSERVICE']._serialized_end=292
# @@protoc_insertion_point(module_scope)
