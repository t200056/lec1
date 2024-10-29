#스트림릿 불러오기
import streamlit as st

#  기계학습 모델 파일 로드(모델명 : logistic_regression_model.pkl)
import joblib
model = joblib.load('logistic_regression_model.pkl')

# 만든 모델로 테스트 데이터에 대해 예측하기
st._______('합불분류 지능 에이전트')

col1, col2 = st.columns(2)

with ______:
      st.subheader(' 1. 기계학습 모델 제작과정 ')
      st.write(' - 기계학습 알고리즘 : 로지스틱 회귀 ')
      st.write(' - 학습 데이터 출처 : https://www.kaggle.com/')
      st.write(' - 총 데이터 건 수: 30건')
      st.write(' - 훈련    데이터 : 21건')
      st.write(' - 테스트 데이터 : 9건')
with _____:
      st.subheader('2. 기계학습 모델 평가')
      st.______('chart.png')   # 이미지 불러오기

st.subheader('3. 지능 에이전트 활용 방법 ')
st.write('**** 공부시간을 입력하세요.. 인공지능이 당신의 합격/불합격 분류 결과를 알려드립니다!')

# 사용자 입력
a = st.____________("공부시간", value=____)

# 예측 버튼 만들기
if st.________("인공지능의 분류 결과"):
        input_data = [[a]]
        p = model.predict(input_data)
         # 단순 조건문으로 예측 결과 출력
        if p[0] == 1:
              st.success('인공지능 분류 결과는 합격입니다........... 그러나, 방심은 금물입니다!')
        else:
              st.success('인공지능 분류 결과는 불합격입니다.......... 더 열심히 공부하면 됩니다!')
