from fastapi import FastAPI
from gtts import gTTS
import os

app = FastAPI()


@app.get('/convert/{target_text}')
def text_to_speech(target_text:str):
    myobj = gTTS(text=target_text, lang='ar', slow=False)
    myobj.save("welcome.mp3")

    os.system("totem welcome.mp3")