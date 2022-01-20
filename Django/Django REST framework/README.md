# Django REST framework

> DRF 공식 문서 tutorial을 따라가며 작성한 내용이다.

## Tutorial 1: Serialization

### Installation

```bash
$ pip install djangorestframework
```

Add the `rest_framework` app to `INSTALLED_APPS`.

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

### Using ModelSerializers

Model은 다음과 같다.

```python
# snippets/models.py

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']
```

ModelSerializer는 다음과 같다.

```python
# snippets/serializers.py

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
```

It's important to remember that `ModelSerializer` classes don't do anything particularly magical, they are simply a shortcut for creating serializer classes:

- An automatically determined set of fields.
- Simple default implementations for the `create()` and `update()` methods.

### Writing regular Django views using our Serializer

```python
# snippets/views.py
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

@csrf_exempt
def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def snippet_detail(request, pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
```

```python
# snippets/urls.py

from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]
```



## Tutorial 2: Requests and Responses

### DRF의 강력한 기능들

#### Request objects

REST framework introduces a `Request` object that extends the regular `HttpRequest`, and provides more flexible request parsing. The core functionality of the `Request` object is the `request.data` attribute, which is similar to `request.POST`, but more useful for working with Web APIs.

#### Response objects

REST framework also introduces a `Response` object, which is a type of `TemplateResponse` that takes unrendered content and uses content negotiation to determine the correct content type to return to the client.

```python
return Response(data)  # Renders to content type as requested by the client.
```

#### Status codes

REST framework provides more explicit identifiers for each status code, such as `HTTP_400_BAD_REQUEST` in the `status` module.

#### Wrapping API views

REST framework provides two wrappers you can use to write API views.

1. The `@api_view` decorator for working with function based views.
2. The `APIView` class for working with class-based views.

These wrappers provide a few bits of functionality such as making sure you receive `Request` instances in your view, and adding context to `Response` objects so that content negotiation can be performed.

### Pulling it all together

```python
# snippets/views.py

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

Notice that we're no longer explicitly tying our requests or responses to a given content type. `request.data` can handle incoming `json` requests.



## Tutorial 3: Class-based Views

We can also write our API views using class-based views, rather than function based views. As we'll see this is a powerful pattern that allows us to reuse common functionality, and helps us keep our code DRY.

```python
# snippets/views.py

from django.http import Http404
from rest_framework.views import APIView

class SnippetList(APIView):
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SnippetDetail(APIView):
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

It looks pretty similar to the previous case, but we've got better separation between the different HTTP methods.

We'll also need to refactor our `snippets/urls.py` slightly now that we're using class-based views.

```python
# snippets/urls.py

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]
```

### Using mixins

One of the big wins of using class-based views is that it allows us to easily compose reusable bits of behaviour. We can compose the views by using the mixin classes.

```python
# snippets/views.py

from rest_framework import mixins
from rest_framework import generics

class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

The base class provides the core functionality, and the mixin classes provide the `.list()` and `.create()` actions. We're then explicitly binding the `get` and `post` methods to the appropriate actions.

`SnippetDetail` 클래스도 mixin을 사용하여 다시 작성해보자.

```python
# snippets/views.py

class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
```

Again we're using the `GenericAPIView` class to provide the core functionality, and adding in mixins to provide the `.retrieve()`, `.update()` and `.destroy()` actions.

### Using generic class-based views

We can go one step further. REST framework provides a set of already mixed-in generic views that we can use to trim down our `views.py` module even more.

```python
# snippets/views.py

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
```



## Tutorial 4: Authentication & Permissions

Currently our API doesn't have any restrictions on who can edit or delete code snippets. We'd like to have some more advanced behavior in order to make sure that:

- Code snippets are always associated with a creator.
- Only authenticated users may create snippets.
- Only the creator of a snippet may update or delete it.
- Unauthenticated requests should have full read-only access.

### Adding information to our model

Add the following field to the `Snippet` model.

```python
# snippets/models.py

owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
```

### Adding endpoints for our User models

```python
# snippets/serializers.py

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
```

Because `snippets` is a *reverse* relationship on the User model, it will not be included by default when using the `ModelSerializer` class, so we needed to add an explicit field for it.

We'll also add a couple of views to `views.py`. We'd like to just use read-only views for the user representations, so we'll use the `ListAPIView` and `RetrieveAPIView` generic class-based views.

```python
# snippets/views.py

from django.contrib.auth.models import User
from snippets.serializers import UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

```python
# snippets/urls.py

path('users/', views.UserList.as_view()),
path('users/<int:pk>/', views.UserDetail.as_view()),
```

### Associating Snippets with Users

Right now, if we created a code snippet, there'd be no way of associating the user that created the snippet, with the snippet instance. The user isn't sent as part of the serialized representation, but is instead a property of the incoming request.

The way we deal with that is by overriding a `.perform_create()` method on our snippet views, that allows us to modify how the instance save is managed, and handle any information that is implicit in the incoming request or requested URL.

```python
# snippets/views.py

class SnippetList(generics.ListCreateAPIView):
    # ...
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
```

The `create()` method of our serializer will now be passed an additional `'owner'` field, along with the validated data from the request.

### Updating our serializer

```python
# snippets/serializers.py

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
     class Meta:
         model = Snippet
         fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner',]
```

The `source` argument controls which attribute is used to populate a field, and can point at any attribute on the serialized instance.

### Adding required permissions to views

Now that code snippets are associated with users, we want to make sure that only authenticated users are able to create, update and delete code snippets.

REST framework includes a number of permission classes that we can use to restrict who can access a given view. In this case the one we're looking for is `IsAuthenticatedOrReadOnly`, which will ensure that authenticated requests get read-write access, and unauthenticated requests get read-only access.

```python
# snippets/views.py

from rest_framework import permissions

class SnippetList(generics.ListCreateAPIView):
    # ...
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    #...


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    # ...
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
```

### Object level permissions

To make only the user that created a code snippet is able to update or delete it, we're going to need to create a custom permission.

Create a new file, `permissions.py`

```python
# snippets/permissions.py

from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user
```

```python
# snippets/views.py

from snippets.permissions import IsOwnerOrReadOnly

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    # ...
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
```



## Tutorial 5: Relationships & Hyperlinked APIs

### Why use hyperlink in API?

There are several ways to implement relationship:

- Using primary keys. (original)
- Using hyperlinking between entities.
- Using a unique identifying slug field on the related entity.
- Using the default string representation of the related entity.
- Nesting the related entity inside the parent representation.
- Some other custom representation

The `HyperlinkedModelSerializer` has the following differences from `ModelSerializer`:

- It does not include the id field by default.
- It includes a url field, using `HyperlinkedIdentityField`.
- Relationships use `HyperlinkedRelatedField`, instead of `PrimaryKeyRelatedField`.

#### ex)

- `ModelSerializer`를 사용하는 경우

```json
"results": [
    {
        "email": "admin@min.com",
        "groups": [
            1,
            2
        ],
        "url": "http://127.0.0.1:8000/users/1/",
        "username": "admin"
    }
]
```

- `HyperlinkedModelSerializer`를 사용하는 경우

```json
 "results": [
	{
        "email": "admin@min.com",
        "groups": [
            "http://127.0.0.1:8000/groups/1/",
            "http://127.0.0.1:8000/groups/2/"
        ],
        "url": "http://127.0.0.1:8000/users/1/",
        "username": "admin"
    }
 ]
```

### Hyperlinking our API

```python
# snippets/serializers.py

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
```

### Naming URL patterns

- Our user serializer includes a field that refers to `'snippet-detail'`.
- Our snippet and user serializers include `'url'` fields that by default will refer to `'{model_name}-detail'`, which in this case will be `'snippet-detail'` and `'user-detail'`.

```python
# snippets/urls.py

from django.urls import path
from snippets import views

# API endpoints
urlpatterns = [
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]
```

### Adding pagination

The list views for users and code snippets could end up returning quite a lot of instances, so really we'd like to make sure we paginate the results, and allow the API client to step through each of the individual pages.

We can change the default list style to use pagination, by modifying our `tutorial/settings.py` file slightly. Add the following setting:

```python
# tutorial/settings.py

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```



## Tutorial 6: ViewSets & Routers

REST framework includes an abstraction for dealing with `ViewSets`, that allows the developer to concentrate on modeling the state and interactions of the API, and leave the URL construction to be handled automatically, based on common conventions.

### Refactoring to use ViewSets

Let's refactor our `UserList` and `UserDetail` views into a single `UserViewSet`. We can remove the two views, and replace them with a single class:

```python
# snippets/views.py

from rest_framework import viewsets

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

Here we've used the `ReadOnlyModelViewSet` class to automatically provide the default 'read-only' operations.

Next we're going to replace the `SnippetList` and `SnippetDetail` view classes. We can remove the two views, and again replace them with a single class.

```python
# snippets/views.py

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
```

### Binding ViewSets to URLs explicitly

Notice how we're creating multiple views from each `ViewSet` class, by binding the http methods to the required action for each view.

```python
# snippets/urls.py

from snippets.views import SnippetViewSet, UserViewSet

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
]
```

### Using Routers

The conventions for wiring up resources into views and urls can be handled automatically, using a `Router` class. All we need to do is register the appropriate view sets with a router, and let it do the rest.

```python
# snippets/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
```



## References

https://www.django-rest-framework.org/tutorial/1-serialization/

https://stackoverflow.com/questions/33421147/what-is-the-benefit-of-using-a-hyperlinkedmodelserializer-in-drf (What is the benefit of using a HyperlinkedModelSerializer in DRF?)
