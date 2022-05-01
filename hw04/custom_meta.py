"""
Module for metaclass which adds "custom_" prefix before all attributes
"""


class CustomMeta(type):
    """
    Metaclass which adds "custom_" prefix before all attributes
    """
    def __new__(cls, name, bases, dct):
        def __setattr__(self, name, val):
            self.__dict__[f'custom_{name}'] = val

        custom_attributes = {'custom_' + attr_name if not (attr_name.startswith('__')
                                                           and attr_name.endswith('__')) else attr_name:
                             attr_value for attr_name, attr_value in dct.items()}
        custom_attributes['__setattr__'] = __setattr__
        return super().__new__(cls, name, bases, custom_attributes)

    def __call__(cls, *args, **kwargs):
        cls_new = super(CustomMeta, cls).__call__(*args, **kwargs)
        custom_attributes = {'custom_' + attr_name if not (attr_name.startswith('__')
                                                           and attr_name.endswith('__')) else attr_name:
                             attr_value for attr_name, attr_value in cls_new.__dict__.items()}
        cls_new.__dict__ = custom_attributes
        return cls_new
