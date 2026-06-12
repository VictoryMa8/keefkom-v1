from fastapi import FastAPI

app = FastAPI()

# When we want to make a query parameter required, we can just not declare any default value:
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item