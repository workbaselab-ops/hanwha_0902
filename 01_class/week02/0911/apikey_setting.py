# .env 파일에 저장해 둔 환경변수를 읽어오기 위한 함수
# 환경변수에 API Key를 직접 설정해 놓았다면 필요없음
from dotenv import load_dotenv

# OpenAI API를 사용하기 위한 OpenAI 클래스 가져오기
from openai import OpenAI


# .env 파일을 읽어서 환경변수로 등록
load_dotenv()


# 환경변수에 저장된 OPENAI_API_KEY를 자동으로 찾아서
# OpenAI와 연결할 수 있는 client 객체 생성
client = OpenAI()


# OpenAI에게 질문 보내기
response = client.responses.create(
    # 사용할 OpenAI 모델
    model="gpt-5-mini",

    # OpenAI에게 전달할 질문
    input="안녕하세요!"
)


# OpenAI가 보내준 답변 출력
print(response.output_text)