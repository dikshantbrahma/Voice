import speech_recognition as sr
import re
import math
from comparison import compare
from random_generator import generate_random_words, select_paragraph
r=sr.Recognizer()
num=10
case=1
if(case==0):
  given_input=generate_random_words(num)
else:
  given_input=re.sub("[^\w]", " ",  select_paragraph().lower()).split()
  num=len(given_input)

with sr.Microphone() as source:
  print("Speak Now")
  audio=r.listen(source)
  print("Time over, thanks")

try:
  user_input=r.recognize_google(audio)
  print(user_input)
  print("SUCCESS PERCENTAGE: ")
  print(math.floor(compare(user_input, given_input, num)))
except:
  print("ERROR")