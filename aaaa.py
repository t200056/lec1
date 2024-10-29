# streamlit 라이브러리 불러오기
import streamlit as st

st.title('동생아 수학 공부하자!')  # 제목 쓰기

st.subheader('오늘의 주제 : 양수와 음수') # 부제목 쓰기

st.write('음수?? 어렵지 않아!')                  # 본문 쓰기

col1, col2 = st.columns(2)       # 여러 개의 열(문단)을 생성
with col1:
       st.write('양수: 0보다 큰 수')
       st.write('음수: 0보다 작은 수')
       st.write('양수: (+) / 음수: (-) 부호가 붙음')
       st.write('부호: (+)는 생략 가능 /(-)는 생략 불가')
with col2:
       st.image( '수학이미지.png' )              # 이미지 불러오기

a = st.number_input('수를 입력하세요', min_value=-100000)   # 사용자의 입력을 받아서 a에 저장하기(최소값은 0)

if a > 0:
       st.write('양수입니다')
elif a<0:
       st.write('음수입니다')
else:
        st.write('0입니다')


import joblib
model = joblib.load('logistic_regression_model (1).pkl')

# 만든 모델로 테스트 데이터에 대해 예측하기
st.title('112233합불 분류 지능에이전트')

col1, col2 = st.columns(2)

with col1:
      st.subheader(' 1. 기계학습 모델 제작과정 ')
      st.write(' - 기계학습 알고리즘 : 로지스틱 회귀 ')
      st.write(' - 학습 데이터 출처 : https://www.kaggle.com/')
      st.write(' - 총 데이터 건 수: 30건')
      st.write(' - 훈련    데이터 : 21건')
      st.write(' - 테스트 데이터 : 9건')
with col2:
      st.subheader('2. 기계학습 모델 평가')
      image_path = 'chart (1).png' # 로컬 이미지 파일 경로
      st.image(image_path )   # 이미지 불러오기

st.subheader('3. 지능 에이전트 활용 방법 ')
st.write('**** 공부시간을 입력하세요.. 인공지능이 당신의 합격/불합격 분류 결과를 알려드립니다!')

# 사용자 입력
a = st.number_input("공부시간", min_value=0)

# 예측 버튼 만들기
if st.button("인공지능의 분류 결과"):
       input_data = [[a]]
       p = model.predict(input_data)
         # 단순 조건문으로 예측 결과 출력      
       if p[0] == 1:
              st.success('인공지능 분류 결과는 합격입니다........... 그러나, 방심은 금물입니다!')
       else:
              st.success('인공지능 분류 결과는 불합격입니다.......... 더 열심히 공부하면 됩니다!')
