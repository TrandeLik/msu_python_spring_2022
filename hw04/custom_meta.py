"""
Module for metaclass which adds "custom_" prefix before all attributes
"""


class CustomMeta(type):
    """
    Metaclass which adds "custom_" prefix before all attributes
    """
    def __new__(cls, name, bases, dct):
        custom_attributes = {'custom_' + attr_name if not attr_name.startswith('__') else attr_name:
                             attr_value for attr_name, attr_value in dct.items()}
        return super(CustomMeta, cls).__new__(cls, name, bases, custom_attributes)

    def __call__(cls, *args, **kwargs):
        cls_new = super(CustomMeta, cls).__call__(*args, **kwargs)
        custom_attributes = {'custom_' + attr_name if not attr_name.startswith('__') else attr_name:
                             attr_value for attr_name, attr_value in cls_new.__dict__.items()}
        cls_new.__dict__ = custom_attributes
        return cls_new
