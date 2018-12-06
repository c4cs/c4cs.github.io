---
permalink: /lectures/f18/rest-api.html
---

class: center, middle

# Introducing REST APIs

.copyright[
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>
** [Pat Pannuto](http://patpannuto.com) / Tarun Khubchandani **
]


---

# What is REST?

--

## REpresentational State Transfer

--

### Six Basic Characteristics

--

  - Separation between client and server
  - Self contained requests (stateless)
  - Cacheable
  - Layered architecture to allow intermediaries
  - Uniform method of communication between client and server
  - (Optional) Code on Demand

--

### Core Ideas
  - Communicate with Application Resources
  - Generally uses HTTP Requests

---

# HTTP Requests and REST

--

## Ways to Modify Resources in REST
You may recognize these as operations from relational databases...
  - Create
  - Retrieve
  - Update
  - Delete

--

## HTTP Requests

| HTTP Request   |  Action                                           |
| --------- | ------------------------------------------------------ |
|  `POST`   |  Create an item/send information                       |
|  `GET`    |  Retrieve items from the server                        |
|  `PUT`    |  Update a resource                                     |
|  `DELETE` |  Remove a resource                                     |
| --------- | ------------------------------------------------------ |

---

# Cool. Why should I care?

--

## Flexible
  - Unlike SOAP, not just contained to XML
  - Allows easy integration with external tools

--

## Easy to Build/Use

  - Pretty uniform once you know the basics
  - Lots of frameworks to help you out (we're going to use Flask)
  - Extremely scalable and lightweight

--

## It's Fun!
### Most of the services you use have an API that can be used to do cool things!

---

class: center, middle
# Enough talking.
# Let's do something cool.

Grab a copy of the [starter code](https://github.com/tarunsk/eecs398-flask-sample).
