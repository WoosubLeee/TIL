# Django custom authentication

## Substituting a custom `User` model

To override the default user model by adding:

```python
# settings.py

AUTH_USER_MODEL = 'myapp.MyUser'
```

This dotted pair describes the label of the Django app (which must be in your `INSTALLED_APPS`, and the name of the Django model that you wish to use as your user model.

### Specifying a custom `User` model

The easiest way to construct a compliant custom user model is to inherit from `AbstractBaseUser`. `AbstractBaseUser` provides the core implementation of a user model, including hashed passwords and tokenized password resets. You must then provide some key implementation details:

#### Fields

##### `USERNAME_FIELD`

A string describing the name of the field on the user model that is used as the unique identifier. This will usually be a username of some kind, but it can also be an email address, or any other unique identifier. The field *must* be unique (i.e., have `unique=True` set in its definition), unless you use a custom authentication backend that can support non-unique usernames.

In the following example, the field `identifier` is used as the identifying field:

```python
class MyUser(AbstractBaseUser):
    identifier = models.CharField(max_length=40, unique=True)
    ...
    USERNAME_FIELD = 'identifier'
```

##### `REQUIRED_FIELDS`

A list of the field names that will be prompted for when creating a user via the `createsuperuser` management command. The user will be prompted to supply a value for each of these fields. It must include any field for which `blank` is `False` or undefined and may include additional fields you want prompted for when a user is created interactively. `REQUIRED_FIELDS` has no effect in other parts of Django, like creating a user in the admin.

For example, here is the partial definition for a user model that defines two required fields - a date of birth and height:

```python
class MyUser(AbstractBaseUser):
    ...
    date_of_birth = models.DateField()
    height = models.FloatField()
    ...
    REQUIRED_FIELDS = ['date_of_birth', 'height']
```

`REQUIRED_FIELDS` must contain all required fields on your user model, but should *not* contain the `USERNAME_FIELD` or `password` as these fields will always be prompted for.

### ex)

```python
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
```

#### * `AbstractUser`

If you’re entirely happy with Django’s `User` model, but you want to add some additional profile information, you could subclass `django.contrib.auth.models.AbstractUser` and add your custom profile fields, although we’d recommend a separate model.

### Writing a manager for a custom user model

If your user model defines `username`, `email`, `is_staff`, `is_active`, `is_superuser`, `last_login`, and `date_joined` fields the same as Django’s default user, you can install Django’s `UserManager`; however, if not, you’ll need to define a custom manager that extends `BaseUserManager` providing two additional methods:

#### `create_user`(*username_field*, *password=None*, ***other_fields*)[¶](https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#django.contrib.auth.models.CustomUserManager.create_user)

The prototype of `create_user()` should accept the username field, plus all required fields as arguments. For example, if your user model uses `email` as the username field, and has `date_of_birth` as a required field, then `create_user` should be defined as:

```python
def create_user(self, email, date_of_birth, password=None):
    # create user here
```

#### `create_superuser`(*username_field*, *password=None*, ***other_fields*)[¶](https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#django.contrib.auth.models.CustomUserManager.create_superuser)

Same as `create_user()`

### Referencing the `User` model

If you reference `User` directly (for example, by referring to it in a foreign key), your code will not work in projects where the `AUTH_USER_MODEL` setting has been changed to a different user model.

#### `get_user_model()`

Instead of referring to `User` directly, you should reference the user model using `django.contrib.auth.get_user_model()`. This method will return the currently active user model – the custom user model if one is specified, or `User` otherwise.

When you define a foreign key or many-to-many relations to the user model, you should specify the custom model using the `AUTH_USER_MODEL` setting. For example:

```python
from django.conf import settings
from django.db import models

class Article(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
```

### Using a custom `user` model when starting a project

If you're using custom `User` model, it’s highly recommended to set up from the start. Because changing `AUTH_USER_MODEL` after you’ve created database tables is significantly more difficult since it affects foreign keys and many-to-many relationships, for example.

So even if the default `User` model is sufficient for you, 다음과 같이 미리 custom model을 작성해놓는 것이 강력히 권장된다.

```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```



## References

https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#substituting-a-custom-user-model