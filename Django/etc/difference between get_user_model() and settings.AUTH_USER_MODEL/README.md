# difference between `get_user_model()` and `settings.AUTH_USER_MODEL`

In particularly, you have to use:

- `get_user_model()` when you need to import the User model to query it. E.g.

```py
User = get_user_model()
User.objects.filter(...)
```

- `settings.AUTH_USER_MODEL` when you need to referencing User model in `ForeignKey`, `ManyToManyField` or `OneToOneField`. E.g.

```py
class MyModel(models.Model):
 user = models.ForeignKey(settings.AUTH_USER_MODEL)
```

If you try to user `get_user_model()` when creating ForeignKey`,`ManyToManyField`or`OneToOneField` you may have circular import issues.

You also have to set `settings.AUTH_USER_MODEL` in your `settings.py` if you want to provide a custom implementation for the user model. E.g. `AUTH_USER_MODEL='myapp.MyUserModel`



## References

[WHAT IS DIFFERENCE BETWEEN get_user_model() ,settings.AUTH_USER_MODEL and USER in django?](https://stackoverflow.com/questions/54720133/what-is-difference-between-get-user-model-settings-auth-user-model-and-user-i)

