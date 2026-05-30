# def greeting():
#     return "Hello python"

# def abc(a):
#     return True if a>20 else False

# print(abc(10))

# def greetings(name,age):
#     print('Hello '+name+' ,you are '+ str(age) +' old')

# greetings('Rama',20)


def talk(phrase):

    def say(word):
        print(word)

    words = phrase.split(" ")

    for word in words:
        say(word)

    

talk('hello this is python')