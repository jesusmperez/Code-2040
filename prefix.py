import requests
import ast # need this module to convert the request to a DICT
key = {'token': '31ffebf069ebed28cd2ceb3b62ad6787'}

dictionary = requests.post('http://challenge.code2040.org/api/prefix', json = key)# Returns a response

print(dictionary)#Checking my dictionary

# converted the request to a dictionary
convertedDict = ast.literal_eval(dictionary.text)

#saved the given prefix into a string literal
prefix = convertedDict[convertedDict.keys()[0]]

#stored the size of the prefix value

size = len(prefix)


words = []#Creating a container to store the words without the ptefix

sizeOfConvertedDict = len(convertedDict['array'])# the size of the array in our dictionary


for x in range(sizeOfConvertedDict):#traversing through the array
	if prefix != convertedDict['array'][x][:size]:# if prefix is not found, 
		words.append(convertedDict['array'][x])# then it gets added to our container.




result = {'token': '31ffebf069ebed28cd2ceb3b62ad6787', 'array': words}
#checking my results
request = requests.post('http://challenge.code2040.org/api/prefix/validate', json = result)

print request.text





