# REST API

## body vs query string

Usually:

- The content body is used for the data that is to be uploaded/downloaded to/from the server.
- The query parameters are used to specify the exact data requested.

For example when you upload a file you specify the name, mime type, etc. in the body but when you fetch list of files you can use the query parameters to filter the list by some property of the files. In general, the query parameters are property of the query not the data.

Of course this is not a strict rule - you can implement it in whatever way you find more appropriate/working for you.



## References

[REST API Best practices: args in query string vs in request body](https://stackoverflow.com/questions/25385559/rest-api-best-practices-args-in-query-string-vs-in-request-body)

