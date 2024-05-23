import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO
import os
from pydub import AudioSegment

password_input = st.text_input("암호를 입력해주세요",type= "password")

if password_input == "cmcpl":
  # review 데이터 불러오기
  dataframe = pd.read_csv('review.csv')

  selected_topics = st.multiselect('학습 주제 선택',  ['직장인을 위한 영어패턴1-25', '미국 직장인이 매일 쓰는 영어 100문장', '원어민이 가장 많이 쓰는 구동사 30개', '일상 영어 회화 패턴 20개', '회사에서 지겹도록 듣게되는 영어 문장 40개'],
    default= ['직장인을 위한 영어패턴1-25', '미국 직장인이 매일 쓰는 영어 100문장', '원어민이 가장 많이 쓰는 구동사 30개', '일상 영어 회화 패턴 20개', '회사에서 지겹도록 듣게되는 영어 문장 40개'])

  df = dataframe[dataframe['Topic'].isin(selected_topics)]
  
  # n개의 무작위 샘플 추출
  df_samples = df.sample(n=1)
  df_quiz = df_samples.loc[:, ['Korean']]
  df_answer = df_samples.loc[:, ['English']]
  quiz = df_quiz.iloc[0,0]
  answer = df_answer.iloc[0,0]
  sound_file = BytesIO()
  tts = gTTS(answer, lang='en')
  tts.write_to_fp(sound_file)

  # scenario 데이터 불러오기
  #data = pd.read_csv('scenario.csv')
  #temp_audio_dir = 'temp_audio'
  #os.makedirs(temp_audio_dir, exist_ok=True)


  st.title('English Quiz')  # 타이틀명 지정
  st.write("")
  
  #st.write(df_quiz)

  #if st.button("Answer"):
  #  st.write(df_answer)

  tab1, tab2, tab3 = st.tabs(['Korean' , 'English', 'English-Audio'])
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

  st.write("")
  st.write("")
  #st.write('All Sentences for the Quiz')
  with st.expander('Show All Sentences'):
      st.write(df)

  # mp3 파일 생성
  mp3_files = []
  tts_korean = gTTS(quiz, lang='ko')
  tts_english = gTTS(answer, lang='en')
  mp3_files.append(tts_korean)
  mp3_files.append(tts_english)
                    
  #for i in range(len(df)):
  #    tts_korean = gTTS(df.loc[i, 'Korean'], lang='ko')
  #    tts_korean.save('korean_{}.mp3'.format(i))
  #    mp3_files.append('korean_{}.mp3'.format(i))
  #    tts_english = gTTS(df.loc[i, 'English'], lang='en')
  #    tts_english.save('english_{}.mp3'.format(i))
  #    mp3_files.append('english_{}.mp3'.format(i))

  # mp3 파일 합치기
  combined = AudioSegment.empty()
  for mp3_file in mp3_files:
      sound = AudioSegment.from_mp3(mp3_file)
      combined += sound

  # 합쳐진 mp3 파일 저장
  st.audio(combined)

  #st.write(df)

  st.write("")
  st.write("")
  link1 = '[Conference Call Scenario Link](http://english-scenario.streamlit.app)'
  st.markdown(link1, unsafe_allow_html=True)

else:
  st.write("")


