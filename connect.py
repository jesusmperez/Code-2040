import requests# importing requests module to connect to CODE2040 API



registration = {'token':'31ffebf069ebed28cd2ceb3b62ad6787', 'github':'https://github.com/jesusmperez/Code-2040.git'}#creating registration endpoint with two key values (token, repository).
endpoint = requests.post('http://challenge.code2040.org/api/register', json = registration)#connecting to the api
print endpoint.text

#Reversing a string


