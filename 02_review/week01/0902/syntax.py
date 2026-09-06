# 0902 파이썬 문법 오답노트 — 백지 타이핑용
# 규칙: 수업 노트를 보지 않고 [문제]만 읽고 코드를 친다. 출력이 [답]과 같으면 통과.
#       막히면 그때 노션을 보고, 다시 덮고, 다시 친다. 린 건 # 오답: 으로 이유를 적는틀다.
# 실행: python syntax.py

# ─────────────────────────────────────────────
# [문제 1] 전역변수와 지역변수
# x = "awesome" 을 전역으로 두고, 함수 안에서 x = "fantastic" 을 만든 뒤
# 함수 안에서 한 번, 함수 밖에서 한 번 "Python is ..." 를 출력한다.

x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is", x)

print("=== 문제 1 ===")
myfunc()
print("Python is", x)

# [답]
# Python is fantastic
# Python is awesome
# 오답노트 :
# 1. def는 실행이 아니라 함수를 정의하는 것.
# 2. 함수 안에서 x = "fantastic" 은 지역변수 x 를 만든 것. 전역변수 x 는 바뀌지 않음. 이름만 같고 다른 변수.
#    함수 안에서 바꿔도 밖의 x는 그대로다.
# 3. my fun()에는 retuyrn이 없어서 자동으로 None을 돌려줌
#    print(myfunc())를 하면 'Python is None' 출력 // 이유: 함수 한 print + 함수 밖 print, 두 번 실행됐기 때문

# [확장] return 사용하기

x = "awesome"
def myfunc():
    x = "fantastic"
    return x

print("=== 문제 1 확장 ===")
print("Python is", myfunc())
print("Python is", x)

#[답]
# Python is fantastic
# Python is awesome
# 오답노트: print(myfunc())의 문제를 고치는 두 가지 방법
#   방법1 (그냥 부르기): print를 그대로 두고, myfunc()을 print로 감싸지 않고 단독으로 호출.
#      -> myfunc() - 함수 안의 print가 그대로 한 번만 찍힘. 원본 실수(이중 print)만 정확히 고친 것.
#   방법2 (return으로 바꾸기): 함수 안의 print를 return으로 바꾸고, 바깥에서 print(myfunc())로 감쌈.
#      -> print("Python is", x) - return한 값을 바깥 print가 한 번만 찍음. 함수 설계 자체를 다르게 바꾼 것.
# 결론: 
#   둘 다 한 줄만 나오지만, 방법1은 "함수는 원래 그대로 두고 부르는 방식만 고친 것"이고
#   방법2는 "함수 내부 설계(print→return)를 바꾼 것"이라는 차이가 있다.
# ─────────────────────────────────────────────



# ─────────────────────────────────────────────
# [문제 2] global 키워드
# 문제 1과 같은데, 함수 안에서 global 을 써서 전역 x 자체를 바꾼다.
# 함수 호출 후 함수 밖에서 출력.

x = "awesome"

def myfunc():
    global x                 # global x = "fantastic" 글로벌 키워드는 한 줄로 쓰지 않음 '약속'
    x = "fantastic"
    print("Python is", x)

print("=== 문제 2 ===")
myfunc()
print("Python is", x)

# [답]
# Python is fantastic
# 오답노트: global x = "fantastic" 처럼 한 줄로 쓰면 왜 에러인가?
# 전역함수인 global x 는 한줄로 쓰지 않음
# ─────────────────────────────────────────────



# ─────────────────────────────────────────────
# [문제 3] 문자열 인덱스
# a = "Hello, World!" 에서 두 번째 글자를 출력.

a = "Hello, World!"
print("=== 문제 3 ===")
print(a[1])

# [답]
# e
# 오답노트: 왜 a[2]가 아니라 a[1]인가?
# 문자열 인덱스는 0부터 시작한다. H=0, e=1, l=2, l=3, o=4, ... , !=12
# 1번째 문자가 '0'번째 '위치'
# 0,1,2,3,...으로 셈   
# ─────────────────────────────────────────────



# ─────────────────────────────────────────────
# [문제 4] for 루프
# fruits = ["apple", "banana", "cherry"] 를 한 줄씩 출력.

print("=== 문제 4 ===")

fruits = ["apple", "banana", "cherry"]    # 리스트 정의를 명확하게 하기

for fruit in fruits:                      # for 단수 in 복수
    print(fruit)

print()    # 빈 줄 출력

# 답은 나오지만 for 단수 in 복수 형태로 쓰기 연습
x = ["apple", "banana", "cherry"]

for item in x:     # "하나씩"이라는 뜻으로 그냥 item
    print(item)

# [답]
# apple
# banana
# cherry
# 오답노트: print 앞에 들여쓰기를 안 하면 어떤 에러가 나는가?
# 들여쓰기 된 블록이 없다는 에러가 뜸 'IndentationError: expected an indented block'
# for 루프 안쪽에 있는 것에만 indentation[인덴테이션 들여쓰기(Tab)] 영향을 받아서 출력된다.
# 반복하지 않을 때는 for 루프 밖에 print를 써야함.
#
# [오답예시] : list 자체를 x로 정의하면 안되는 이유
# x = ["apple", "banana", "cherry"]
# for x in ["apple", "banana", "cherry"]:  -> for x in x 가 되어버림. 따라서 x는 '하나씩' 덮어써짐
#     print(x)
# print(len(x))  -> 3이 아니라 1이 나옴. 
# 이유: for 루프에서 x가 반복 끝난 뒤 x가 "마지막 항목 하나"로 바뀌어버려 마지막 'cherry'만 남기때문에 len(x) = 1
# ─────────────────────────────────────────────



# ─────────────────────────────────────────────
# [문제 5] 함수 선언 + return
# 화씨(f)를 섭씨로 바꾸는 함수 cel(f) 를 만들고 cel(77) 출력.
# 공식: (f - 32) * 5/9

def cel(f):
    return (f - 32) * 5/9

print("=== 문제 5 ===")
print(cel(77))

# [답]
# 25.0
# 오답노트: return 뒤에 스페이스 없이 (f - 32)를 붙여도 실행은 되지만,
# 보통 return (f - 32) * 5/9 처럼 스페이스를 넣는 게 관례다.
# ─────────────────────────────────────────────



# ─────────────────────────────────────────────
# [문제 6] 함수 4개 (사칙연산)
# f1~f4 가 각각 su + 100, su - 100, su * 100, su / 100 을 return.
# 5를 넣어 4개 출력.

def f1(su):
    return su + 100
def f2(su):
    return su - 100
def f3(su):
    return su * 100
def f4(su):
    return su / 100

print("=== 문제 6 ===")
print(f1(5))
print(f1(10))    # su를 함수정의 내에서 괄호 안에 넣으면 출력 값이 달라도 코드 수정없이 값을 뽑을 수 있음
print(f2(5))
print(f3(5))
print(f4(5))

# [답]
# 105
# -95
# 500
# 0.05
# 오답노트: 
# f1()처럼 괄호를 비우고 함수 밖에서 su를 그대로 쓰는것 : su 값을 바꾸려면 코드 위쪽을 고쳐야함
# f1((su))처럼 괄호안에 값을 받아쓰는 것의 차이 : 원하는 다른 값을 바로 넣을 수 있음
#
# [오답예시] : su 자체를 5로 정의하면 안되는 이유

# su = 5

# def f1():
#     return su + 100
# def f2():
#     return su - 100
# def f3():
#     return su * 100
# def f4():
#     return su / 100

# print(f1())
# print(f2())
# print(f3())
# print(f4())
# 이유: 함수 밖(전역)에서 su를 5로 정의하면, 함수 안에서 su를 바꾸지 못하고 전역변수 su = 5만 계속 쓰게 된다.
# 변수를 바꾸려면 su를 찾아서 다시 정의해야함.
# ─────────────────────────────────────────────



# ─────────────────────────────────────────────
# [문제 7] 개인 실습 — 리스트 + for 로 줄이기
# 제목 "AI 서비스 백엔드 프로그래밍 실무", 구분선 "===========" 출력 후
# ["파이썬 기본 문법", "클래스", "데코레이터", "예외 처리", "로깅"] 각각을
# "항목 , 시간 : 8" 형태로 출력. print 를 5번 쓰지 말고 for 한 번으로.

title = "AI 서비스 백엔드 프로그래밍 실무"
topics = ["파이썬 기본 문법", "클래스", "데코레이터", "예외 처리", "로깅"]
time = 8

print("=== 문제 7 ===")
print(title)
print("===========")

for topic in topics:
     print(topic, time, sep=", 시간 : ") 

# [답]
# AI 서비스 백엔드 프로그래밍 실무
# ===========
# 파이썬 기본 문법, 시간 8
# 클래스, 시간 8
# ...
# 오답노트: sep은 구분자(separator)로 print() 안에 콤파 사이사이를 뭘로 붙일지 정하는 옵션
# print(topic, time, sep=", 시간 : ") -> sep은 항상 맨 뒤에 와야 한다.
# 순서를 바꾸면 에러남 -> print(topic, sep=", 시간 : ", time)
# topic, 시간 : time (cf. 로깅, 시간 : 8)
# [쉬운 예시]
# print("A", "B")            # A B   ← 사이에 기본 공백
# print("A", "B", sep="-")   # A-B  ← 공백 대신 "-"
# ─────────────────────────────────────────────
# 테스트 3가지

print("= 테스트A =")
title = "AI 서비스 백엔드 프로그래밍 실무"
topics = ["파이썬 기본 문법", "클래스", "데코레이터", "예외 처리", "로깅"]
time = 8
a = "파이썬 기본 문법, 시간"

print(title)
print("===========")

for topic in topics:
    print(topic, ", 시간:", time)    # 콤마로 구분한 걸 전부 띄어쓰기로 이어서 출력 (cf. 로깅 , 8시간)

print()

print("= 테스트B(f-string) =")
title = "AI 서비스 백엔드 프로그래밍 실무"
topics = ["파이썬 기본 문법", "클래스", "데코레이터", "예외 처리", "로깅"]
time = 8

print(title)
print("===========")

for topic in topics:
    print(f"{topic}, 시간 : {time}")    

print()

print("= 테스트C(f-string) =")
title = "AI 서비스 백엔드 프로그래밍 실무"
topics = ["파이썬 기본 문법", "클래스", "데코레이터", "예외 처리", "로깅"]

for topic in topics:
    print(f"{topic}, 시간 : 8")


# 오답노트: [테스트 B vs.C]
# 둘다 f-string을 사용하지만 값의 형태에 따라 다름
# f-string 안에 값을 변수로 넣을지({time}) 직접 써넣을지(8) 차이.
# 변수(time)로 두면 한 곳만 고치면 전체가 바뀜 -> 값이 바뀔 가능성 있으면 변수 사용(figma > component 라고 이해하면 쉬움) -> 일반적이며 안전
# 숫자(8)를 코드 여기저기 직접 박아두는 걸 "매직 넘버"라 부르며 좋지 않은 습관으로 본다. 




