user = input('Enter your name: ')
playing = input('Do you wanna play the game? (y/n) ')

if playing != "y":
    print('Goodbye ', user)
else:
    print('Welcome To The Adventure ', user, ' !')
    
    answer = input("You are on an unknown Island and found some wood. Do you wanna create raft or weapon? " ).lower()
    if answer == 'raft':
        print('Successfully built Raft.')
        print('Ready to explore the Ocean.')

        answer = input("Now you're quite far from that island. Do you wanna keep moving forward or return? (forward/return) ").lower()
        if answer == 'forward':
            print('While moving forward, storm came and you drowned. YOU LOSE!')
        elif answer == 'return':
            print('Returned back to the Island.')
            
            answer = input("Do you wanna create weapon form wood of raft or continue? ").lower()
            if answer == 'weapon':
                print('Axe Created.')
                print('Exploring The Wild!')

                answer = input('What do you want to collect, wood or food? ').lower()
                if answer == 'wood':
                    print('You died of hunger. YOU LOSE!')
                elif answer == 'food':
                    print('Energy Full.')
                    print('Cutting trees to collect wood.')
                    print('Wood Collected.')

                    answer = input('Do you want to create better weapon or boat? ').lower()
                    if answer == 'boat':
                        print('Continuing to Way of Waters!')
                        print('Heading towards Home.')
                        print('Low on Energy.')

                        answer = input('Do you wanna catch fish or continue? ').lower()
                        if answer == 'fish':
                            print('Full on energy.')
                            print('You were attacked by Pirates, you fought and died. YOU LOSE!')
                        elif answer == 'continue':
                            print('You died of hunger. YOU LOSE')
                        else:
                            print('ERROR. Entered wrong choice. YOU LOSE!')
                    
                    elif answer == 'weapon':
                        print('While crafting a Cross-bow, you heard some human voices.')
                        print('You start to follow the voices and see some people in the cage.')

                        answer = input('Do you want to save them or no? (y/n)')
                        if answer == 'y':
                            print('You saved them and you all defeated the pirate.')
                            print('You took his treasure and left for your home. You successfully completed the Adventure. YOU WON!')
                        elif answer == 'n':
                            print('You were caught too. YOU LOSED!')
                        else:
                            print('ERROR. Entered wrong choice. YOU LOSE!')
                    else:
                        print('ERROR. Entered wrong choice. YOU LOSE!')
                else:
                    print('ERROR. Entered wrong choice. YOU LOSE!')
            elif answer == 'continue':
                print('You were attacked by animals. YOU LOSE!')
            else:
                print('ERROR. Entered wrong choice. YOU LOSE!')
        else:
            print('ERROR. Entered wrong choice. YOU LOSE!')
    elif answer == 'weapon':
        print('Axe Created.')
        print('Exploring The Wild!')

        answer = input('What do you want to collect, wood or food? ').lower()
        if answer == 'wood':
            print('You died of hunger. YOU LOSE!')
        elif answer == 'food':
            print('Energy Full.')
            print('Cutting trees to collect wood.')
            print('Wood Collected.')

            answer = input('Do you want to create better weapon or boat? ').lower()
            if answer == 'boat':
                print('Continuing to Way of Waters!')
                print('Heading towards Home.')
                print('Low on Energy.')

                answer = input('Do you wanna catch fish or continue? ').lower()
                if answer == 'fish':
                    print('Full on energy.')
                    print('You were attacked by Pirates, you fought and died. YOU LOSE!')
                elif answer == 'continue':
                    print('You died of hunger. YOU LOSE')
                else:
                    print('ERROR. Entered wrong choice. YOU LOSE!')
                    
            elif answer == 'weapon':
                print('While crafting a Cross-bow, you heard some human voices.')
                print('You start to follow the voices and see some people in the cage.')

                answer = input('Do you want to save them or no? (y/n)')
                if answer == 'y':
                    print('You saved them and you all defeated the pirate.')
                    print('You took his treasure and left for your home. You successfully completed the Adventure. YOU WON!')
                elif answer == 'n':
                    print('You were caught too. YOU LOSED!')
                else:
                    print('ERROR. Entered wrong choice. YOU LOSE!')
            else:
                print('ERROR. Entered wrong choice. YOU LOSE!')
    else:
        print('ERROR. Entered wrong choice. YOU LOSE!')