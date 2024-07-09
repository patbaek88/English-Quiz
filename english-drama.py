import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO
import os

password_input = st.text_input("암호를 입력해주세요",type= "password")
if password_input == "cmcpl":

  st.header("English Drama Expressions")
  st.write("")
  # scenario 데이터 불러오기
  filename = st.selectbox('Select a scenario', ('The Office_S01E01.csv','The Office_S01E02.csv'))
  data = pd.read_csv(filename)

  exp_df = pd.read_csv('The Office_S01_expressions.csv')

  expressions = data[['Exp_En', 'Exp_Kr']].set_index('Exp_En')
  df = exp_df[exp_df['Episode'].isin(filename)]
  st.dataframe(df)

  
  temp_audio_dir = 'temp_audio'
  os.makedirs(temp_audio_dir, exist_ok=True)
  st.write("")

  lang_df = pd.DataFrame({'Language':['English', 'Spanish', 'French', 'German', 'Italian', 'Chinese', 'Japanese', 'Korean'],  'Code':['en', 'es', 'fr', 'de', 'it', 'zh', 'ja', 'ko']})
  lang_select = st.selectbox('Select a language', lang_df['Language'])
  lang_code = lang_df[lang_df['Language'] == lang_select]['Code']
  lang = lang_code.iloc[0]
  accent = 'com'
  if lang == 'en':
    accent_df = pd.DataFrame({'Accent':['United States', 'United Kingdom', 'Ireland', 'Canada', 'Australia', 'India', 'South Africa'],  'Accent_Code':['com', 'co.uk', 'ie', 'ca', 'com.au', 'co.in', 'co.za']})
    accent_select = st.selectbox('Select an English accent', accent_df['Accent'])
    accent_code = accent_df[accent_df['Accent'] == accent_select]['Accent_Code']
    accent = accent_code.iloc[0]

  
  #sound_file = BytesIO()
  st.write("")

  for index, row in data.iterrows():
    english_sentence = row['English']
    korean_translation = row['Korean']
    order = row['Number']
    tts=gTTS(english_sentence, lang=lang, tld=accent)
    audio_file_path = os.path.join(temp_audio_dir, f'audio_{index}.mp3')
    tts.save(audio_file_path)
    st.write(f"{order}. ")
    st.audio(audio_file_path)
    #if st.button("Show Text"):
    #  st.write(f"{english_sentence}")
    st.write(f"{korean_translation}")
    st.write(f"{english_sentence}")
    st.write("")
        
  
else:
  st.write("")

