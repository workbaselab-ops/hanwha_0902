# 2. 실전: 기본값, Optional, 중첩 모델
# Pydantic 모델 안에 또 다른 Pydantic 모델이 들어가 있으면 중첩 모델이다.

from pydantic import BaseModel, Field

class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    name: str
    age: int = Field(ge=0, le=150)      # Field()는 Pydantic에서 필드에 추가적인 조건이나 설정을 지정할 때 사용
    email: str
    address: Address                    # address라는 필드는 Address 타입이다.라는 뜻
    nickname: str | None = None

user = User(
    name="Alice",
    age=25,
    email="alice@example.com",
    address={                            # { }는 Python에서 딕셔너리(dictionary) 를 만들 때 사용하는 문법
        "city": "Daejeon",
        "zip_code": "34100",
    },
)

print(user)
print(user.address.city)
print(user.nickname)

#---------------
# neme='Alice' age=25 email='alice@example.com' address=Adress(city='Daejeon', zip_code='34100') nicknam='None'
# Daejeon
# None
#---------------
 

# 1. Adree안에 왜 (city='Daejeon') 모양으로 들어올까?
# Pydantic이 딕셔너리를 Address 모델로 변환한 뒤, 그 모델 객체의 출력 표현 방식이 =를 사용하는 것입니다.
# 딕셔너리 입력
# {
#     "city": "Daejeon",
#     "zip_code": "34100"
# }
#         ↓
#    Pydantic 변환
#         ↓
# Address 객체
#         ↓
# 출력 표현
# Address(city='Daejeon', zip_code='34100')

# 2. age: int = Field(ge=0, le=150)는 무슨 뜻인가?
# Field()는 Pydantic에서 필드에 추가적인 조건이나 설정을 지정할 때 사용 
# -> Pydantic 모델의 각 필드에 "추가 검증 조건"을 붙이는 기능
# 'ge'는 greater than or equal to의 약자
# ge=0 : 0보다 크거나 같아야 한다.
# le는 less than or equal to의 약자
# le=150 : 150보다 작거나 같아야한다.
# 따라서, age: int = Field(ge=0, le=150) -> age는 정수이고, 0 이상 150 이하만 허용한다는 뜻 = 0 ≤ age ≤ 150

# 자주 쓰는 Field 조건
# | 조건       | 의미           |
# | -------- | ------------ |
# | `ge=0`   | 0 이상 (`≥`)   |
# | `gt=0`   | 0 초과 (`>`)   |
# | `le=150` | 150 이하 (`≤`) |
# | `lt=150` | 150 미만 (`<`) |
