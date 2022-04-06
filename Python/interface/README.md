# Python interface

An interface acts as a blueprint for designing classes. Interfaces define methods, but unlike classes, these methods are **abstract**.

## Informal interfaces

An informal Python interface is a class that defines methods that can be overridden, but there’s no strict enforcement.

```python
class InformalParserInterface:
    def load_data_source(self, path: str, file_name: str) -> str:
        pass

    def extract_text(self, full_file_name: str) -> dict:
        pass
```

`InformalParserInterface` defines the two methods `.load_data_source()` and `.extract_text()`. These methods are defined but not implemented. The implementation will occur once you create **concrete classes** that inherit from `InformalParserInterface`.

```python
class PdfParser(InformalParserInterface):
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides InformalParserInterface.extract_text()"""
        pass
```

```python
class EmlParser(InformalParserInterface):
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override InformalParserInterface.extract_text()
        """
        pass
```

You've defined two **concrete implementations** of the `InformalPythonInterface`. However, the second one(`EmlParser`) fails to properly define `.extract_text()`.

```python
>>> # Check if both PdfParser and EmlParser implement InformalParserInterface
>>> issubclass(PdfParser, InformalParserInterface)
True

>>> issubclass(EmlParser, InformalParserInterface)
True
```

```python
>>> PdfParser.__mro__
(__main__.PdfParser, __main__.InformalParserInterface, object)

>>> EmlParser.__mro__
(__main__.EmlParser, __main__.InformalParserInterface, object)
```

Interface를 제대로 implement하지 않았음에도 `issubclass()`와 `__mro__`(method resolution order: shows the superclasses of the class)에 모두 interface를 implement한 것으로 나온다.

Such informal interfaces are fine for small projects where only a few developers are working on the source code. However, as projects get larger and teams grow, this could lead to developers spending countless hours looking for hard-to-find logic errors in the codebase.

### Using metaclasses

그렇다면 `issubclass(EmlParser, InformalParserInterface)`가 `False`를 return하도록 하려면 어떻게 해야할까? To do this, you'll create a metaclass which overrides two dunder methods:

1. `.__instancecheck__()`
2. `.__subclasscheck__()`

```python
class ParserMeta(type):
    """A Parser metaclass that will be used for parser class creation.
    """
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and 
                callable(subclass.extract_text))

class UpdatedInformalParserInterface(metaclass=ParserMeta):
    """This interface is used for concrete classes to inherit from.
    There is no need to define the ParserMeta methods as any class
    as they are implicitly made available via .__subclasscheck__().
    """
    pass
```

이렇게 하면 methods를 정확히 define하지 않는다면 `issubclass()`에서 `False`를 return한다.

```python
>>> issubclass(PdfParserNew, UpdatedInformalParserInterface)
True

>>> issubclass(EmlParserNew, UpdatedInformalParserInterface)
False
```

하지만 이번에는 MRO의 경우를 보자:

```python
>>> PdfParserNew.__mro__
(<class '__main__.PdfParserNew'>, <class 'object'>)
```

`UpdatedInformalParserInterface`는 `PdfParserNew`의 superclass임에도 MRO에 나타나지 않는다. This unusual behavior is caused by the fact that  `UpdatedInformalParserInterface` is a **virtual base class** of `PdfParserNew`.

### Using virtual base classes

The key difference between virtual base classes and standard subclasses is that virtual base classes use the `.__subclasscheck__()` dunder method to implicitly check if a class is a virtual subclass of the superclass. Additionally, virtual base classes don’t appear in the subclass MRO.

아래와 같은 metaclass가 있다고 하자:

```python
class PersonMeta(type):
    """A person metaclass"""
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'name') and 
                callable(subclass.name) and 
                hasattr(subclass, 'age') and 
                callable(subclass.age))
```

You'll define two concrete classes, `Employee` and `Friend`:

```python
# Inheriting subclasses
class Employee(PersonSuper):
    """Inherits from PersonSuper
    PersonSuper will appear in Employee.__mro__
    """
    pass

class Friend:
    """Built implicitly from Person
    Friend is a virtual subclass of Person since
    both required methods exist.
    Person not in Friend.__mro__
    """
    def name(self):
        pass

    def age(self):
        pass
```

Although `Friend` does not explicitly inherit from `Person`, it implements `.name()` and `.age()`, so `Person` becomes a **virtual base class** of `Friend`.

```python
>>> issubclass(Friend, PersonMeta)
True
```



## Formal interfaces

Informal interfaces would be the wrong approach for larger applications. In order to create a **formal Python interface**, you’ll need a few more tools from Python’s `abc` module.

### Using `abc.ABCMeta`

To enforce the subclass instantiation of abstract methods, you’ll utilize Python’s builtin `ABCMeta` from the `abc` module. Rather than create your own metaclass, you’ll use `abc.ABCMeta` as the metaclass. Then, you’ll overwrite `.__subclasshook__()` in place of `.__instancecheck__()` and `.__subclasscheck__()`, as it creates a more reliable implementation of these dunder methods.

```python
import abc

class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and 
                callable(subclass.extract_text))
```

If you run `issubclass()` on `PdfParserNew` and `EmlParserNew`, then `issubclass()` will return `True` and `False`, respectively.

### Using `abc` to register a virtual subclass

Once you’ve imported the `abc` module, you can directly **register a virtual subclass** by using the `.register()` metamethod. In the next example, you register the interface `Double` as a virtual base class of the built-in `__float__` class:

```python
class Double(metaclass=abc.ABCMeta):
    pass

Double.register(float)
```

```python
>>> issubclass(float, Double)
True

>>> isinstance(1.2345, Double)
True
```

Once you’ve registered `Double`, you can use it as class decorator to set the decorated class as a virtual subclass:

```python
@Double.register
class Double64:
    pass

print(issubclass(Double64, Double))  # True
```

The decorator register method helps you to create a hierarchy of custom virtual class inheritance.

### Using subclass detection with registration

`.__subclasshook__()` takes precedence to `.register()`. If you want `.register()` is taken into consideration, you must add `NotImplemented` to the `.__subclasshook__()`.

```python
class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and 
                callable(subclass.extract_text) or 
                NotImplemented)
```

```python
@FormalParserInterface.register
class EmlParserNew:
    def load_data_source(self, path: str, file_name: str) -> str:
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass

print(issubclass(EmlParserNew, FormalParserInterface))  # True
```

### Using abstract method declaration

The **abstract method** must be overridden by the concrete class that implements the interface in question. To create abstract methods in Python, you add the `@abc.abstractmethod` decorator to the interface’s methods.

```python
class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and 
                callable(subclass.extract_text) or 
                NotImplemented)

    @abc.abstractmethod
    def load_data_source(self, path: str, file_name: str):
        raise NotImplementedError

    @abc.abstractmethod
    def extract_text(self, full_file_path: str):
        raise NotImplementedError
```

```python
class PdfParserNew(FormalParserInterface):
    def load_data_source(self, path: str, file_name: str) -> str:
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass

class EmlParserNew(FormalParserInterface):
    def load_data_source(self, path: str, file_name: str) -> str:
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass
```

```python
>>> pdf_parser = PdfParserNew()
>>> eml_parser = EmlParserNew()
Traceback (most recent call last):
  File "real_python_interfaces.py", line 53, in <module>
    eml_interface = EmlParserNew()
TypeError: Can't instantiate abstract class EmlParserNew with abstract methods extract_text
```



## References

[Implementing an Interface in Python](https://realpython.com/python-interface/)