from typing import Type, TypeVar, get_type_hints

T = TypeVar('T')


class FromDictMixin:
    @classmethod
    def from_dict(cls: Type[T], data: dict) -> T:
        instance = cls.__new__(cls)
        type_hints = get_type_hints(cls)

        for field_name, field_type in type_hints.items():
            if field_name in data:
                value = data[field_name]
                if isinstance(value, dict) and hasattr(field_type, 'from_dict'):
                    setattr(instance, field_name, field_type.from_dict(value))
                else:
                    setattr(instance, field_name, value)

        return instance
