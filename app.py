import streamlit as st
import pandas as pd
from gtts import gTTS
import io
from io import BytesIO
import os
from pydub import AudioSegment

password_input = st.text_input("암호를 입력해주세요",type= "password")

if password_input == "cmcpl":
  # review 데이터 불러오기
  dataframe = pd.read_csv('review.csv')


  # Create Radio Buttons
  topic=st.radio(label = '학습 주제선택', options = ['모두', '직장인을 위한 영어패턴1-25', '미국 직장인이 매일 쓰는 영어 100문장', '원어민이 가장 많이 쓰는 구동사 30개', '일상 영어 회화 패턴 20개', '회사에서 지겹도록 듣게되는 영어 문장 40개', '비즈니스 이메일 핵심패턴 15개'])

  st.write("")
  if st.checkbox('반복재생'):
    loop = True   
  else:
    loop = False
    
  if topic == '모두':
    selected_topics =  ['직장인을 위한 영어패턴1-25', '미국 직장인이 매일 쓰는 영어 100문장', '원어민이 가장 많이 쓰는 구동사 30개', '일상 영어 회화 패턴 20개', '회사에서 지겹도록 듣게되는 영어 문장 40개', '비즈니스 이메일 핵심패턴 15개']
    st.write("모든 문장 듣기")
    st.audio('combined_all_6.m4a', loop = loop)
  elif topic == '직장인을 위한 영어패턴1-25':
    selected_topics = ['직장인을 위한 영어패턴1-25']
    st.write("직장인을 위한 영어패턴1-25 듣기")
    st.audio('combined1.m4a', loop = loop)
  elif topic == '미국 직장인이 매일 쓰는 영어 100문장':
    selected_topics = ['미국 직장인이 매일 쓰는 영어 100문장']
    st.write("미국 직장인이 매일 쓰는 영어 100문장 듣기")
    st.audio('combined2.m4a', loop = loop)
  elif topic == '원어민이 가장 많이 쓰는 구동사 30개':
    selected_topics = ['원어민이 가장 많이 쓰는 구동사 30개']
    st.write("원어민이 가장 많이 쓰는 구동사 30개 듣기")
    st.audio('combined3.m4a', loop = loop)
  elif topic == '일상 영어 회화 패턴 20개':
    selected_topics = ['일상 영어 회화 패턴 20개']
    st.write("일상 영어 회화 패턴 20개 듣기")
    st.audio('combined4.m4a', loop = loop)
  elif topic == '회사에서 지겹도록 듣게되는 영어 문장 40개':
    selected_topics = ['회사에서 지겹도록 듣게되는 영어 문장 40개']
    st.write("회사에서 지겹도록 듣게되는 영어 문장 40개 듣기")
    st.audio('combined5.m4a', loop = loop)
  elif topic == '비즈니스 이메일 핵심패턴 15개':
    selected_topics = ['비즈니스 이메일 핵심패턴 15개']
    st.write("비즈니스 이메일 핵심패턴 15개 듣기")
    st.audio('combined6.m4a', loop = loop)
  
  #selected_topics = st.multiselect('학습 주제 선택',  ['직장인을 위한 영어패턴1-25', '미국 직장인이 매일 쓰는 영어 100문장', '원어민이 가장 많이 쓰는 구동사 30개', '일상 영어 회화 패턴 20개', '회사에서 지겹도록 듣게되는 영어 문장 40개'],
  #  default= ['직장인을 위한 영어패턴1-25', '미국 직장인이 매일 쓰는 영어 100문장', '원어민이 가장 많이 쓰는 구동사 30개', '일상 영어 회화 패턴 20개', '회사에서 지겹도록 듣게되는 영어 문장 40개'])


  df = dataframe[dataframe['Topic'].isin(selected_topics)]



  #st.write("")
  with st.expander('선택한 학습 주제의 모든 문장 보기'):
      st.write(df)

  st.write("")
  st.subheader('English Quiz')  # 타이틀명 지정
  
  # n개의 무작위 샘플 추출
  #n_quiz = st.number_input('한번에 나오는 문제 수 설정', 0, 99, value = 1)
  n_quiz =1
  df_samples = df.sample(n=n_quiz)
  df_quiz = df_samples.loc[:, ['Korean']]
  df_answer = df_samples.loc[:, ['English']]
  quiz = df_quiz.iloc[0,0]
  answer = df_answer.iloc[0,0]
  sound_file = BytesIO()
  tts = gTTS(answer, lang='en')
  tts.write_to_fp(sound_file)
  
  tab1, tab2, tab3 = st.tabs(['Korean' , 'English', 'English Audio'])
  with tab1:
    #tab A 를 누르면 표시될 내용
    st.table(df_quiz)
    
  with tab2:
    #tab B를 누르면 표시될 내용 
    st.table(df_answer)

  with tab3:
    #tab C를 누르면 표시될 내용
    
    st.audio(sound_file)

  if st.button("Reload"):
    st.write("")

  #st.write("")
  #st.subheader('Korean-English Audio')  # 타이틀명 지정
  #st.write("모든 문장 듣기")
  #st.audio('combined_all.m4a')
  
  #st.write("직장인을 위한 영어패턴1-25 듣기")
  #st.audio('combined1.m4a')

  #st.write("미국 직장인이 매일 쓰는 영어 100문장 듣기")
  #st.audio('combined2.m4a')

  #st.write("원어민이 가장 많이 쓰는 구동사 30개 듣기")
  #st.audio('combined3.m4a')

  #st.write("일상 영어 회화 패턴 20개 듣기")
  #st.audio('combined4.m4a')

  #st.write("회사에서 지겹도록 듣게되는 영어 문장 40개 듣기")
  #st.audio('combined5.m4a')
  
  #st.write(df)

  st.write("")
  st.write("")
  link1 = '[Conference Call Scenario Link](http://english-scenario.streamlit.app)'
  st.markdown(link1, unsafe_allow_html=True)

else:
  st.write("")
  
