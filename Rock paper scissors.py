import random

statements = {'win' : ['Horray!' , 'Awesome!' , 'You got me this time!', 'Hats of to you!', 'Great game!', 'Hip-Hip-Hurray!','Kudos!', "I'll get you next time",], 'lose' : ['Better luck next time', 'You can do better!','Try again!'],'tie' : ['You read my mind', "It's a tie"]}

outcomes= ['rock','paper','scissors']

result = 'temp'
while result is not 'end':
    
    computer = random.choice(outcomes)
    user = input ('\nEnter choice: \n')
    
    if user == computer:
        result = 'tie'
    elif user == 'rock' and computer == 'scissors':
        result = 'win'
    elif user == 'rock' and computer == 'paper':
        result = 'lose'
    elif user == 'paper' and computer == 'rock':
        result = 'win'
    elif user == 'paper' and computer == 'scissors':
        result = 'lose'
    elif user == 'scissors' and computer == 'paper':
        result = 'win'
    elif user == 'scissors' and computer == 'rock':
        result = 'lose'
    elif user == 'end':
        result = 'end'
        break
    else:
        result = 'invalid'
        print('Please enter a valid input')
        continue
    print(computer)
    print(result)

    remark = random.choice(statements[result])
    print(remark)
          
