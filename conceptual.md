### Conceptual Exercise

Answer the following questions below:

- What is RESTful routing?
Restful routing is utilizing GET, POST, PUT, PATCH, DELETE and CRUD actions like Create, Read, Update and Destroy together in a conventional pattern.
- What is a resource?
A resource is a representation of what the website's URL returns. It can be a file, JSON, or information. Once the resource is grabbed, the developer can decide what to do with it.
- When building a JSON API why do you not include routes to render a form that when submitted creates a new user?
There is no reason to use render or redirect because building a JSON API passes the information from the route to a JSON dictionary in postgrSQL via POST.
- What does idempotent mean? Which HTTP verbs are idempotent?
Idempotent means the results are the same no matter how many times its submitted, GET, PUT, PATCH, and DELETE are all idempotent because they will all return the same result when used 
- What is the difference between PUT and PATCH?
PUT updates a whole server while PATCH updates part of it
- What is one way encryption?
Hashing
- What is the purpose of a `salt` when hashing a password?
A salt adds some random characters into the hashed password so that it is much harder to distinguish the part that is the actual hashed password, thus making a bruteforce attack inefficient
- What is the purpose of the Bcrypt module?
To hash passwords so they can be stored
- What is the difference between authorization and authentication?
Authorizatiton is being allowed to something on a website where authentication is verifying who you are on a website