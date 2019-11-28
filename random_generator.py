from random_word import RandomWords
import re
import random

def generate_random_words(n):
  r=RandomWords()
  list_of_words=r.get_random_words(hasDictionaryDef="true", includePartOfSpeech="noun,adjective", minLength=5, limit=n)
  print(list_of_words)
  return list_of_words

def select_paragraph():
  index=random.choice([1,2,3,4,5,6,7,8,9,0])
  articles=['Biased journalist or biased news channel shows that all policies and steps of government or apolitical party is always right.', 
  'They do not criticize government for their wrong work and this will harm the democracy or country because criticism is the backbone of democracy',
  'The temple has been out of bounds for Indian pilgrims since partition. Earlier, annual pilgrimages were organised by the kings.',
  'These trips, known as yatras, flourished during the reign of Maharaja Ranbir Singh. ',
  'A saint known as Swami Nandlalji was the last to live here, even beyond partition.', 
  'Plastic is the material consisting of synthetic or semi synthetic organic compounds that are malleable.',
  'Promise and peril is the two sides of plastic. The revolution brought by the plastic in India was really like a brown study even for its inventor himself.',
  'Management of the planning in India now itself a infrastructure activity. Offenders is a punishable activity.',
  'It was born during the first Industrial Revolution. Parkesine is considered the first ever man-made plastic on earth.',
  'Since then it has not seen any restrictions imposed on by the technologically genius human beings until they themselves realised their own dooms due to this plastic.']
  print(articles[index])
  return(articles[index])