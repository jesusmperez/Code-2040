
import requests

key ={'token':'31ffebf069ebed28cd2ceb3b62ad6787'}#Storing the token in a key value

endpoint = requests.post('http://challenge.code2040.org/api/reverse', json = key)

#print(request.txt), String is given

givenString = endpoint.text

givenStringSize = len(givenString)# Finding the length of the string
reverseString = ""# Initializing to avoid junk values

for x in range (0, givenStringSize):#Iterating through the string.
	
	reverseString = givenString[x] + reverseString# Concatenating the string in reverse order
	
#print(reverseString) testing.

lastStage = {'token':'31ffebf069ebed28cd2ceb3b62ad6787', 'string': reverseString}
	
request = requests.post('http://challenge.code2040.org/api/reverse/validate', json = lastStage)

print request.text
