# Unfamiliar Territory

This document will have my notes for things I'm even just a little unsure on.

## PyDantic

Pydantic acts as a strict gatekeeper for our data, ensuring that untrusted inputs (like web forms, API requests, or database queries) perfectly match the format our application expects before we process them

Instead of writing standard Python classes, we build schemas that inherit from BaseModel and define our fields using Python type hints

### Example

```python
Example:
class User(BaseModel):
    id: int
    username: str

# Pydantic validates and parses this raw data automatically

raw_data = {
    "id": "777",          # Notice, the string gets converted to integer
    "username": "alice",
}

user = User(**raw_data)
print(user.id)  # 777 (This is now an integer, not a string)
```

## Async + Await
Python normally runs code synchronously, one line at a time, waiting for each to finish

async def + await is asynchronous I/O. 
It lets Python say: 
"I'm waiting for this network call, go handle other requests, and come back when the data arrives"

async with httpx.AsyncClient() creates an HTTP client that works asynchronously

The await on client.get(url) tells Python: "pause this function here, let other things run, resume when the HTTP response arrives.

The popular requests library is synchronous only, httpx is its async-capable replacement

Python's asyncio (which uvicorn + FastAPI run on) is a single-threaded event loop

It handles concurrency not with multiple threads, but by switching between tasks whenever one is waiting for I/O. This is the same model as JavaScript's event loop

## ref()

Vue's reactivity system needs to know when data changes so it can re-render. A plain let articles = [] is invisible to Vue. ref([]) wraps the array in a reactive container. When we set articles.value = newArray, Vue sees the change and updates the DOM.

The .value thing: When we access a ref inside script setup, we use .value. Inside template, Vue unwraps it automatically — we just write articles, not articles.value.

## Separation from components and api.ts

### Pros
- If we later change the backend URL (e.g. /api/v2/news/{country_code}), we change it in one place: api.ts Without this, we'd have to hunt through every component
- If we add an auth token header we add it once in api.ts, and every component automatically gets it
- Testing is easier, we can mock api.ts without touching component code.
- Components become "dumb" about network details. They just call fetchNews('gb') and get back typed data.

## Vite Proxy (Works without CORS errors?)

Our frontend runs on localhost:5173. Our backend runs on localhost:8000. 

These are different origins (different port = different origin). Browsers block cross-origin requests by default (this is the Same-Origin Policy, a browser security feature)

The Vite proxy sidesteps this entirely during development:
```ts
// vite.config.ts
server: {
  proxy: {
    '/news': { target: 'http://localhost:8000', changeOrigin: true }
  }
}
```

When our Vue code calls fetch('/news/us'), the browser sends that to localhost:5173/news/us (same origin, no CORS issue). 

Vite intercepts it and forwards it to localhost:8000/news/us on the server side. The browser never sees a cross-origin request

This is a reverse proxy pattern. In production (when deployed), our backend will be at a real URL, and we'll configure CORS middleware in FastAPI instead

## Regular Expressions (regex)
The validation pattern "^[a-z]{2}$" is a regex:

- ^ means "start of string"
- [a-z] means "any lowercase letter a through z"
- {2} means "exactly 2 of the previous"
- $ means "end of string"

