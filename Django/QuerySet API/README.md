# Django QuerySet API

## Methods that do not return QuerySets

### `get_or_create()`

A convenience method for looking up an object with the given `kwargs`, creating one if necessary. Returns a tuple of `(object, created)`, where `object` is the retrieved or created object and `created` is a boolean specifying whether a new object was created.

```python
obj, created = Person.objects.get_or_create(
    first_name='John',
    last_name='Lennon',
    defaults={'birthday': date(1940, 10, 9)},
)
```

위 코드는 다음 코드와 같은 결과를 낸다:

```python
try:
    obj = Person.objects.get(first_name='John', last_name='Lennon')
except Person.DoesNotExist:
    obj = Person(first_name='John', last_name='Lennon', birthday=date(1940, 10, 9))
    obj.save()
```

Any keyword arguments passed to `get_or_create()` — *except* an optional one called `defaults` — will be used in a `get()` call.

#### more complex conditions

You can specify more complex conditions for the retrieved object by chaining `get_or_create()` with `filter()` and using [`Q objects`](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#django.db.models.Q). For example, to retrieve Robert or Bob Marley if either exists, and create the latter otherwise:

```python
from django.db.models import Q

obj, created = Person.objects.filter(
    Q(first_name='Bob') | Q(first_name='Robert'),
).get_or_create(last_name='Marley', defaults={'first_name': 'Bob'})
```



## References

https://docs.djangoproject.com/en/4.0/ref/models/querysets/#get-or-create
