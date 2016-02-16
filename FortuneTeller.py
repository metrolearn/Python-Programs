
#import Python's 'randomrange' module
from random import randrange

#list of possible answers
fortuneTellerAnswers = [
"It is certain",
"It is decidedly so",
"Without a doubt",
"Yes, definitely",
"You may rely on it",
"As I see it, yes",
"Most likely",
"Outlook good",
"Yes",
"Signs point to yes",
"Reply hazy try again",
"Ask again later",
"Better not tell you now",
"Cannot predict now",
"Concentrate and ask again",
"Don't count on it",
"My reply is no",
"My sources say no",
"Outlook not so good"
]

#ask user for name
person = input('Hi whats your name: ')
#ask user if they would like their fortune read
print("Hello " + person +", would you like your fortune read today? ")
answer = input("Enter Y for yes and N for no..." )

#if the user DOES not enter Y quit
if answer != 'Y':
    print("Ok Goodbye!")
    exit
    #else read let the person ask you a question
    #and predict their fortune.
else:
    question =  input("Ask me any question!")
     
    #create random index number
    #within the range of the qty of possible answers.
    random_index = randrange(0, len(fortuneTellerAnswers))

    #return a random answer (based on random index number)
    answerForUser = fortuneTellerAnswers[random_index]
    
    #print answer
    print(answerForUser)
