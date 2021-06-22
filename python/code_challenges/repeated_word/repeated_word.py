from Data_Structures.hashtable.hashtable import Hashtable
import re

def repeated_word(string):
  # create hashmap
  hashmap = Hashtable()

  words_list = re.findall(r'\w+', string)

  for word in words_list:
    counter = 0
    lower_word = word.lower()
    if not hashmap.contains(lower_word):

        hashmap.add(lower_word,counter)
        counter+= 1

    else:
      return lower_word
