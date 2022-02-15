# DRF ViewSets

Django REST framework allows you to combine the logic for a set of related views in a single class, called a `ViewSet`. In other frameworks you may also find conceptually similar implementations named something like 'Resources' or 'Controllers'.

## ViewSet actions

The default routers included with REST framework will provide routes for a standard set of create/retrieve/update/destroy style actions, as shown below:

```python
class UserViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
```

### Attributes

During dispatch, the following attributes are available on the `ViewSet`.

- `basename` - the base to use for the URL names that are created.
- `action` - the name of the current action (e.g., `list`, `create`).
- `detail` - boolean indicating if the current action is configured for a list or detail view.
- `suffix` - the display suffix for the viewset type - mirrors the `detail` attribute.
- `name` - the display name for the viewset. This argument is mutually exclusive to `suffix`.
- `description` - the display description for the individual view of a viewset.

#### ex)

```python
def get_permissions(self):
    """
    Instantiates and returns the list of permissions that this view requires.
    """
    if self.action == 'list':
        permission_classes = [IsAuthenticated]
    else:
        permission_classes = [IsAdminUser]
    return [permission() for permission in permission_classes]
```

### Making extra actions

Default action 이외에 action을 추가하려면, you can mark them as such with the `@action` decorator. Like regular actions, extra actions may be intended for either a single object, or an entire collection(list인지, detail인지). To indicate this, set the `detail` argument to `True` or `False`.

The router will configure its URL patterns accordingly. e.g., the `DefaultRouter` will configure detail actions to contain `pk` in their URL patterns.

```python
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from myapp.serializers import UserSerializer, PasswordSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
	
    # detail=True이므로 pk가 포함된 URL로 접근한다.
    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False)
    def recent_users(self, request):
        recent_users = User.objects.all().order_by('-last_login')

        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)
```

The `action` decorator will route `GET` requests by default, but may also accept other HTTP methods by setting the `methods` argument. For example:

```python
@action(detail=True, methods=['post', 'delete'])
```

The decorator allows you to override any viewset-level configuration such as `permission_classes`, `serializer_class`, `filter_backends`...:

```python
@action(detail=True, methods=['post'], permission_classes=[IsAdminOrIsSelf])
```

#### URLS

The two new actions will then be available at the urls:

- `/users/{pk}/set_password/`
- `/users/{pk}/unset_password/`



## References

https://www.django-rest-framework.org/api-guide/viewsets/#viewsets