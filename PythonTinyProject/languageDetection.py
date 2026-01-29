'''
We can detect the language of a given text in Python using the langdetect library
'''
from langdetect import detect

text = input("Enter any text in any language: ")
print(detect(text))