#single quotes
message = 'Hello World'
message = 'bob\'s world'

#double quotes
message = "bob's worldd"

#multiline
message = """ this is python """

# Finding length 
print(len(message))

#Acces a character
print(message[2])

#Access a part of the string
print(message[0:5])

# Lowecase and Uppercase
print(message.upper())
print(message.lower())

#Find and Count 
print(message.find('this'))
print(message.count('i'))

#Replace the word
print(message.replace('this','that'))

#Concat 

greet = 'Hello'
name = 'Michel'


print(greet + ' ' +name)

#Better way
print('{}, {}.welcome!'.format(greet,name))

#Even better in python3

print(f'{greet}, {name}.welcome!')

#casting 

num1 = '100'
num2 = '200'

num1 = int(num1)
num2 = int(num2)
print(num1+num2)