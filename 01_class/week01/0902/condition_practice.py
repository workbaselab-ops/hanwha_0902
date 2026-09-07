questions = ["asyncio란?", "", "FastAPI란?"]
valid_questions: list[str] = []    # "문자열(str)을 담는 리스트"

for question in questions:

    # strip()은 문자열(string) 양쪽에 있는 공백(스페이스, 탭, 줄바꿈 등)을 제거해 주는 Python의 내장 문자열 메서드.
    cleaned = question.strip()
    if not cleaned:
        continue    # <--- cleaned가 빈 문자열("")이면, 이후 실행X, 3번째 요소를 실행.

    valid_questions.append(cleaned)
                    # append()는 리스트의 마지막에 값을 하나 추가하는 Python의 내장 리스트 메서드.
print(valid_questions)

#---------------
# ['asyncio란?', 'FastAPI란?']
#---------------


# ['asyncio란?, '', 'FastAPI란?', 'cleanded'] -> 총 4개

# 1. strip() // append() // continue 비교
# strip()   → 문자열(str) 메서드 : 앞뒤 공백 제거
# append()  → 리스트(list) 메서드 : 마지막에 값 추가
# continue  → 메서드가 아니라 반복문 제어문

# conticue는 주로 반복문(for, while)에서 이번 반복만 건너뛰고 다음 반복으로 넘어갈 때 사용
# -> "이번 차례는 건너뛰고 다음 차례로 가!
# continue = 이번 것만 패스하고 다음으로
# break    = 반복 자체를 그만