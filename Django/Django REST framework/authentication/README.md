# DRF authentication

## `TokenAuthentication`

This authentication scheme uses a simple token-based HTTP Authentication scheme. Token authentication is appropriate for client-server setups, such as native desktop and mobile clients.

To use the `TokenAuthentication` scheme you'll need to configure the authentication classes to include `TokenAuthentication`, and additionally include `rest_framework.authtoken` in your `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = [
    ...
    'rest_framework.authtoken'
]
```

and migrate so the `authtoken` app can provide Django database migrations.

For clients to authenticate, the token key should be included in the `Authorization` HTTP header. The key should be prefixed by the string literal "Token", with whitespace separating the two strings. For example:

```python
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

If you want to use a different keyword in the header, such as `Bearer`, simply subclass `TokenAuthentication` and set the `keyword` class variable.

If successfully authenticated, `TokenAuthentication` provides the following credentials.

- `request.user` will be a Django `User` instance.
- `request.auth` will be a `rest_framework.authtoken.models.Token` instance.

### Generation tokens

When using `TokenAuthentication`, you may want to provide a mechanism for clients to obtain a token given the username and password. REST framework provides a built-in view to provide this behaviour. To use it, add the `obtain_auth_token` view to your URLconf. The URL part of the pattern can be whatever you want to use:

```python
from rest_framework.authtoken import views
urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]
```

By default, there are no permissions or throttling applied to the `obtain_auth_token` view. If you do wish to apply to throttle you'll need to override the view class, and include them using the `throttle_classes` attribute.

If you need a customized version of the `obtain_auth_token` view, you can do so by subclassing the `ObtainAuthToken` view class, and using that in your url conf instead.

```python
# views.py

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
```

```python
# urls.py

urlpatterns += [
    path('api-token-auth/', CustomAuthToken.as_view())
]
```

#### Custom AuthTokenSerializer

model이 달라지면 serializer의 validation도 다시 작성해야 할 경우도 있다.

```python
from rest_framework import serializers
from django.contrib.auth import authenticate

class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(write_only=True)
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(
                request=self.context.get('request'),
                email=email,
                password=password
            )
            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
```



## References

https://www.django-rest-framework.org/api-guide/authentication