# 로컬 호스트 :  localhost:8000 = http://127.0.0.1:8000

# enum 열거형 : 서로 관련 있는 고정된 상수(값)들의 집합을 정의할 때 사용하는 데이터 타입
# api 문서에다가 경로별로 정리하는 것 중요 : 어디에 뭐가 있는지 확인 가능

from enum import Enum 
from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

app= FastAPI()

# http://127.0.0.1:8000/
@app.get("/")    # get("/"") get요청 /(슬러시:루트)는 local host 웹 경로
def read_root():
    return {"Hell" : "World"}


# http://127.0.0.1:8000/items/1    # 경로뒤에 /1 추가
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None=None):
    return {"item_id": item_id, "q": q}


# http://127.0.0.1:8000/user/me
@app.get("/user/me")
async def read_user_me():
    return {"user_id": "the current user"}


# http://127.0.0.1:8000/user/김희영
@app.get("/user/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


# http://127.0.0.1:8000/user/김희영
@app.get("/user/{user_id}")              # read_user2 실행안됨-> {"detail":"Not Found"} 뜸
async def read_user2(user_id: str):      # 이유: 경로상 상단 read_user가 먼저 매칭
    return {"user_id": user_id}          # 기본적으로 첫 번째 것이 항상 사용됨


# http://127.0.0.1:8000/users
@app.get("/users")
async def red_users():
    return ["Rick", "Morty" ]


# >>>>>>>>>>>>>>>>
# //채워 놓아야 할 것들//
# 경로 매개변수 일부 빠짐
# <<<<<<<<<<<<<<<<

# http://localhost:8000/items2/test    # 경로뒤에 /test 추가
# http://localhost:8000/items2/{test}
# http://localhost:8000/items2/{test}?
@app.get("/items2/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q" : q}
    return {"item_id": item_id}
