import requests
import ast #Need to include this module to convert the request to a DICT

#Request Call

key = {'token':'31ffebf069ebed28cd2ceb3b62ad6787'}
#Getting the request
dictionary = requests.post('http://challenge.code2040.org/api/haystack', json = key)

#print (dictionary)# Brings back a response<200>

hayStack = ast.literal_eval(dictionary.text) #Using this method to turn the unicode to a dictionary.
#print(hayStack)# Displays the dict
target = hayStack[hayStack.keys()[1]]#converting the needle to a string
#print(target)# checking my string
#Target changes

index = hayStack["haystack"].index(target)# finds the index of the needle in they haystack.

#print index #Displays the targets index location

result = {'token': '31ffebf069ebed28cd2ceb3b62ad6787', 'needle':index} # retrieving results and storing them to a DICT

result = requests.post('http://challenge.code2040.org/api/haystack/validate', json = result)

print(result.text)
