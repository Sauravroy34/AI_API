from g4f.client import Client
from flask import Flask , request ,jsonify
import sys
import tkinter


class mainframe():
    def __init__(self) -> None:
        pass


def bot(text):

    client = Client()
    response = client.chat.completions.create(
        model="gemini",
        messages=[{"role": "user", "content": f"{text}"}],
        
    )
    data = (response.choices[0].message.content)
    print(data)


while True:
    text = input("enter your doubt ")
    if text.upper() == "CLOSE":
        sys.exit()
    bot(text)
    