# NumPy

## `numpy.argsort(a, axis=-1, kind=None, order=None)`

Perform an indirect sort along the given axis using the algorithm specified by the `kind` keyword. It returns an array of indices of the same shape as `a`.

### Parameters

- `a` : array to sort
- `axis` : `int` or `None`, default = `-1`(the last axis)
- `kind` : `{'quicksort', 'mergesort', 'heapsort', 'stable'}`, default = `'quicksort'`
- `order` : `str` or list of `str`

### Examples

#### One-dimensional array

```python
>>> x = np.array([3, 1, 2])
>>> np.argsort(x)
# x[1] = 1로 가장 작음
# x[2] = 2로 두번째로 작음
# x[0] = 3으로 가장 큼
array([1, 2, 0])
```

#### Two-dimensional array

```python
>>> x = np.array([[0, 3], [2, 2]])
>>> np.argsort(x, axis=0)
# sorts along first axis(down)
array([[0, 1],
       [1, 0]])
```

```python
>>> np.argsort(x, axis=1)
# sorts along last axis(across)
array([[0, 1],
       [0, 1]])
```

