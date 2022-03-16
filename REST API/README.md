# REST API

It is a software architectural style to guide the design of architecture for the web. Any API (Application Programming Interface) that follows the REST design principle is said to be RESTful. Simply put, a REST API is a medium for two computers to communicate over HTTP (Hypertext Transfer Protocol), in the same way clients and servers communicate.



## Best practices

### 1. Use JSON as the format for sending and receiving data

### 2. Use nouns instead of verbs in endpoint paths

This is because HTTP methods such as `GET`, `POST`, `PUT`, `PATCH`, and `DELETE` are already in verb form for performing basic CRUD operations.

With the two principles we discussed above in mind, we should create routes like GET `/articles/` for getting news articles. Likewise, POST `/articles/` is for adding a new article , PUT `/articles/:id` is for updating the article with the given `id`. DELETE `/articles/:id` is for deleting an existing article with the given ID.

### 3. Use logical nesting on endpoints

That is, if one object can contain another object, you should design the endpoint to reflect that. This is good practice regardless of whether your data is structured like this in your database.

```
'/articles/:articleId/comments'
```

However, nesting can go too far. After about the second or third level, nested endpoints can get unwieldy. Consider, instead, returning the URL to those resources instead, especially if that data is not necessarily contained within the top level object.

For example, suppose you wanted to return the author of particular comments. You could use `/articles/:articleId/comments/:commentId/author`. But that’s getting out of hand. Instead, return the URI for that particular user within the JSON response instead:

```
"author": "/users/:userId"
```

### 4. Handle errors gracefully and return standard error codes

### 5. Allow filtering, sorting, and pagination

### 6. Maintain good security practices

Most communication between client and server should be private since we often send and receive private information. Therefore, using SSL/TLS for security is a must. A SSL certificate isn’t too difficult to load onto a server and the cost is free or very low. There’s no reason not to make our REST APIs communicate over secure channels instead of in the open.

To enforce the principle of least privilege, we need to add role checks either for a single role, or have more granular roles for each user.

### 7. Cache data to improve performance

We can add caching to return data from the local memory cache instead of querying the database to get the data every time we want to retrieve some data that users request. However, the data that users get may be outdated. This may also lead to issues when debugging in production environments when something goes wrong as we keep seeing old data.

### 8. Versioning our APIs



## Etc

### body vs query string

Usually:

- The content body is used for the data that is to be uploaded/downloaded to/from the server.
- The query parameters are used to specify the exact data requested.

For example when you upload a file you specify the name, mime type, etc. in the body but when you fetch list of files you can use the query parameters to filter the list by some property of the files. In general, the query parameters are property of the query not the data.

Of course this is not a strict rule - you can implement it in whatever way you find more appropriate/working for you.



## References

[Best practices for REST API design](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)

[REST API Best Practices – REST Endpoint Design Examples](https://www.freecodecamp.org/news/rest-api-best-practices-rest-endpoint-design-examples/)

[REST API Best practices: args in query string vs in request body](https://stackoverflow.com/questions/25385559/rest-api-best-practices-args-in-query-string-vs-in-request-body)

