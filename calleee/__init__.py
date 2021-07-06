"""
calleee
"""
__version__ = "0.4.0"
__description__ = "Argument matchers for unittest.mock"
__author__ = "Karol Kuczmarski"
__license__ = "BSD"


from calleee.attributes import Attrs, Attr, HasAttrs, HasAttr
from calleee.base import \
    And, Either, Eq, Is, IsNot, OneOf, Or, Matcher, Not, Xor
from calleee.collections import \
    Dict, Generator, Iterable, List, Mapping, OrderedDict, Sequence, Set
from calleee.general import Any, ArgThat, Captor, Matching
from calleee.functions import \
    Callable, CoroutineFunction, Function, GeneratorFunction
from calleee.numbers import (Complex, Float, Fraction, Int, Integer, Integral,
                            Long, Number, Rational, Real)
from calleee.objects import Bytes, Coroutine, FileLike
from calleee.operators import (
    Contains,
    Ge, Greater, GreaterOrEqual, GreaterOrEqualTo, GreaterThan, Gt,
    In,
    Le, Less, LessOrEqual, LessOrEqualTo, LessThan,
    Longer, LongerOrEqual, LongerOrEqualTo, LongerThan, Lt,
    Shorter, ShorterOrEqual, ShorterOrEqualTo, ShorterThan)
from calleee.strings import \
    EndsWith, Glob, Regex, StartsWith, String, Unicode
from calleee.types import InstanceOf, IsA, SubclassOf, Inherits, Type, Class


__all__ = [
    'Matcher',
    'Eq', 'Is', 'IsNot',
    'Not', 'And', 'Or', 'Either', 'OneOf', 'Xor',

    'Attrs', 'Attr', 'HasAttrs', 'HasAttr',

    'Iterable', 'Generator',
    'Sequence', 'List', 'Set',
    'Mapping', 'Dict', 'OrderedDict',

    'Any', 'Matching', 'ArgThat', 'Captor',

    'Callable', 'Function', 'GeneratorFunction',
    'CoroutineFunction',

    'Number',
    'Complex', 'Real', 'Float', 'Rational', 'Fraction',
    'Integral', 'Integer', 'Int', 'Long',

    'Bytes',
    'Coroutine',
    'FileLike',

    'Less', 'LessThan', 'Lt',
    'LessOrEqual', 'LessOrEqualTo', 'Le',
    'Greater', 'GreaterThan', 'Gt',
    'GreaterOrEqual', 'GreaterOrEqualTo', 'Ge',
    'Shorter', 'ShorterThan', 'ShorterOrEqual', 'ShorterOrEqualTo',
    'Longer', 'LongerThan', 'LongerOrEqual', 'LongerOrEqualTo',
    'Contains', 'In',

    'String', 'Unicode',
    'StartsWith', 'EndsWith', 'Glob', 'Regex',

    'InstanceOf', 'IsA', 'SubclassOf', 'Inherits', 'Type', 'Class',
]
