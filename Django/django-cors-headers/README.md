# django-cors-headers

A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses. This allows in-browser requests to your Django application from other origins.



## Setup

```bash
$ python -m pip install django-cors-headers
```

Then add it to your installed apps:

```python
INSTALLED_APPS = [
    ...,
    "corsheaders",
    ...,
]
```

You will also need to add a middleware class to listen in on responses:

```python
MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware", # before this module
    ...,
]
```



## Configuration

You must set at least one of three following settings:

- `CORS_ALLOWED_ORIGINS`
- `CORS_ALLOWED_ORIGIN_REGEXES`
- `CORS_ALLOW_ALL_ORIGINS`

### `CORS_ALLOWED_ORIGINS`

A list of origins that are authorized to make cross-site HTTP requests. Defaults to `[]`.

```python
CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
]
```

### `CORS_ALLOWED_ORIGIN_REGEXES`

A list of strings representing regexes that match Origins that are authorized to make cross-site HTTP requests. Defaults to `[]`. Useful when `CORS_ALLOWED_ORIGINS` is impractical, such as when you have a large number of subdomains.

```python
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://\w+\.example\.com$",
]
```

### `CORS_ALLOW_ALL_ORIGINS`

If `True`, all origins will be allowed. Other settings restricting allowed origins will be ignored. Defaults to `False`. Setting this to `True` can be *dangerous*, as it allows any website to make cross-origin requests to yours.



## References

https://pypi.org/project/django-cors-headers/