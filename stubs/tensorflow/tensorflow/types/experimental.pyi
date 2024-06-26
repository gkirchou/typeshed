import abc
from _typeshed import Incomplete
from typing import Any, Generic, TypeVar, overload
from typing_extensions import ParamSpec

import tensorflow as tf
from tensorflow._aliases import ContainerGeneric

_P = ParamSpec("_P")
_R = TypeVar("_R", covariant=True)

class Callable(Generic[_P, _R], metaclass=abc.ABCMeta):
    def __call__(self, *args: _P.args, **kwargs: _P.kwargs) -> _R: ...

class ConcreteFunction(Callable[_P, _R], metaclass=abc.ABCMeta):
    def __call__(self, *args: _P.args, **kwargs: _P.kwargs) -> _R: ...

class GenericFunction(Callable[_P, _R], metaclass=abc.ABCMeta):
    @overload
    @abc.abstractmethod
    def get_concrete_function(self, *args: _P.args, **kwargs: _P.kwargs) -> ConcreteFunction[_P, _R]: ...
    @overload
    @abc.abstractmethod
    def get_concrete_function(
        self, *args: ContainerGeneric[tf.TypeSpec[Any]], **kwargs: ContainerGeneric[tf.TypeSpec[Any]]
    ) -> ConcreteFunction[_P, _R]: ...
    def experimental_get_compiler_ir(self, *args, **kwargs): ...

def __getattr__(name: str) -> Incomplete: ...
