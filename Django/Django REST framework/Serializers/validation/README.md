# DRF Serializers validation

## `is_valid()`

When deserializing data, you always need to call `is_valid()` before attempting to access the validated data. If any validation errors occur, the `.errors` property will contain a dictionary representing the resulting error messages. For example:

```python
serializer = CommentSerializer(data={'email': 'foobar', 'content': 'baz'})
serializer.is_valid()
# False
serializer.errors
# {'email': ['Enter a valid e-mail address.'], 'created': ['This field is required.']}
```

Each key in the dictionary will be the field name, and the values will be lists of strings of any error messages corresponding to that field. The `non_field_errors` key may also be present, and will list any general validation errors. The name of the `non_field_errors` key may be customized using the `NON_FIELD_ERRORS_KEY` REST framework setting.

When deserializing a list of items, errors will be returned as a list of dictionaries representing each of the deserialized items.

### `raise_exception`

The `.is_valid()` method takes an optional `raise_exception` flag that will cause it to raise a `serializers.ValidationError` exception if there are validation errors.

```python
# Return a 400 response if the data was invalid.
serializer.is_valid(raise_exception=True)
```



## Validation의 종류

### Field-level validation

You can specify custom field-level validation by adding `.validate_<field_name>`(`password`를 검증한다면 `validate_password`) methods to your `Serializer` subclass. Your `validate_<field_name>` methods should return the validated value or raise a `serializers.ValidationError`. For example:

```python
from rest_framework import serializers

class BlogPostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()

    def validate_title(self, value):
        """
        Check that the blog post is about Django.
        """
        if 'django' not in value.lower():
            raise serializers.ValidationError("Blog post is not about Django")
        return value
```

### Object-level validation

To do any other validation that requires access to multiple fields, add a method called `.validate()` to your `Serializer` subclass. This method takes a single argument, which is a dictionary of field values. It should raise a `serializers.ValidationError` if necessary, or just return the validated values. For example:

```python
from rest_framework import serializers

class EventSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=100)
    start = serializers.DateTimeField()
    finish = serializers.DateTimeField()

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data['start'] > data['finish']:
            raise serializers.ValidationError("finish must occur after start")
        return data
```

### Validators

Individual fields on a serializer can include validators, by declaring them on the field instance, for example:

```python
def multiple_of_ten(value):
    if value % 10 != 0:
        raise serializers.ValidationError('Not a multiple of ten')

class GameRecord(serializers.Serializer):
    score = IntegerField(validators=[multiple_of_ten])
    ...
```

Serializer classes can also include reusable validators that are applied to the complete set of field data. These validators are included by declaring them on an inner `Meta` class, like so:

```python
class EventSerializer(serializers.Serializer):
    name = serializers.CharField()
    room_number = serializers.IntegerField(choices=[101, 102, 103, 201])
    date = serializers.DateField()

    class Meta:
        # Each room only has one event per day.
        validators = [
            UniqueTogetherValidator(
                queryset=Event.objects.all(),
                fields=['room_number', 'date']
            )
        ]
```



## References

https://www.django-rest-framework.org/api-guide/serializers/#validation