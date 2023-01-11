#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2023/1/10
# @file __init__.py.py

# from utils import setting, log, scanner_, util
#
# from util import exec_
# from . import util, scanner_, setting, log
# from . import timer, timer_ns
# from . import Setting, exec_
# from . import get_logger as logger_

# from .log import get_logger
# from .setting import Setting
# from .util import exec_
# from utils.util import *
# from utils.scanner_ import *
# from utils.setting import *
# from utils.log import get_logger




# def lazy_import(module_name, submodules, submod_attrs):
#     """
#     Boilerplate to define PEP 562 __getattr__ for lazy import
#     https://www.python.org/dev/peps/pep-0562/
#     """
#     import importlib
#     import os
#     name_to_submod = {
#         func: mod for mod, funcs in submod_attrs.items()
#         for func in funcs
#     }
#
#     def __getattr__(name):
#         if name in submodules:
#             attr = importlib.import_module(
#                 '{module_name}.{name}'.format(
#                     module_name=module_name, name=name)
#             )
#         elif name in name_to_submod:
#             submodname = name_to_submod[name]
#             module = importlib.import_module(
#                 '{module_name}.{submodname}'.format(
#                     module_name=module_name, submodname=submodname)
#             )
#             attr = getattr(module, name)
#         else:
#             raise AttributeError(
#                 'No {module_name} attribute {name}'.format(
#                     module_name=module_name, name=name))
#         globals()[name] = attr
#         return attr
#
#     if os.environ.get('EAGER_IMPORT', ''):
#         for name in submodules:
#             __getattr__(name)
#
#         for attrs in submod_attrs.values():
#             for attr in attrs:
#                 __getattr__(attr)
#     return __getattr__
#
#
# __getattr__ = lazy_import(
#     __name__,
#     submodules={
#         'log',
#         'scanner_',
#         'setting',
#         'timer',
#         'util',
#     },
#     submod_attrs={
#         'log'     : [
#             'get_logger',
#         ],
#         'scanner_': [
#             'Scanner',
#         ],
#         'setting' : [
#             'Setting',
#         ],
#         'timer'   : [
#             'timer',
#             'timer_ns',
#         ],
#         'util'    : [
#             'exec_'
#         ]
#     },
# )
#
#
# def __dir__():
#     return __all__


# __all__ = ['get_logger', 'Scanner', 'setting_', 'Setting', 'timer', 'timer_ns', 'exec_']
