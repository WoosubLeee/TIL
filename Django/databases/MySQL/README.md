# Using MySQL in Django

## Connecting to the database

Connection settings are used in this order:

1. `OPTIONS`
2. `NAME`, `USER`, `PASSWORD`, `HOST`, `PORT`
3. MySQL option files

In other words, if you set the name of the database in `OPTIONS`, this will take precedence over `NAME`, which would override anything in a MySQL option file.



## References

https://docs.djangoproject.com/en/3.2/ref/databases/#mysql-notes