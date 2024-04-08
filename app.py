import streamlit as st
import pandas as pd

# review 데이터 불러오기
df = pd.read_csv('review.csv')

# n개의 무작위 샘플 추출
df_samples = df.sample(n=1)

st.title('English Quiz')  # 타이틀명 지정
st.write("")
st.write(df_samples)
if st.button("Reload"):
  st.experimental_rerun()
  

st.write("")
st.write("")
st.write('All Sentences for the Quiz')
st.write(df)
