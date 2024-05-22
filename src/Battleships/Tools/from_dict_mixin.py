from typing import Type, TypeVar, get_type_hints, List, get_origin, get_args

T = TypeVar('T')


class FromDictMixin:
    @classmethod
    def from_dict(cls: Type[T], data: dict) -> T:
        instance = cls.__new__(cls)  # Create a new instance without calling __init__
        type_hints = get_type_hints(cls)

        for field_name, field_type in type_hints.items():
            if field_name in data:
                value = data[field_name]

                origin_type = get_origin(field_type)
                args = get_args(field_type)

                if origin_type is list and len(args) == 1:
                    elem_type = args[0]
                    if hasattr(elem_type, 'from_dict'):
                        setattr(instance, field_name,
                                [elem_type.from_dict(item) if isinstance(item, dict) else item for item in value])
                    else:
                        setattr(instance, field_name, value)
                elif isinstance(value, dict) and hasattr(field_type, 'from_dict'):
                    setattr(instance, field_name, field_type.from_dict(value))
                else:
                    setattr(instance, field_name, value)

        return instance
