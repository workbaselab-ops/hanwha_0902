questions = ["asyncio란?", "", "FastAPI란?"]
valid_questions: list[str] = []

for question in questions:

    # strip()은 문자열(string) 양쪽에 있는 공백(스페이스, 탭, 줄바꿈 등)을 제거해 주는 Python의 내장 문자열 메서드.
    cleaned = question.strip()
    if not cleaned:
        continue    # <--- cleaned가 빈 문자열("")이면, 이후 실행X, 3번째 요소를 실행.

    valid_questions.append(cleaned)

print(valid_questions)

#---------------
#
#---------------

# ['asyncio란?', 'FastAPI란?']




# 질문은 2가지 
# 유효성 리스트는 []안에 문자로 나열된다
# Cleanded는 질물 양쪽에

# 1.append가 무엇인가?

# 2.valid_questions: list[str] = []는 어떤 무엇을 쓰고, 출력시 어떻게 나오는가?



