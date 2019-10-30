from dataclasses import dataclass, field
from uuid import uuid4, UUID
from typing import Any, Optional


@dataclass(frozen=True)
class SimpleObject:
    """
    This object can only return its value based on version. When no version specified, returns the last value.
    Version less than 0 not allowed.
    When updating object, you must always specify the version which is higher than last change. or it's fail
    _version_to_value_list: [{'version': 0, 'value': 'Initial value'}, {'version': 1, 'value': 'Changed value'}]
    """
    name: str = 'Noname object'
    id: UUID = field(default_factory=uuid4)
    _version_to_value_list: tuple = ({'version': 0, 'value': 'Initial value'}, )

    def get_value(self, version: Optional[int] = None) -> Any:
        if version is None:
            return self._version_to_value_list[-1]['value']
        previous_item = self._version_to_value_list[0]
        for item in self._version_to_value_list:
            if item['version'] > version:
                return previous_item['value']
            previous_item = item

        return previous_item['value']

    def set_value(self, value: Any, version: Optional[int] = None) -> 'SimpleObject':
        if version is None:
            return SimpleObject(
                name=self.name,
                _version_to_value_list=self._version_to_value_list + ({'version': self.last_version() + 1, 'value': value}, ))

        if version <= self.last_version():
            return self

        return SimpleObject(name=self.name, _version_to_value_list=self._version_to_value_list + ({'version': version, 'value': value}, ))

    def last_version(self):
        return self._version_to_value_list[-1]['version']
