# streamlit 라이브러리 불러오기
import streamlit as st

st.title('수학 ㅁㅇㄻㄴㅇ학습 보조 프로그램')                       # 제목 쓰기

st.subheader('양수음수 판별기')         # 부제목 쓰기

st.write('음수를 아시나요?')                  # 본문 쓰기

col1, col2 = st.columns(2)       # 여러 개의 열(문단)을 생성
with col1:
       st.write('0보다 큰 수는 양수')
with col2:
       st.write('0보다 작은 수는 음수')

st.image( 'chart (1).png' )              # 이미지 불러오기

a = st.number_input('수를 입력하세요', min_value=0)   # 사용자의 입력을 받아서 a에 저장하기(최소값은 0)

if a > 0:
       st.write('양수입니다')
elif a<0:
       st.write('음수입니다')
else:
        st.write('0입니다')
