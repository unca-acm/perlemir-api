# Perlemir API Architecture

The API connecting all aspects of the Perlemir Algo-Bot application. 
This document notes the structure of the application, including the 
specific endpoints and the file structure.

## Process

There are only a couple endpoints that will be accessible without 
a session ID associated with a specific user's ID attached. All
other endpoints must be accessed with the session started, otherwise
there will be a **HTTP-401-UNAUTHORIZED** response code returned.

## Endpoints

The Endpoints for this project are all set up as routes in the 
perlemir_api.py file, but they are each defined in other groupings.
They are merely called in the route definitions, so that file size 
can be kept to a minimum for easy reading.

## Bot Endpoints

### **Bot List All Running** (#bot-list)
<h3><strong style="color:#FFD366;">GET /api/v1/bot</strong></h3>

Enumerate bots, returning a list of existing bots and their status.
Should include information to uniquely identify each bot.

### **Request**
`{site.domain}/api/v1/bot`

**Header**

**Body**

### **Response**
`200 OK`
```json
[ { “name”: “My First Bot”, “id”: “xyz-1”,
      “status”: “active” },
  { “name”: “My Second Bot”, “id”: “abc-3”,
    “status”: “inactive” }, ... ]
```

### **Bot Create** {#bot-create}
<h3><strong style="color:#FFD366;">POST /api/v1/bot/new</strong></h3>

Create a new instance of a trading bot, providing the bot’s initial 
settings as key-value pairs in the request body. Settings include 
things like the name, strategy, frequency, etc. Some will be universal, 
but specific bots/strategies will likely have their own specific settings.

### **Request**
`{site.domain}/api/v1/bot/new`

**Params**

| Key         | Value           | Description           |
| ----------- | --------------- | --------------------- |
| name        | bot name        | The name of the bot   |
| strategy    | dollar-cost-avg |   do                  |
| period      | weekly          |   do                  |

**Header**

**Body**
```json
{
    "name" : "bot name",
    "strategy" : "",
    "period": "",
    "frequency" : ""
}
```

### **Response**
`201 CREATED`
```json
{
    "id" : "xyz-123-abc",
    "status" : "active"
}
```

### Bot Query/Modifier Endpoints {#bot_modify}
<h3><strong style="color:#FFD366;">GET /api/v1/bot/{id}</strong></h3>

---

## User Endpoints
 
### User Creation {#user_create}
<h3><strong style="color:#FFD366;">GET /api/v1/user/create</strong></h3>

### User Deletion {#user_delete}
<h3><strong style="color:#FFD366;">GET /api/v1/user/delete</strong></h3>

### User Modification {#user_modify}
<h3><strong style="color:#FFD366;">GET /api/v1/user/modify</strong></h3>

### User Login {#user_login}
<h3><strong style="color:#FFD366;">GET /api/v1/user/login</strong></h3>

```json
{
    "uid" : "ladair",
    "pwd" : "$2y$12$P6UZTktamKQi3ROs2bYWOOwv4klzV55AYtQz1xmOyblInH83NLL2i",
    "nonce" : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MTMyNTkzNTEsImlhdCI6MTYxMzI1OTIwMX0.Ue-dTTgSHuJ3ZEshy9EWZD23QP243hrJLTqNBfgeOhw"
}
```

### User Logout {#user_logout}
<h3><strong style="color:#FFD366;">GET /api/v1/user/logout</strong></h3>

## Auxilliary Endpoints
<h3><strong style="color:#FFD366;">GET /api/v1/user/get_nonce</strong></h3>

---

## File Structure
```
📦perlemir-api
 ┣ 📂bot
 ┃ ┣ 📜bot.py
 ┃ ┗ 📜bot_fun.py
 ┣ 📂config
 ┃ ┣ 📂logs
 ┃ ┣ 📜config.py
 ┃ ┗ 📜database.py
 ┣ 📂objects
 ┃ ┗ 📜get-pip.py
 ┣ 📂ud
 ┃ ┗ 📜users.json
 ┣ 📂user
 ┃ ┗ 📜user_fun.py
 ┣ 📜LICENSE
 ┣ 📜README.md
 ┣ 📜architecture.md
 ┗ 📜perlemir_api.py
```