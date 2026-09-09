from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 데이터형식
class UserSchema(BaseModel):
    name: str
    age: int
    hobby: str | None = None

users_db:dict[int, dict] = {}
id_counter = 1


# 생성 Create -> POST 요청
@app.post("/users/", status_code=201)
async def create_user(user:UserSchema):
    global id_counter
    new_user =  user.model_dump()
    new_user["id"] = id_counter

    users_db[id_counter] = new_user
    id_counter += 1    # id_counter = id_counter + 1

    # return users_db

# Swagger UI 실행시 
# http://127.0.0.1:8000/users/
# code=201
# Response body
# {
#   "1": {        
#     "name": "김희영",
#     "age": 34,
#     "hobby": "음악듣기",
#     "id": 1                    # 첫번째 실행시
#   },
#   "2": {
#     "name": "김희영",
#     "age": 34,
#     "hobby": "음악듣기",
#     "id": 2                    # 두번째 실행시
#   }
# }




# 조회 (전체)Read -> GET 요청
@app.get("/users/")
async def get_all_users():
    return {"message": "전체 목록 조회 완료", "data": list(users_db.values())}

# Swagger UI 실행시 
# http://127.0.0.1:8000/users/
# code=200
# Response body
# {
#   "message": "전체 목록 조회 완료",
#   "data": [
#     {
#       "name": "김은영",
#       "age": 37,
#       "hobby": "릴스만들기",
#       "id": 1
#     },
#     {
#       "name": "김희영",
#       "age": 34,
#       "hobby": "드라이브",
#       "id": 3
#     },
#     {
#       "name": "김소영",
#       "age": 29,
#       "hobby": "블로그글쓰기",
#       "id": 3
#     }
#   ]
# }



# 조회 (단일)Read -> GET 요청
@app.get("/user/{user_id}")
async def get_user(user_id:int):

    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다")

    return {"message":"단일 조회 완료", "data":users_db[user_id]}

# Swagger UI 실행시 
#http://127.0.0.1:8000/user/1
# code=200
# Response body
# {
#   "message": "단일 조회 완료",
#   "data": {
#     "name": "김은영",
#     "age": 37,
#     "hobby": "릴스만들기",
#     "id": 1
#   }
# }




# 수정 Update -> PUT 요청
@app.put("/user/{user_id}")
async def upate_user(user_id:int, user:UserSchema):

    if user_id not in users_db:
        raise HTTPException(status_cod=404, detail="사용자를 찾을 수 없습니다.")

    updated_date = user.model_dump()
    updated_date["id"] = user_id
    users_db[user_id] = updated_date

    return  {"message":"수정완료", "data":updated_date}

# Swagger UI 실행시 
#http://127.0.0.1:8000/user/1
# code=200
# Response body
# {
#   "message": "수정완료",
#   "data": {
#     "name": "김은영",
#     "age": 37,
#     "hobby": "AI랑대화하기",
#     "id": 1
#   }
# }




# 삭제 Delete -> DELETE 요청
@app.delete("/user/{user_id}")
async def delete_user(user_id:int):

    if user_id not in users_db:
        raise HTTPException(status_code="404", detail="사용자를 찾을 수 없습니다.")

    # 삭제된 유저를 띄워라
    delete_user = users_db.pop(user_id)

    return {
        "message": f"ID {user_id} 사용자가 삭제되었습니다.",
        "data": delete_user
    }

# Swagger UI 실행시 
#http://127.0.0.1:8000/user/3
# code=200
# Response body
# {
#   "message": "ID1사용자가 삭제되었습니다.",
#   "data": {
#     "name": "김소영",
#     "age": 29,
#     "hobby": "블로그쓰기",
#     "id": 3
#   }
# }
