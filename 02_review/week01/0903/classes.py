# 0903 클래스 오답노트 — 백지 타이핑용
# 이게 1주차에서 가장 중요한 파일. Pydantic(STEP 01) / LangGraph State(STEP 06) 전부 class 다.

# ─────────────────────────────────────────────
# [문제 1] 가장 작은 클래스
# x = 5 를 가진 MyClass 를 만들고, 객체 p1 을 만들어 p1.x 출력.

class MyClass:
    x = 5

p1 = MyClass()

print("=== 문제 1 ===")
print(p1.x)

# [답]
# 5
# 오답노트: 클래스명은 대문자로 시작(PascalCase:단어마다 첫 글자 대문자, 붙여쓰기), 객체(인스턴스)명은 소문자로 시작
# 문법적 강제는 아니고 관례. 이름만 보고 "이게 설계도(클래스)인지 물건(객체)인지" 구분하기 위함.
# 지키지 않아도 실행은 되지만, 남이 코드를 읽을 때 헷갈린다.
# ─────────────────────────────────────────────



# ─────────────────────────────────────────────
# [문제 2] __init__()
# Person 클래스: __init__(self, name, age) 로 이름·나이를 받는다.
# p1("홍길동", 16), p2("벤자민", 22), p3("세종대왕", 30) 을 만들고 p2 의 이름과 나이 출력.

class Person:
    def __init__(self, name, age):  # __init__()메서드 에서는 문법적으로 'self'가 맨 앞에 나와야함 (중간 또는 끝에 나오지않음) 
        self.name = name
        self.age = age

p1 = Person("홍길동", 16)
p2 = Person("벤자민", 22)
p3 = Person("세종대왕", 30)

print("=== 문제 2 ===")
print(p2.name)
print(p2.age)


# [답]
# 벤자민
# 22

# 오답 테스트A: _init_ (밑줄 1개씩) 으로 쓰면 무슨 일이 생기나?
# print("= 테스트A =")

# class Person:
#     def _init_(self, name, age):   # 앞,뒤로 '_'가 하나씩 있으면 그냥 평범한 함수. 클래스 자동 실행 안됨
#         self.name = name
#         self.age = age

# p1 = Person("홍길동", 16)    # 객체를 만드는 순간, 파이썬이 __init__이 있는지 찾음

# print(p1.name)

# 오답노트: _init_ (밑줄 1개씩)은 그냥 평범한 함수 이름이라 자동 실행되지 않는다.
# 자동 실행되는 건 __init__ (밑줄 2개씩, 앞뒤 4개)뿐
#
# [테스트 1] Person("홍길동", 16) 처럼 값을 넣어 만들면
#   -> TypeError: Person() takes no arguments
#   -> "만드는 자리"에서 바로 에러남. 원인을 즉시 알 수 있어 오히려 안전.
#
# [테스트 2] Person() 처럼 값 없이 만들면
#   -> 값을 쓰는 동안에는 에러를 확인할 수 없음 (__init__이 실행 안 됐으니 name, age가 애초에 안 생김)
#   -> 한참 뒤 print(p1.name) 출력을 실행하면 에러가 뜸
#      AttributeError: 'Person' object has no attribute 'name'
#   -> "문제가 생긴 자리(_init_ 오타)"와 "에러가 뜨는 자리(p1.name)"가 멀리 떨어져 있어서
#      원인을 찾기 훨씬 어렵다. 이게 "더 위험하다"의 뜻.
#
# 결론: 두 에러 다 뿌리는 같다(오타로 __init__이 자동실행 안 됨).
#   다만 TypeError는 원인 근처에서 바로 터지고, AttributeError는 한참 뒤에 터진다.
#
# [에러 메세지 읽는 법]
# 1)TypeError
# Traceback (most recent call last):          ← "지금부터 에러 경로를 보여줄게"
#   File "...", line 62, in <module>          ← 몇 번째 줄에서 문제가 시작됐나
#     print(p1.name)                          ← 그 줄의 실제 코드
# -> Traceback은 항상 여러 줄인데, 진짜 결론은 맨 마지막 줄의 "에러이름: 설명"이다.
#    위쪽 File, line 정보는 "어디서" 났는지 위치일 뿐, 항상 맨 아래부터 읽는다.
# 2)AttributeError	
# -> 이름(객체)은 있는데, 그 안의 속성이 없음
# (cf. p1.name — p1은 있지만 그 안에 name이 없음)
# AttributeError: 'Person' object has no attribute 'name'   ← 진짜 결론. 항상 맨 마지막 줄
# 3) NameError
# -> 그 이름(변수/함수 등) 자체가 어디에도 정의된 적이 없다는 뜻.
# print(self)     # self를 매개변수로 받은 적도, 어디서 만든 적도 없다면
# NameError: name 'self' is not defined
# 4)SyntaxError
# -> "문법이 틀렸다"는 큰 범주
# 5)IndentationError
# -> 문법 중에서도 "들여쓰기가 틀려서" 생긴 경우를 콕 집어 알려주는 것


# 오답 테스트B: self 를 빼고 def __init__(name, age) 로 쓰면 어떤 에러?
# print("= 테스트B =")

# class Person:
#     def __init__(name, age):   #self 빠짐
#         self.name = name
#         self.age = age

# p1 = Person("홍길동", 16)    

# print(p1.name)

# 오답노트: self는 직접 넣는 값이 아니라 객체를 만들 때 파이썬이 자동으로 넣어주는 값이다.
# def __init__(self, name, age): -> 자리 3개(self, name, age), 값 3개(p1, 홍길동, 16) = 딱 맞음
# def __init__(name, age):       -> 자리 2개(name, age)뿐인데 여전히 3개(p1, 홍길동, 16)가 들어오려 함 = 하나 초과
# -> TypeError: __init__() takes 2 positional arguments but 3 were given
# -> NameError(self가 없다는 에러)가 아니라 TypeError가 먼저 나 이유 
#    : 파이썬은 함수 안의 코드를 실행하기 전에, 먼저 "값이 자리에 맞게 들어왔는지"부터 확인하기 때문


# 오답 테스트C: __init__ 안에서 self.name = name 대신 name = name 을 쓰면?
# print("= 테스트C =")

# class Person:
#     def __init__(self, name, age):   #self 빠짐
#         name = name     # 이 줄은 문제 있음    
#         self.age = age  # 이 줄은 정상

# p1 = Person("홍길동", 16)    

# print(p1.name)

# 오답노트: 
#
# [테스트 1] print(p1.name) 
#   -> p1.name을 확인하면 'name'이 없다고 에러 뜸
#      AttributeError: 'Person' object has no attribute 'name'
#
# [테스트 2] print(p1.age) 
#   -> p1.age만 확인하면 정상으로 '16'출력됨
#   -> 파이썬은 name = name 처럼 "안 쓰이는 잘못된 코드"를 미리 경고해주지 않는다.
#      실제로 그 값을 사용하는 순간에만 문제가 드러난다.
# ─────────────────────────────────────────────



# ─────────────────────────────────────────────
# [문제 3] pass 와 나중에 속성 붙이기
# 내용이 비어있는 Person 클래스를 pass 로 만들고, p1 을 만든 뒤
# p1.name = "Tobias", p1.age = 25, p1.eye = "blue" 를 붙여서 세 개 출력. -> 속성을 붙여서 '나란히 옆으로 붙이라는 뜻X'

# 답안1
class Person:
    pass

p1 = Person()   # 반드시 들어가야하는 부분. 답안 작성시 해당 코드가 없었지만 에러 없이 출력됨. 위 어딘가에서 p1을 썼기 때문.

p1.name = "Tobias"
p1.age = 25
p1.eye = "blue"


print("= 답1 =")
print(p1.name)
print(p1.age)
print(p1.eye)

print()

# 답안2

class Person:
    pass

p1 = Person()

p1.name = "Tobias"
p1.age = 25
p1.eye = "blue"

print("= 답3 =")
print(p1.name, p1.age, p1.eye)

# 다른 표기 방법
print(p1.name,"," ,p1.age,"," ,p1.eye)
print(p1.name, p1.age, p1.eye, sep=", ")
print(f"{p1.name}, {p1.age}, {p1.eye}")

# 오답노트: 답안1, 답안2에서 p1 = Person()을 빠뜨렸는데도 에러가 안남.
# 이유: 파일 앞부분(문제 1, self 실험 등)에서 이미 p1 = ... 로 만들어둔 게 남아있었기 때문
# -> 그 "재활용된 p1"에 새 속성이 붙은 것뿐(우연히 위에 있던 변수가 대신 받음), 제대로 돌아간게 아님 
# -> 한 파일 안에서 변수 이름을 계속 재사용하면, 실수로 빠뜨린 코드가 있어도 에러 없이 넘어가는 위험한 상황이 생길 수 있음
# -> [문제3] 아래 del p1 로 강제로 지운 뒤 다시 실행하면 진짜 NameError가 뜸 (문제 1~2에서 쓰인 p1을 지웠기 때문)
#    del p1    #p1을 강제로 지워버림

# 답안3
class Person:
    pass

p1 = Person()

name = "Tobias"
age = 25
eye = "blue"

print("= 답2 =")
print(name, age, eye)
#print(p1.name)   ->에러남! p1 안에는 name이라는 속성이 없으니까

print()

# 오답노트: 답은 나왔으나, 클래스를 코드로 넣었지만 적용은 안됨
# name, age, eye가 그냥 독립된 변수라서, p1 = Person()d이 있더라도 p1 객체와는 아무 상관이 없음
# '객체에 속성 붙이기'가 아니라 '변수 3개 만들기'가 되버림

# [답]
# Tobias
# 25
# blue
# 오답노트: pass 를 안 쓰면 왜 에러인가?
#   -> class(또는 for/if/def 등) 뒤 콜론(:) 다음에는 들여쓰기된 "body (본문)=block (블록)"이 반드시 있어야 함. 문법 규칙 때문
#   -> 블록이 아예 없으면 IndentationError 들여쓰기 에러처리 됨.
#   -> pass는 "아무 일도 안 하지만 블록 자리를 채워서" 이 규칙만 만족시키는 용도.

# 오답노트 : p1 = Person() 에서는 반드시 빈 괄호이여야 함
# pass로 클래스를 만들면 객체 속성의 값'()'은 비워둬야함 // 속성을 미리 정해두는__init__이 없기 때문
# -> 나중에 속성 붙이기 방식은 유연하지만, 오타를 내도 쓰는 동안에는 에러가 안 난다
# (p1.nmae = "홍길동"처럼 오타를 내도 그냥 새 속성이 생겨버림) : 읽지 않았거나 출력을 하지 않는 등 실행을 하지 않았기 때문
#
# __init__ 방식은 "이 객체가 반드시 가져야 할 속성"을 미리 정해두는 것.
# 객체를 만드는 순간 개수/이름이 틀리면 바로 에러가 나서 더 안전하다.
# -> 이게 실무에서 __init__을 훨씬 많이 쓰는 이유.
#
# [에러가 난다 Vs. 에러가 안난다 - 기준] 
# 출력(print) < 실행(run) : 출력은 실행 중 일어나는 여러 동작 중 하나일 뿐
# 에러가 나느냐 안 나느냐의 진짜 기준은 "읽기냐 쓰기냐"다.
# 쓰기(객체.속성 = 값)  -> 항상 성공. 없으면 새로 만듦. 오타여도 티가 안 남.
# 읽기(객체.속성, print든 변수 대입이든 상관없이)  -> 이전에 쓰여진 코드가 실제로 있어야만 성공.
# 없으면 AttributeError. 
# -> print를 안 써도, x = p1.name 처럼 그냥 읽기만 해도 똑같이 에러난다.
#
print()
#
# [활용 문제]
# __init__()메서드
class Person:
    def __init__(self, name, age, eye):
        self.name = name
        self.age = age
        self.eye = eye

p1 = Person("Tobias", 25, "blue")

print("= 활용 답 =")
print(p1.eye)

# ─────────────────────────────────────────────



# ─────────────────────────────────────────────
# [문제 4] 메서드 2개
# 문제 2의 Person 에 greet(self) 와 display_info(self) 를 추가.
# p1("홍길동", 16), p2("벤자민", 22), p3("세종대왕", 30)
# greet: "Hello, my name is " + 이름 출력
# display_info: f-string 으로 "이름: ..., 나이: ..." 출력
# p2 로 name, age 출력 후 greet(), display_info() 호출.

# [1차 시도 실패]
# del p1 

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("홍길동", 16)
# p2 = Person("벤자민", 22)
# p3 = Person("세종대왕", 30)


# greet = "Hello, my name is ", "name"
# display_info = f"{"이름:", p2.name}, {"나이:", p2.age}"

# print("=== 문제 4 ===")
# print(p2.name)
# print(p2.age)
# print(greet, p2.name)   
# print(display_info)

# #[오답]
# 벤자민
# 22
# ('Hello, my name is ', 'name') 벤자민
# ('이름:', '벤자민'), ('나이:', 22)

# [2차 시도 실패]
# del p1 

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __init__(self, greet):
#         self.greet = greet
#         greet = print("Hello, my name is ", name)

#     def __init__(self, display_info):
#         self.display_info = display_info
#         greet = print(f"이름: {self.name}, 나이: {self.age}")

# p1 = Person("홍길동", 16)
# p2 = Person("벤자민", 22)
# p3 = Person("세종대왕", 30)

# print("=== 문제 4 ===")
# print(p2.name)
# print(p2.age)         
# print(p2.greet) 
# print(p2.display_info)

# [에러]
# Traceback (most recent call last):
#   File "/Users/hykim/Desktop/dev/hanwha_0902/02_review/week01/0903/classes.py", line 310, in <module>
#     p1 = Person("홍길동", 16)
#          ^^^^^^^^^^^^^^^^^^^^
# TypeError: Person.__init__() takes 2 positional arguments but 3 were given

del p1 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):    # ← 클래스 "안에" 함수로 추가
        print("Hello, my name is " + self.name)

    def display_info(self):    # ← 클래스 "안에" 함수로 추가
        print(f"이름: {self.name}, 나이: {self.age}")

p1 = Person("홍길동", 16)
p2 = Person("벤자민", 22)
p3 = Person("세종대왕", 30)

print("=== 문제 4 ===")
print(p2.name)
print(p2.age)         
p2.greet()    # 함수(메서드)이므로 괄호를 붙여서 "호출"        
p2.display_info()    # 함수(메서드)이므로 괄호를 붙여서 "호출"  

# [답]
# 벤자민
# 22
# Hello, my name is 벤자민
# 이름: 벤자민, 나이: 22
#
# 오답노트:
# greet, display_info를 클래스 밖에서 독립 변수로 만들면 안 됨.
#   클래스 "안에" def로 만들어야 메서드가 되고, self를 통해 그 객체의 name, age를 쓸 수 있다.
#   호출할 때도 변수처럼 그냥 쓰는 게 아니라 p2.greet()처럼 괄호를 붙여 "실행"해야 한다.
#   p2.greet() (괄호 있음) = 지금 실행해라
#   p2.greet (괄호 없음) = 함수 자체를 가리킴, 실행 안 됨
#
# p2.greet() 호출 시 self 자리
#   -> 파이썬이 내부적으로 greet(p2)로 바꿔 실행. self 자리에 p2(호출한 객체 자신)가 들어감.
#   -> 그래서 self.name은 실제로 p2.name을 가리킴.
#   -> p1.greet()을 부르면 이번엔 self 자리에 p1이 들어가서, 같은 코드라도 결과가 달라짐.
#
# 속성 vs 메서드
#   -> 속성(name, age): 값. 괄호 없이 씀.
#   -> 메서드(__init__, greet, display_info): 동작. 괄호 붙여서 씀. self가 항상 필요.
#
#__init__ vs greet/display_info ///중요///
#   1. __init__은 클래스당 딱 하나만 의미가 있다
#    같은 이름(__init__)으로 여러 개 만들면, 마지막에 쓴 것만 남고 앞의 것들은 덮어져서 사라짐
#    -> 2차시도 풀이에서 여러 개 만들었다가 실수했던 실험 참고
#   2. __init__이 "특별"한 이유
#    파이썬이 정확히 이 이름(__init__)만 미리 특별 취급하도록 정해둬서,
#    p1 = Person(...) 으로 객체를 만드는 순간 "자동으로" 실행된다.
#    (직접 p1.__init__(...) 이라고 부른 적이 없는데도 실행됨)
#   3. greet, display_info는 특별대우가 없다
#    이름이 평범해서 파이썬이 자동 실행해주지 않고,
#    p2.greet() 처럼 "직접 불러야만" 실행된다.
# 결론: 메서드는 "자동실행 메서드(__init__)" vs "직접호출 메서드(greet, display_info 등)"로 나뉨
#    __init__ = 객체가 생성될 때 한 번 실행되는 자리 (초기 데이터 설정 전용)
#    greet, display_info = "나중에 하고 싶은 동작"이므로, __init__ 안에 넣지 말고
#    완전히 새로운 이름의 메서드로 따로 만들어야 한다.  (cf. def greet(self): 형태로)
#
# print(p2.greet) 괄호 없음 vs print(p2.greet()) 괄호 있음
#   -> 괄호 없으면 "함수 자체를 가리키는 이상한 문구"만 나오고 실행 안 됨.
#   -> 괄호 있으면 진짜 실행되고, return이 없으면 그 결과(None)까지 출력됨.
#
# p2.greet()가 print 없이도 출력되는 이유
#   -> greet 함수 "안에" 이미 print가 들어있어서, 함수를 부르는 것 자체가 그 print를 실행시킴.
#   -> print(p2.greet())로 감싸면:
#      ① 안의 print가 먼저 찍힘 (Hello, my name is 벤자민)
#      ② greet()에 return이 없어 자동으로 None을 돌려줌
#      ③ 바깥 print가 그 None을 받아 한 줄 더 찍음
#
# print(p2.greet())는 결과적으로 항상 2줄이 나온다 (None만 단독으로 나오는 게 아님).
#   1번째 줄: greet() 함수가 실행되며 그 "안의" print가 찍는 것 (무조건 일어남, 없어지지 않음)
#   2번째 줄: greet()이 돌려준 결과값(return이 없어서 None)을 "바깥" print가 별도로 찍는 것
#   -> 안쪽 실행과 바깥쪽 실행은 서로 대체되는 게 아니라 "누적"된다.
#   -> 결과: 두 줄이 나온다 (안쪽 실행 + None 둘 다, 서로 대체 아니고 누적됨)
#   -> 0902/syntax.py 문제 1의 myfunc() 예제와 완전히 동일한 패턴.
#      (return 없는 함수를 print()로 한 번 더 감싸면 항상 "실행결과 + None" 2줄이 나온다)
#
# print와 return은 완전히 다른 일을 한다.
#   print = 화면에 "보여주기"만 함. 함수 밖으로 아무것도 전달 안 함.
#   return = 함수를 호출한 곳으로 "값을 전달"함. 화면엔 안 보임.
#   화면에 뭔가 찍혔다고 해서 그게 자동으로 함수의 결과값(return 값)이 되는 게 아니다.
#   return이 아예 없으면, 파이썬은 규칙에 따라 자동으로 None을 결과값으로 정한다.
#   -> greet()는 print만 있고 return이 없어서, 결과값은 항상 None.
# ─────────────────────────────────────────────



# ─────────────────────────────────────────────
# [문제 5] 내 것으로 만들기 (노션에 없는 문제)
# 누보아 상품을 표현하는 Product 클래스: __init__(self, name, price)
# discount(self, rate) 메서드: price * (1 - rate) 를 return.
# 원피스 39000원, 코트 129000원을 만들고 원피스 20% 할인가 출력.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Discaount(self, rate):
    self.rate = rate
    return (price*(1-rate))

Product1 = ("원피스,", "39000원")
product2 = ("코트,", "29000원" )

print(원피스.discount(20))


    
# [답]
# 31200.0
# 오답노트: 이건 return 이 있고 greet 는 return 이 없다. 차이가 뭔가?
# ─────────────────────────────────────────────


