from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

user = User(
    name="Alice",
    age="25",
    email="alice@example.com",
)

print(user)
print(user.age)
print(type(user.age))

#---------------
# name=Alice age=25 email=alice@example.com
# 25
# <class 'int'>   # python에서 type 객체 출력 방식
#---------------
 

# 1. print(user)에서 왜 'Alice'처럼 따옴표가 붙을까?
# ' '는 실제 문자열에 포함된 문자가 아닙니다.
# Pydantic이 User 객체를 출력할 때, 
# 문자열이라는 것을 알아보기 쉽게 표현(representation) 해주는 것입니다.
# -> print(repr(name)) -> 'Alice'