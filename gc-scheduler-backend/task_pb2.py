# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: task.proto
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
    'task.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntask.proto\x12\tscheduler\"b\n\x0bMeetRequest\x12\r\n\x05\x65mpid\x18\x01 \x01(\t\x12\x0f\n\x07\x65mailID\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x0f\n\x07\x65mpName\x18\x04 \x01(\t\x12\x11\n\ttimestamp\x18\x05 \x01(\x03\"/\n\x0cMeetResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0e\n\x06job_id\x18\x02 \x01(\t2N\n\tScheduler\x12\x41\n\x0cScheduleMeet\x12\x16.scheduler.MeetRequest\x1a\x17.scheduler.MeetResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'task_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MEETREQUEST']._serialized_start=25
  _globals['_MEETREQUEST']._serialized_end=123
  _globals['_MEETRESPONSE']._serialized_start=125
  _globals['_MEETRESPONSE']._serialized_end=172
  _globals['_SCHEDULER']._serialized_start=174
  _globals['_SCHEDULER']._serialized_end=252
# @@protoc_insertion_point(module_scope)
