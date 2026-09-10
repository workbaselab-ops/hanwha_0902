import streamlit as st
import requests

#FastAPI 백엔드 URL                       
FASTAPT_URL = "http://127.0.0.1:8000"     # 서버주소는 바뀌지 않기 때문에 변수 이름을 상수(대문자)로 쓴다. = run타임동안 변수를 재정의를 하지 않겠다
                                         
st.title("Streamlit & FastAPI 연결 예제")

# 입력 폼 구성
with st.form("user_form"):
    name = st.text_input("이름", value="홍길동")  #defualt 값 없애는 방법 = ("이름")
    age = st.number_input("나이", value=20, min_value=1, max_value=120)
    submit_button = st.form_submit_button("백엔드로 전송")

if submit_button:
    # FastAPI로 보낼 데이터 페이로드
    payload = {
        "name" : name,
        "age" : age
    }

    try:
        # FastAPI /predict 엔드포인트에 POST 요청
        response = requests.post(f"{FASTAPT_URL}/predict", json=payload)

        if response.status_code == 200:
            result = response.json()
            st.success("FastAPI 응답 성공!")
            st.write(f"**결과:** {result['result_message']}")
        else:
            st.error(f"오류 발생 (상태코드: {response.status_code})")

    except requests.exceptions.ConnectionError:
        st.error("FastAPI 서버에 연결할 수 없습니다. 백엔드 서버가 실행 중인지 확인해 주세요.")
