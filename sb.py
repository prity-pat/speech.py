import streamlit as st
import speech_recognition as sr 

st.title('Speech to Text Converter')

recog = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    st.write('Please speak...')
    audio = recog.listen(source)

    try:
        text = recog.recognise_google(audio)
        st.write(f'You said: {Text}')
    except:
        st.write('Sorry. I could not understand the audio.')
    finally:
        st.write("processing complete.")        



