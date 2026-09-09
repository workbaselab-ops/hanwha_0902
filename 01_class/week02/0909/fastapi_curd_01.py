from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# http://127.0.0.1:8000/docs 에서도 확인 가능. FastAPI연결되어있어야함

# POST 요청으로 받을 데이터 구조 정의 (pydantic 모델 사용)
class User(BaseModel):
    name: str
    age: int
    hobby: str | None = None


# PUT 요청으로 받을 데이터 구조 정의 (pydantic 모델 사용)
class UserUpdate(BaseModel):
    name: str
    age: int
    hobby: str | None = None


# 임시DB1
users_db = {
    1:{"name": "김은영", "age": 37},
    2:{"name": "김희영", "age": 34},
    3:{"name": "김소영", "age": 29},

}

# 임시DB2
users_db2 = {
    1:{"name": "김은영", "age": 37, "hobby": "릴스만들기"},
    2:{"name": "김희영", "age": 34, "hobby": "드라이브"},
    3:{"name": "김소영", "age": 29, "hobby": "블로그쓰기"},

}


app = FastAPI()


# http://127.0.0.1:8000/
@app.get("/")
async def root():
    return{"message":"안녕!"}



# http://127.0.0.1:8000/signin
@app.get("/signin")
async def root():
    return{"message":"사용자님 반가워요."}



# http://127.0.0.1:8000/users/question
@app.get("/users/question")
async def read_user_me():
    return {"user_id": "궁금한걸 물어보세요."}



# http://127.0.0.1:8000/users/
# POST 요청
@app.post("/users/")
async def create_user(user:User):
    return{
        "message": "사용자가 생성되었습니다.",
        "name": user.name,
        "age": user.age,
        "hobby": user.hobby,
    }



# GET 요청
@app.get("/users/")
async def create_user(user:User):
    return{
        "message": "사용자가 생성되었습니다.",
        "name": user.name,
        "age": user.age,
        "hobby": user.hobby,
    }


# PUT 요청
@app.put("/users/")
async def update(user_id: int, user: UserUpdate):
    # 찾는 사용자가 임시DB2에 없을 경우
    if user_id not in users_db2:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")
    
    # 수정된 유저
    updated_data2 = user.model_dump()
    users_db2[user_id] = updated_data2

    return {
        "message": "사용자를 수정하였습니다.",
        "user_id": user_id,
        "name" : user.name,
        "age" : user.age,
        "hobby" : user.hobby,
    }


# http://127.0.0.1:8000/users/1      # 1 -> id값
# DELETE 요청
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    # 찾는 사용자가 임시DB에 없을 경우
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")

    # 삭제된 유저를 띄워라
    del_user = users_db.pop(user_id)

    return {
        "message": f"ID {user_id}사용자가 삭제되었습니다.",
        "delete reason": del_user
    }
