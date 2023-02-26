from enum import Enum


class NonIterable:
    """Descriptor for non-iterable class methods"""
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        self.instance = instance
        return self

    def __call__(self, *args, **kwargs):
        return self.func(self.instance, *args, **kwargs)


def non_iterable(func):
    """Prevents the decorated method from being included in the iteration of an object"""
    return NonIterable(func)


class CustomEnum:
    """Defining enumerated types, where class members represent enumerated values"""
    _items = None

    def __get_items(self):
        items = []
        attributes = dir(self)

        for attr_name in attributes:
            value = getattr(self, attr_name)
            if attr_name.startswith('_') or isinstance(value, NonIterable):
                continue

            items.append((attr_name, value))

        return items

    # def __get_items(self):
    #     return [(attr_name, getattr(self, attr_name))
    #              for attr_name in dir(self)
    #             if not attr_name.startswith('_') \
    #             and not isinstance(getattr(self, attr_name), NonIterable)]

    def __iter__(self):
        self._items = self.__get_items()
        self._index = 0
        return iter(self._items)

    def __next__(self):
        if self._index < len(self._items):
            x = self._items[self._index]
            self._index += 1
            return x
        else:
            raise StopIteration

    def __get_values(self):
        return [value for _, value in self]

    def __get_keys(self):
        return [key for key, _ in self]

    @non_iterable
    def values(self):
        return self.__get_values()

    @non_iterable
    def keys(self):
        return self.__get_keys()

    @non_iterable
    def items(self):
        return self.__get_items()




class StaticCustomEnumWrapper(CustomEnum):
    def __init__(self, *args, **kwargs):
        for attr_name, value in args[2].items():
            if attr_name.startswith('_') or isinstance(value, NonIterable):
                continue
            self.__setattr__(attr_name, value)

class StaticCustomEnum(metaclass=StaticCustomEnumWrapper):
    pass

