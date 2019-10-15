"""Utility"""
import re
from json import loads
from urllib.parse import urlencode

from django.http import QueryDict


class RequestBodyDecoder:
    """Request Body Decoder"""

    def __init__(self, body: bytes, default=QueryDict(urlencode({}))):
        self.body = body
        self.default = default

    def decode(self) -> QueryDict:
        """decode to QueryDict"""
        if not self.body:
            return self.default

        decode_methods = ("normal", "regex")
        for method in decode_methods:
            data = getattr(self, method)(self.body)
            if data:
                return self.to_query_dict(data)
        return self.default

    @staticmethod
    def to_query_dict(data: dict) -> QueryDict:
        """dict to QueryDict"""
        return QueryDict(urlencode(data))

    @staticmethod
    def normal(body: bytes) -> dict:
        """json decode"""
        try:
            return loads(body)
        except ValueError:
            return {}

    @staticmethod
    def regex(body: bytes) -> dict:
        """regex decode"""
        data = {}
        pattern = rb'name="(?P<name>.+)"\r\n\r\n(?P<value>.+)\r\n'
        for match in re.finditer(pattern, body):
            name, value = match.group("name"), match.group("value")
            data[name.decode()] = value.decode()
        return data
