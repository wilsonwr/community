# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: beacon.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='beacon.proto',
  package='beacon',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x62\x65\x61\x63on.proto\x12\x06\x62\x65\x61\x63on\" \n\x0e\x42\x65\x61\x63onIncoming\x12\x0e\n\x06\x42\x65\x61\x63on\x18\x01 \x01(\t\" \n\x0e\x42\x65\x61\x63onOutgoing\x12\x0e\n\x06\x42\x65\x61\x63on\x18\x01 \x01(\t2D\n\x06\x42\x65\x61\x63on\x12:\n\x06Handle\x12\x16.beacon.BeaconIncoming\x1a\x16.beacon.BeaconOutgoing\"\x00\x62\x06proto3'
)




_BEACONINCOMING = _descriptor.Descriptor(
  name='BeaconIncoming',
  full_name='beacon.BeaconIncoming',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Beacon', full_name='beacon.BeaconIncoming.Beacon', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=24,
  serialized_end=56,
)


_BEACONOUTGOING = _descriptor.Descriptor(
  name='BeaconOutgoing',
  full_name='beacon.BeaconOutgoing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Beacon', full_name='beacon.BeaconOutgoing.Beacon', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=58,
  serialized_end=90,
)

DESCRIPTOR.message_types_by_name['BeaconIncoming'] = _BEACONINCOMING
DESCRIPTOR.message_types_by_name['BeaconOutgoing'] = _BEACONOUTGOING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BeaconIncoming = _reflection.GeneratedProtocolMessageType('BeaconIncoming', (_message.Message,), {
  'DESCRIPTOR' : _BEACONINCOMING,
  '__module__' : 'beacon_pb2'
  # @@protoc_insertion_point(class_scope:beacon.BeaconIncoming)
  })
_sym_db.RegisterMessage(BeaconIncoming)

BeaconOutgoing = _reflection.GeneratedProtocolMessageType('BeaconOutgoing', (_message.Message,), {
  'DESCRIPTOR' : _BEACONOUTGOING,
  '__module__' : 'beacon_pb2'
  # @@protoc_insertion_point(class_scope:beacon.BeaconOutgoing)
  })
_sym_db.RegisterMessage(BeaconOutgoing)



_BEACON = _descriptor.ServiceDescriptor(
  name='Beacon',
  full_name='beacon.Beacon',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=92,
  serialized_end=160,
  methods=[
  _descriptor.MethodDescriptor(
    name='Handle',
    full_name='beacon.Beacon.Handle',
    index=0,
    containing_service=None,
    input_type=_BEACONINCOMING,
    output_type=_BEACONOUTGOING,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BEACON)

DESCRIPTOR.services_by_name['Beacon'] = _BEACON

# @@protoc_insertion_point(module_scope)
