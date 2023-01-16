print('Welcome To My JAVA Quiz!')

playing = input('Do you want to play? (y/n): ')

if playing != 'y':
    print('Goodbye user')
else:
    print("Okay! Let's begin the Quiz.")
    print("This Quiz has 5 questions.")

    correctAnswers = 0
    incorrectAnswers = 0
    quesList = ['What is a correct syntax to output "Hello World" in Java?: ', 'Is Java short for "JavaScript"?: ', 'Which method can be used to return a string in upper case letters?: ', 'Which data type is used to create a variable that should store text?: ', 'How do you create a method in Java?']
    ansList = ['System.out.println("Hello World")', 'No', 'toUpperCase()', 'String', 'methodName()']
    for i in range(5):
        answer = input(quesList[i])

        if answer == ansList[i]:
            correctAnswers += 1
        else:
            incorrectAnswers += 1

    print('Out of 5 questions, correct answers are ', correctAnswers, ' and incorrect answers are ', incorrectAnswers)
    
