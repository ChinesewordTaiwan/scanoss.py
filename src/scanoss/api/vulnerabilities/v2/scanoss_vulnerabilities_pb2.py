# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scanoss/api/vulnerabilities/v2/scanoss-vulnerabilities.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from scanoss.api.common.v2 import scanoss_common_pb2 as scanoss_dot_api_dot_common_dot_v2_dot_scanoss__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='scanoss/api/vulnerabilities/v2/scanoss-vulnerabilities.proto',
  package='scanoss.api.vulnerabilities.v2',
  syntax='proto3',
  serialized_options=b'Z?github.com/scanoss/papi/api/vulnerabilitiesv2;vulnerabilitiesv2',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n<scanoss/api/vulnerabilities/v2/scanoss-vulnerabilities.proto\x12\x1escanoss.api.vulnerabilities.v2\x1a*scanoss/api/common/v2/scanoss-common.proto\"\x8d\x01\n\x14VulnerabilityRequest\x12I\n\x05purls\x18\x01 \x03(\x0b\x32:.scanoss.api.vulnerabilities.v2.VulnerabilityRequest.Purls\x1a*\n\x05Purls\x12\x0c\n\x04purl\x18\x01 \x01(\t\x12\x13\n\x0brequirement\x18\x02 \x01(\t\"\xab\x01\n\x0b\x43peResponse\x12@\n\x05purls\x18\x01 \x03(\x0b\x32\x31.scanoss.api.vulnerabilities.v2.CpeResponse.Purls\x12\x35\n\x06status\x18\x02 \x01(\x0b\x32%.scanoss.api.common.v2.StatusResponse\x1a#\n\x05Purls\x12\x0c\n\x04purl\x18\x01 \x01(\t\x12\x0c\n\x04\x63pes\x18\x02 \x03(\t\"\xa3\x03\n\x15VulnerabilityResponse\x12J\n\x05purls\x18\x01 \x03(\x0b\x32;.scanoss.api.vulnerabilities.v2.VulnerabilityResponse.Purls\x12\x35\n\x06status\x18\x02 \x01(\x0b\x32%.scanoss.api.common.v2.StatusResponse\x1a\x8f\x01\n\x0fVulnerabilities\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03\x63ve\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x0f\n\x07summary\x18\x04 \x01(\t\x12\x10\n\x08severity\x18\x05 \x01(\t\x12\x11\n\tpublished\x18\x06 \x01(\t\x12\x10\n\x08modified\x18\x07 \x01(\t\x12\x0e\n\x06source\x18\x08 \x01(\t\x1au\n\x05Purls\x12\x0c\n\x04purl\x18\x01 \x01(\t\x12^\n\x0fvulnerabilities\x18\x02 \x03(\x0b\x32\x45.scanoss.api.vulnerabilities.v2.VulnerabilityResponse.Vulnerabilities2\xd4\x02\n\x0fVulnerabilities\x12O\n\x04\x45\x63ho\x12\".scanoss.api.common.v2.EchoRequest\x1a#.scanoss.api.common.v2.EchoResponse\x12l\n\x07GetCpes\x12\x34.scanoss.api.vulnerabilities.v2.VulnerabilityRequest\x1a+.scanoss.api.vulnerabilities.v2.CpeResponse\x12\x81\x01\n\x12GetVulnerabilities\x12\x34.scanoss.api.vulnerabilities.v2.VulnerabilityRequest\x1a\x35.scanoss.api.vulnerabilities.v2.VulnerabilityResponseBAZ?github.com/scanoss/papi/api/vulnerabilitiesv2;vulnerabilitiesv2b\x06proto3'
  ,
  dependencies=[scanoss_dot_api_dot_common_dot_v2_dot_scanoss__common__pb2.DESCRIPTOR,])




_VULNERABILITYREQUEST_PURLS = _descriptor.Descriptor(
  name='Purls',
  full_name='scanoss.api.vulnerabilities.v2.VulnerabilityRequest.Purls',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='purl', full_name='scanoss.api.vulnerabilities.v2.VulnerabilityRequest.Purls.purl', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='requirement', full_name='scanoss.api.vulnerabilities.v2.VulnerabilityRequest.Purls.requirement', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=240,
  serialized_end=282,
)

_VULNERABILITYREQUEST = _descriptor.Descriptor(
  name='VulnerabilityRequest',
  full_name='scanoss.api.vulnerabilities.v2.VulnerabilityRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='purls', full_name='scanoss.api.vulnerabilities.v2.VulnerabilityRequest.purls', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_VULNERABILITYREQUEST_PURLS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=282,
)


_CPERESPONSE_PURLS = _descriptor.Descriptor(
  name='Purls',
  full_name='scanoss.api.vulnerabilities.v2.CpeResponse.Purls',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='purl', full_name='scanoss.api.vulnerabilities.v2.CpeResponse.Purls.purl', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cpes', full_name='scanoss.api.vulnerabilities.v2.CpeResponse.Purls.cpes', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=421,
  serialized_end=456,
)

_CPERESPONSE = _descriptor.Descriptor(
  name='CpeResponse',
  full_name='scanoss.api.vulnerabilities.v2.CpeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='purls', full_name='scanoss.api.vulnerabilities.v2.CpeResponse.purls', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='scanoss.api.vulnerabilities.v2.CpeResponse.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CPERESPONSE_PURLS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=285,
  serialized_end=456,
)


_VULNERABILITYRESPONSE_VULNERABILITIES = _descriptor.Descriptor(
  name='Vulnerabilities',
  full_name='scanoss.api.vulnerabilities.v2.VulnerabilityResponse.Vulnerabilities',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='scanoss.api.vulnerabilities.v2.VulnerabilityResponse.Vulnerabilities.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cve', full_name='scanoss.api.vulnerabilities.v2.VulnerabilityResponse.Vulnerabilities.cve', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url', full_name='scanoss.api.vulnerabilities.v2.VulnerabilityResponse.Vulnerabilities.url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='summary', full_name='scanoss.api.vulnerabilities.v2.VulnerabilityResponse.Vulnerabilities.summary', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='severity', full_name='scanoss.api.vulnerabilities.v2.VulnerabilityResponse.Vulnerabilities.severity', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='published', full_name='scanoss.api.vulnerabilities.v2.VulnerabilityResponse.Vulnerabilities.published', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='modified', full_name='scanoss.api.vulnerabilities.v2.VulnerabilityResponse.Vulnerabilities.modified', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='scanoss.api.vulnerabilities.v2.VulnerabilityResponse.Vulnerabilities.source', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=616,
  serialized_end=759,
)

_VULNERABILITYRESPONSE_PURLS = _descriptor.Descriptor(
  name='Purls',
  full_name='scanoss.api.vulnerabilities.v2.VulnerabilityResponse.Purls',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='purl', full_name='scanoss.api.vulnerabilities.v2.VulnerabilityResponse.Purls.purl', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vulnerabilities', full_name='scanoss.api.vulnerabilities.v2.VulnerabilityResponse.Purls.vulnerabilities', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=761,
  serialized_end=878,
)

_VULNERABILITYRESPONSE = _descriptor.Descriptor(
  name='VulnerabilityResponse',
  full_name='scanoss.api.vulnerabilities.v2.VulnerabilityResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='purls', full_name='scanoss.api.vulnerabilities.v2.VulnerabilityResponse.purls', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='scanoss.api.vulnerabilities.v2.VulnerabilityResponse.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_VULNERABILITYRESPONSE_VULNERABILITIES, _VULNERABILITYRESPONSE_PURLS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=459,
  serialized_end=878,
)

_VULNERABILITYREQUEST_PURLS.containing_type = _VULNERABILITYREQUEST
_VULNERABILITYREQUEST.fields_by_name['purls'].message_type = _VULNERABILITYREQUEST_PURLS
_CPERESPONSE_PURLS.containing_type = _CPERESPONSE
_CPERESPONSE.fields_by_name['purls'].message_type = _CPERESPONSE_PURLS
_CPERESPONSE.fields_by_name['status'].message_type = scanoss_dot_api_dot_common_dot_v2_dot_scanoss__common__pb2._STATUSRESPONSE
_VULNERABILITYRESPONSE_VULNERABILITIES.containing_type = _VULNERABILITYRESPONSE
_VULNERABILITYRESPONSE_PURLS.fields_by_name['vulnerabilities'].message_type = _VULNERABILITYRESPONSE_VULNERABILITIES
_VULNERABILITYRESPONSE_PURLS.containing_type = _VULNERABILITYRESPONSE
_VULNERABILITYRESPONSE.fields_by_name['purls'].message_type = _VULNERABILITYRESPONSE_PURLS
_VULNERABILITYRESPONSE.fields_by_name['status'].message_type = scanoss_dot_api_dot_common_dot_v2_dot_scanoss__common__pb2._STATUSRESPONSE
DESCRIPTOR.message_types_by_name['VulnerabilityRequest'] = _VULNERABILITYREQUEST
DESCRIPTOR.message_types_by_name['CpeResponse'] = _CPERESPONSE
DESCRIPTOR.message_types_by_name['VulnerabilityResponse'] = _VULNERABILITYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VulnerabilityRequest = _reflection.GeneratedProtocolMessageType('VulnerabilityRequest', (_message.Message,), {

  'Purls' : _reflection.GeneratedProtocolMessageType('Purls', (_message.Message,), {
    'DESCRIPTOR' : _VULNERABILITYREQUEST_PURLS,
    '__module__' : 'scanoss.api.vulnerabilities.v2.scanoss_vulnerabilities_pb2'
    # @@protoc_insertion_point(class_scope:scanoss.api.vulnerabilities.v2.VulnerabilityRequest.Purls)
    })
  ,
  'DESCRIPTOR' : _VULNERABILITYREQUEST,
  '__module__' : 'scanoss.api.vulnerabilities.v2.scanoss_vulnerabilities_pb2'
  # @@protoc_insertion_point(class_scope:scanoss.api.vulnerabilities.v2.VulnerabilityRequest)
  })
_sym_db.RegisterMessage(VulnerabilityRequest)
_sym_db.RegisterMessage(VulnerabilityRequest.Purls)

CpeResponse = _reflection.GeneratedProtocolMessageType('CpeResponse', (_message.Message,), {

  'Purls' : _reflection.GeneratedProtocolMessageType('Purls', (_message.Message,), {
    'DESCRIPTOR' : _CPERESPONSE_PURLS,
    '__module__' : 'scanoss.api.vulnerabilities.v2.scanoss_vulnerabilities_pb2'
    # @@protoc_insertion_point(class_scope:scanoss.api.vulnerabilities.v2.CpeResponse.Purls)
    })
  ,
  'DESCRIPTOR' : _CPERESPONSE,
  '__module__' : 'scanoss.api.vulnerabilities.v2.scanoss_vulnerabilities_pb2'
  # @@protoc_insertion_point(class_scope:scanoss.api.vulnerabilities.v2.CpeResponse)
  })
_sym_db.RegisterMessage(CpeResponse)
_sym_db.RegisterMessage(CpeResponse.Purls)

VulnerabilityResponse = _reflection.GeneratedProtocolMessageType('VulnerabilityResponse', (_message.Message,), {

  'Vulnerabilities' : _reflection.GeneratedProtocolMessageType('Vulnerabilities', (_message.Message,), {
    'DESCRIPTOR' : _VULNERABILITYRESPONSE_VULNERABILITIES,
    '__module__' : 'scanoss.api.vulnerabilities.v2.scanoss_vulnerabilities_pb2'
    # @@protoc_insertion_point(class_scope:scanoss.api.vulnerabilities.v2.VulnerabilityResponse.Vulnerabilities)
    })
  ,

  'Purls' : _reflection.GeneratedProtocolMessageType('Purls', (_message.Message,), {
    'DESCRIPTOR' : _VULNERABILITYRESPONSE_PURLS,
    '__module__' : 'scanoss.api.vulnerabilities.v2.scanoss_vulnerabilities_pb2'
    # @@protoc_insertion_point(class_scope:scanoss.api.vulnerabilities.v2.VulnerabilityResponse.Purls)
    })
  ,
  'DESCRIPTOR' : _VULNERABILITYRESPONSE,
  '__module__' : 'scanoss.api.vulnerabilities.v2.scanoss_vulnerabilities_pb2'
  # @@protoc_insertion_point(class_scope:scanoss.api.vulnerabilities.v2.VulnerabilityResponse)
  })
_sym_db.RegisterMessage(VulnerabilityResponse)
_sym_db.RegisterMessage(VulnerabilityResponse.Vulnerabilities)
_sym_db.RegisterMessage(VulnerabilityResponse.Purls)


DESCRIPTOR._options = None

_VULNERABILITIES = _descriptor.ServiceDescriptor(
  name='Vulnerabilities',
  full_name='scanoss.api.vulnerabilities.v2.Vulnerabilities',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=881,
  serialized_end=1221,
  methods=[
  _descriptor.MethodDescriptor(
    name='Echo',
    full_name='scanoss.api.vulnerabilities.v2.Vulnerabilities.Echo',
    index=0,
    containing_service=None,
    input_type=scanoss_dot_api_dot_common_dot_v2_dot_scanoss__common__pb2._ECHOREQUEST,
    output_type=scanoss_dot_api_dot_common_dot_v2_dot_scanoss__common__pb2._ECHORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetCpes',
    full_name='scanoss.api.vulnerabilities.v2.Vulnerabilities.GetCpes',
    index=1,
    containing_service=None,
    input_type=_VULNERABILITYREQUEST,
    output_type=_CPERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetVulnerabilities',
    full_name='scanoss.api.vulnerabilities.v2.Vulnerabilities.GetVulnerabilities',
    index=2,
    containing_service=None,
    input_type=_VULNERABILITYREQUEST,
    output_type=_VULNERABILITYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_VULNERABILITIES)

DESCRIPTOR.services_by_name['Vulnerabilities'] = _VULNERABILITIES

# @@protoc_insertion_point(module_scope)