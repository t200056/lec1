# streamlit 라이브러리 불러오기
import streamlit as st

st.title('동생아 수학 공부하자!')  # 제목 쓰기

st.subheader('오늘의 주제:양수와 음수') # 부제목 쓰기

st.write('음수?? 어렵지 않아!')                  # 본문 쓰기

col1, col2 = st.columns(2)       # 여러 개의 열(문단)을 생성
with col1:
       st.subheader('**개념정리')
       st.write('-양수: 0보다 큰 수')
       st.write('-음수: 0보다 작은 수')
       st.write('-양수: (+) / 음수: (-) 부호가 붙음')
       st.write('-부호: (+)는 생략 가능 /(-)는 생략 불가')
with col2:
       st.image('수학이미지.png')                  # 이미지 불러오기

a = st.number_input('수를 입력하세요', value=0)   # 사용자의 입력을 받아서 a에 저장하기(초기값은 0)

if st.button("양수일까 음수일까?"):
       if a > 0:
              st.write('양수입니다')
       elif a<0:
              st.write('음수입니다')
       else:
              st.write('0입니다')

