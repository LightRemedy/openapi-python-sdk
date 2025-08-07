from tigeropen.push.pb import PushData_pb2 as _PushData_pb2
from tigeropen.push.pb import SocketCommon_pb2 as _SocketCommon_pb2_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from tigeropen.push.pb.SocketCommon_pb2 import SocketCommon as SocketCommon
from tigeropen.push.pb.PushData_pb2 import PushData as PushData

DESCRIPTOR: _descriptor.FileDescriptor

class Response(_message.Message):
    __slots__ = ("command", "id", "code", "msg", "body")
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    command: _SocketCommon_pb2_1.SocketCommon.Command
    id: int
    code: int
    msg: str
    body: _PushData_pb2.PushData
    def __init__(self, command: _Optional[_Union[_SocketCommon_pb2_1.SocketCommon.Command, str]] = ..., id: _Optional[int] = ..., code: _Optional[int] = ..., msg: _Optional[str] = ..., body: _Optional[_Union[_PushData_pb2.PushData, _Mapping]] = ...) -> None: ...
