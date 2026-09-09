
from fastapi import FastAPI

app = FastAPI()


# >>>>>>>>>>>>>>>>
# //채워 놓아야 할 것들//
# 쿼리 매개변수 일부 빠짐
# <<<<<<<<<<<<<<<<


# http://localhost:8000/items/test    # 경로뒤에 /test 추가
# http://localhost:8000/items/{test}
# http://localhost:8000/items/{test}?
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q" : q}
    return {"item_id": item_id}
