import re

### Calculates and returns the percentage of words in user_audio and the given_input ###

def compare(user_audio, given_input, length):
  count=0
  user_input = re.sub("[^\w]", " ",  user_audio).split()
  for x in user_input:
    for y in given_input:
      if(x==y):
        count+=1
  return ((count/length)*100.00)