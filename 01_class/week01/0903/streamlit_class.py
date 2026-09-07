# [참고] 강사님 수업 원본 코드. 오답노트는 02_review/week01/0903/streamlit_review.py 참고


# import streamlit as st
# import pandas as pd

# df = pd.DataFrame({
#     'first colum' : [1, 2, 3, 4],
#     'second colum' : [10, 20, 30, 40]
# })
# df

# st.write("반가워 스트림릿")




# import streamlit as st
# import pandas as pd

# df = pd.DataFrame({
#     'first colum' : [1, 2, 3, 4],
#     'second colum' : [10, 20, 30, 40]
# })
# df

# st.write(df)

# st.write("반가워 스트림릿")




# import streamlit as st
# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     'first colum' : [1, 2, 3, 4],
#     'second colum' : [10, 20, 30, 40]
# })
# # df

# st.write(df)

# dataframe = np.random.randn(10, 20)
# st.dataframe(dataframe)

# st.write("반가워 스트림릿")





# 개별토스트 st.toast()를 매번 독립적으로 3번 호출
# import time
# import streamlit as st

# if st.button("Cook breakfast"):
#     st.toast("Gathering ingredients...")
#     time.sleep(1)
#     st.toast("Cooking...")
#     time.sleep(1)
#     st.toast("Ready!", icon="🥞")




# # 기존변수(msg)를 지정 호출하여 독립적으로 3번 호출
# import time
# import streamlit as st

# # 함수 정의 (def)
# def cook_breakfast():
#     st.toast("Gathering ingredients...")
#     time.sleep(1)
#     st.toast("Cooking...")
#     time.sleep(1)
#     st.toast("Ready!", icon="🥞")

# # 버튼 클릭 시 함수 호출
# if st.button("Cook breakfast"):
#     cook_breakfast()



# # 기존변수(msg)를 지정 호출하여 새 알림창이 아닌, 1개의 알림 창 내용만 바꾸기
# import time
# import streamlit as st

# def cook_breakfast():
#     msg = st.toast("Gat")
#     time.sleep(1)
#     msg.toast("Cooking...")
#     time.sleep(1)
#     msg.toast("Ready!", icon="🥞")

# if st.button("Cook breakfast"):
#     cook_breakfast()



#스트림릿 st.empty()를 사용
import time
import streamlit as st

def cook_breakfast():
    msg = st.empty()

    msg.info("🥕 Gathering ingredients...")
    time.sleep(1)

    msg.info("🍳 Cooking...")
    time.sleep(1)

    msg.success("🥞 Ready!")

if st.button("Cook breakfast"):
    cook_breakfast()

