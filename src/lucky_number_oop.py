import random
import datetime

class NumberGuessingGame:
    def __init__(self,input_function=input):
        self.input_function = input_function
        self.player_lucky_list = [random.randint(0, 100) for _ in range(10)]
        self.lucky_number = random.choice(self.player_lucky_list)
        self.tries_count = 0
        self.done = False
        self.player_name = ""
        self.player_birthdate = ""
        self.player_age = 0
    
    def initialize_game_properties(self):
        self.player_lucky_list = [random.randint(0, 100) for _ in range(10)]
        self.lucky_number = random.choice(self.player_lucky_list)
        self.tries_count = 0
        

    def welcome_message(self):
        print("Welcome to the Number Guessing Game!")

    
    def get_player_name(self):
        while True:
        
            player_name = input("Please enter your full name (first name and last name with a single space): ")
            player_name = player_name.strip()
            if all(c.isalpha() or c.isspace() for c in player_name) and player_name.count(' ') == 1:
                self.player_name = player_name
                break
            
            else:
                print("Invalid input. Please enter a valid name with only letters and a single space between first name and last name.")
                self.player_name = None  # Set player_name to None for invalid input

    def get_player_birthdate(self):
        while True:
            birthdate = input("Please enter your birthdate in the format yyyymmdd: ")
            if len(birthdate) == 8 and birthdate.isdigit():
                year = int(birthdate[:4])
                month = int(birthdate[4:6])
                day = int(birthdate[6:8])
                try:
                    self.player_birthdate = datetime.date(year, month, day)
                    break
                except ValueError:
                    print("Invalid date. Please enter a valid date in the format yyyymmdd.")
                    self.player_birthdate = None
            else:
                print("Invalid input. Please enter a valid date in the format yyyymmdd.")
                self.player_birthdate = None

    def calculate_player_age(self):
        current_year = datetime.datetime.now().year
        self.player_age = current_year - self.player_birthdate.year
        if self.player_age < 18:
            print("Sorry, you are not allowed to play because you are underage.")
            self.done = True

    def start(self):
        #self.initialize_game_properties()
        print("DEBUG: player_lucky_list at start:", self.player_lucky_list)
        self.welcome_message()  # Call the welcome_message method
        self.get_player_name()   # Call the get_player_name method
        self.get_player_birthdate()  # Call the get_player_birthdate method
        self.calculate_player_age()  # Call the player_age method

        while not self.done:
            if self.done:
                break  # Exit the loop if the game is already done
            self.tries_count += 1
            print(self.player_lucky_list)
            player_guess_str = input(f'Hi {self.player_name}, this is your try #{self.tries_count}. Please enter a number from the list: ')
            
            

            if not player_guess_str.isdigit():
                print('Sorry, wrong value, enter an integer NUMBER!!!')
                continue
            
            player_guess = int(player_guess_str)
            
            if player_guess == self.lucky_number:
                print(f'Congratulations, your lucky number is {self.lucky_number}. You got it from try #{self.tries_count}')
                self.done = True
                self.play_again()
                break

            short_list = list(set([num for num in self.player_lucky_list if abs(num - self.lucky_number) < 11]))

            print("DEBUG: Short list:", short_list)

            while short_list and len(short_list) > 2:
                self.tries_count += 1
                new_guess_str = input(f'Guess the number from the short list {short_list}: ')
                if not new_guess_str.isdigit():
                    print('Sorry, wrong value, enter an integer NUMBER!!!')
                    continue
                new_guess = int(new_guess_str)
                if new_guess in short_list:  # Check if new_guess is in short_list
                    if new_guess == self.lucky_number:
                        print(f'Congratulations, your lucky number is {self.lucky_number}. You got it from try #{self.tries_count}')
                        self.done = True
                        self.play_again()
                        break
                    short_list.remove(new_guess)  # Remove new_guess from short_list
                else:
                    print(f'Your guess {new_guess} is not in the short list. Try again.')

            if len(short_list) <= 2:
                print(f'These numbers remain {short_list} and the game is over.')
                self.done = True

            # while short_list:
            #     self.tries_count += 1
            #     if len(short_list) <= 2:
            #         print(f'These numbers remain {short_list} and the game is over.')
            #         self.done = True
            #         break

            #     new_guess_str = input(f'Guess the number from the short list {short_list}: ')
            #     if not new_guess_str.isdigit():
            #         print('Sorry, wrong value, enter an integer NUMBER!!!')
            #         continue

            #     new_guess = int(new_guess_str)
            #     if new_guess in short_list:  # Check if new_guess is in short_list
            #         if new_guess == self.lucky_number:
            #             print(f'Congratulations, your lucky number is {self.lucky_number}. You got it from try #{self.tries_count}')
            #             self.done = True
            #             self.play_again()
            #             break

            #         short_list.remove(new_guess)  # Remove new_guess from short_list   
            #     else:
            #             print(f'Your guess {new_guess} is not in the short list. Try again.')
            #     if not new_guess_str.isdigit():
            #         print('Sorry, wrong value, enter an integer NUMBER!!!')
            #         continue
                
                

           

    def play_again(self):
        play_again_input = input("Do you want to play again? (Input 'y' for Yes, 'n' for No): ")
        if play_again_input.lower() == 'y':
            self.player_lucky_list = [random.randint(0, 100) for _ in range(10)]
            self.lucky_number = random.choice(self.player_lucky_list)
            self.tries_count = 0
            self.done = False
        else:
            print("Thanks for playing. Goodbye!")
            self.done= True

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.start()
