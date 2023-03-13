import random


class RPC:

    def __init__(self, u, c):
        self.User_choice = u
        self.Computer_choice = c

    def user_input(self):
        while True:
            x = input("Enter r = Rock, p = Paper, s = Scissor, e = Exit : ")
            if x == 'r' or x == 'R' or x == 'p' or x == 'P' or x == 's' or x == 'S':
                return x.lower()

            elif x == 'e' or x == 'E':
                return x.lower()

            else:
                print("Invalid input. Enter Again ")

    def check_winner(self):
        if self.Computer_choice == self.User_choice:
            print("\t\tIt's a Draw")

        elif self.Computer_choice == 'r':
            if self.User_choice == 's':
                print('\t\tComputer Wins')

            elif self.User_choice == 'p':
                print('\t\tUser Wins')

        elif self.Computer_choice == 'p':
            if self.User_choice == 'r':
                print('\t\tComputer Wins')

            elif self.User_choice == 's':
                print('\t\tUser Wins')

        elif self.Computer_choice == 's':
            if self.User_choice == 'p':
                print('\t\tComputer Wins')

            elif self.User_choice == 'r':
                print('\t\tUser Wins')

    def play(self):
        uchoice = self.user_input()
        self.User_choice = uchoice

        compchoice = ['r', 'p', 's']
        self.Computer_choice = random.choice(compchoice)
        print('Your Choice : ', self.User_choice)
        print('Your Computer : ', self.Computer_choice)

        if self.User_choice == 'e':
            return self.User_choice

        self.check_winner()
        print('')


def play_main(obj):
    x = obj.play()
    return x


if __name__ == '__main__':

    print("\t\tWELCOME TO ROCK PAPER SCISSORS")
    print('')
    obj = RPC('n', 'n')
    while True:
        x = input("To Play press (y) OR press any key to exit ").lower()

        if x == 'y':
            t = play_main(obj)
            if t == 'e':
                break


        else:
            break
