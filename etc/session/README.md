# Session

## What is a web session?

A **web session** is the amount of time that a user spends browsing a given website: from the moment they arrive on the first page, to the moment they leave the site.



## How do web sessions work?

In practice, a web session consists of the data or files that are persistent throughout the use of a website or web application. These resources are uniquely identified with a **session ID**. The user's browser is given this ID upon beginning a new session, and this ID is exchanged during each subsequent communication between the browser and the server.

A web session includes all the information that may be relevant during the user's visit. Depending on the purpose of the website or web application, this may include data such as:

- The pages the user has viewed
- The contact details that the user has entered into a form
- The items in the user's shopping cart

There is typically some upper time limit for web sessions, after which the session will time out. This maximum time limit depends on the implementation. For example, web sessions in [Google Analytics](https://support.google.com/analytics/answer/2731565?hl=en) expire after 30 minutes of inactivity; further user activity will be treated as a new session.

Websites and web applications with very high numbers of users often cache web sessions, so that they can be retrieved faster and more efficiently.



## Why use web sessions?

HTTP에는 Connectionless(비연결성)와 Stateless(비상태성)이라는 특징이 있다. 서버의 자원을 절약하기 위해 요청마다 연결과 해제의 과정을 거치기 때문에 연결 상태가 유지되어 있지 않다. 이 HTTP의 비연결성과 비상태성을 보완하여 서버가 클라이언트를 식별하게 해주는 것이 session이다.

The benefits of using web sessions are obvious: web sessions allow the website to have some form of "short-term memory" about a user's activity.

Having no memory of users at all would be extremely inconvenient. If an e-commerce website could not remember a user's actions, for example, users would have to place e-commerce orders all at once within a single action, rather than storing items in a shopping cart.



## vs. cookies

Web sessions are frequently compared to (and confused with) cookies. Although both cookies and web sessions store information about a user, their functions are different in practice.

Cookies are text files that are used to authenticate and track visitors to a website, and that are stored only on the user's machine. The lifespan of a cookie is typically much longer than that of a web session, on the order of months or even years. Cookies are how websites store long-term user information that should be preserved: for example, automatically logging the user in when arriving at the website, or automatically filling in a form with the user's details.

By contrast, web sessions are meant to store information about only the user's most recent activities. Web sessions are stored on the server rather than the client, which helps prevent malicious users from editing them. Both web sessions and cookies can be used in combination to keep track of users' long-term and short-term behavior.



## References

https://redisson.org/glossary/web-session.html (What is a Web Session?)

https://devuna.tistory.com/23 ([web] 쿠키(cookie)와 세션(session)의 개념/차이/용도/작동방식)

