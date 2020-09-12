# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: order.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='order.proto',
  package='order',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0border.proto\x12\x05order\"b\n\x12\x43reateOrderRequest\x12\x14\n\x0crestaurantId\x18\x01 \x01(\x03\x12\x12\n\nconsumerId\x18\x02 \x01(\x03\x12\"\n\tlineItems\x18\x03 \x03(\x0b\x32\x0f.order.LineItem\"0\n\x08LineItem\x12\x12\n\nmenuItemId\x18\x01 \x01(\x03\x12\x10\n\x08quantity\x18\x02 \x01(\x05\"O\n\x10\x43reateOrderReply\x12\x16\n\x0erestaurantName\x18\x01 \x01(\t\x12\x14\n\x0c\x63onsumerName\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\x03\x32S\n\x0cOrderService\x12\x43\n\x0b\x63reateOrder\x12\x19.order.CreateOrderRequest\x1a\x17.order.CreateOrderReply\"\x00\x62\x06proto3'
)




_CREATEORDERREQUEST = _descriptor.Descriptor(
  name='CreateOrderRequest',
  full_name='order.CreateOrderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='restaurantId', full_name='order.CreateOrderRequest.restaurantId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='consumerId', full_name='order.CreateOrderRequest.consumerId', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lineItems', full_name='order.CreateOrderRequest.lineItems', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=22,
  serialized_end=120,
)


_LINEITEM = _descriptor.Descriptor(
  name='LineItem',
  full_name='order.LineItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='menuItemId', full_name='order.LineItem.menuItemId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='order.LineItem.quantity', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=122,
  serialized_end=170,
)


_CREATEORDERREPLY = _descriptor.Descriptor(
  name='CreateOrderReply',
  full_name='order.CreateOrderReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='restaurantName', full_name='order.CreateOrderReply.restaurantName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='consumerName', full_name='order.CreateOrderReply.consumerName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='order.CreateOrderReply.price', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=172,
  serialized_end=251,
)

_CREATEORDERREQUEST.fields_by_name['lineItems'].message_type = _LINEITEM
DESCRIPTOR.message_types_by_name['CreateOrderRequest'] = _CREATEORDERREQUEST
DESCRIPTOR.message_types_by_name['LineItem'] = _LINEITEM
DESCRIPTOR.message_types_by_name['CreateOrderReply'] = _CREATEORDERREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateOrderRequest = _reflection.GeneratedProtocolMessageType('CreateOrderRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEORDERREQUEST,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:order.CreateOrderRequest)
  })
_sym_db.RegisterMessage(CreateOrderRequest)

LineItem = _reflection.GeneratedProtocolMessageType('LineItem', (_message.Message,), {
  'DESCRIPTOR' : _LINEITEM,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:order.LineItem)
  })
_sym_db.RegisterMessage(LineItem)

CreateOrderReply = _reflection.GeneratedProtocolMessageType('CreateOrderReply', (_message.Message,), {
  'DESCRIPTOR' : _CREATEORDERREPLY,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:order.CreateOrderReply)
  })
_sym_db.RegisterMessage(CreateOrderReply)



_ORDERSERVICE = _descriptor.ServiceDescriptor(
  name='OrderService',
  full_name='order.OrderService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=253,
  serialized_end=336,
  methods=[
  _descriptor.MethodDescriptor(
    name='createOrder',
    full_name='order.OrderService.createOrder',
    index=0,
    containing_service=None,
    input_type=_CREATEORDERREQUEST,
    output_type=_CREATEORDERREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ORDERSERVICE)

DESCRIPTOR.services_by_name['OrderService'] = _ORDERSERVICE

# @@protoc_insertion_point(module_scope)