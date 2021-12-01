# Python

## Functions

#### `getattr(object, name[, default])`

Return the value of the named attribute of *object*. *name* must be a string. For example, `getattr(x, 'foobar')` is equivalent to `x.foobar`. If the named attribute does not exist, *default* is returned if provided, otherwise `AttributeError` is raised.

```python
class sample:
    
    def __init__(self, x):
        self.x = x
    
    def foo(self):
        print('Hello, world!')
        
c = sample('woosub')

getattr(c, 'x') # woosub
getattr(c, 'foo') # sample.foo()
```

