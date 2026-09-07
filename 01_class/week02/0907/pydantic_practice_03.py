# 3. API 요청 → 검증 → 데이터 변환

from pydantic import BaseModel, Field


class SignupRequest(BaseModel):
    username: str = Field(min_length=3, max_length=20)  # username 문자 길이는 최소3-최대20자
    password: str = Field(min_length=8)  # password 문자 길이는 최대8자
    age: int = Field(ge=14)  # age 숫자 길이는 14보다 크거나 같다


def signup(data: SignupRequest):
    print("회원가입 처리")
    print(f"username: {data.username}")
    print(f"age: {data.age}")


request = SignupRequest(
    username="alice",
    password="12345678",
    age=25,
)

signup(request)

#---------------
# 회원가입 처리
# username: alice
# age: 25
#---------------
