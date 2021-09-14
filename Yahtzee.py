# Made by Matthew DiMaggio #
#     Created 8/5/2021     #
#  Last Updated 8/26/2021  #

import secrets
import csv


class Player:
    def __init__(self, name):
        self.name = name


class Card:
    # Upper Section
    aces = "#"
    twos = "#"
    threes = "#"
    fours = "#"
    fives = "#"
    sixes = "#"
    upper_subtotal = "#"
    upper_bonus = "#"
    upper_total = "#"

    # Lower Section
    three_of_a_kind = "#"
    four_of_a_kind = "#"
    full_house = "#"
    small_straight = "#"
    large_straight = "#"
    yahtzee = "#"
    chance = "#"
    yahtzee_bonus = "#"
    lower_total = "#"

    # Finish
    grand_total = "#"


class Dice:
    def __init__(self):
        self.value = 1
        self.keep = 0

    def roll(self):
        randomizer = secrets.SystemRandom()
        self.value = randomizer.randrange(1, 7)

    def keep_dice(self):
        self.keep = 1

    def unkeep_dice(self):
        self.keep = 0

    def show_value(self):
        return self.value


def reset():
    # Upper Section
    Card.aces = "#"
    Card.twos = "#"
    Card.threes = "#"
    Card.fours = "#"
    Card.fives = "#"
    Card.sixes = "#"
    Card.upper_subtotal = "#"
    Card.upper_bonus = "#"
    Card.upper_total = "#"

    # Lower Section
    Card.three_of_a_kind = "#"
    Card.four_of_a_kind = "#"
    Card.full_house = "#"
    Card.small_straight = "#"
    Card.large_straight = "#"
    Card.yahtzee = "#"
    Card.chance = "#"
    Card.yahtzee_bonus = "#"
    Card.lower_total = "#"

    # Finish
    Card.grand_total = "#"


def end_state_debug(val):
    # THIS FUNCTION IS FOR DEBUG USE ONLY
    if val == 0:
        Card.aces = 4
        Card.twos = 8
        Card.threes = 12
        Card.fours = 16
        Card.fives = 20
        Card.sixes = 24
        Card.upper_subtotal = "#"   # Expected Value: 84
        Card.upper_bonus = "#"   # Expected Value: 35
        Card.upper_total = "#"   # Expected Value: 119

        Card.three_of_a_kind = 24
        Card.four_of_a_kind = 11
        Card.full_house = 25
        Card.small_straight = 30
        Card.large_straight = 40
        Card.yahtzee = 50
        Card.chance = 17
        Card.yahtzee_bonus = 0
        Card.lower_total = "#"   # Expected Value: 197

        Card.grand_total = "#"   # Expected Value: 315
    else:
        randomizer = secrets.SystemRandom()
        Card.aces = randomizer.randrange(1, 6)
        Card.twos = randomizer.randrange(2, 11)
        Card.threes = randomizer.randrange(3, 16)
        Card.fours = randomizer.randrange(4, 21)
        Card.fives = randomizer.randrange(5, 26)
        Card.sixes = randomizer.randrange(6, 31)
        Card.upper_subtotal = "#"
        Card.upper_bonus = "#"
        Card.upper_total = "#"

        Card.three_of_a_kind = randomizer.randrange(5, 31)
        Card.four_of_a_kind = randomizer.randrange(5, 31)
        Card.full_house = randomizer.choice([0, 25])
        Card.small_straight = randomizer.choice([0, 30])
        Card.large_straight = randomizer.choice([0, 40])
        Card.yahtzee = randomizer.choice([0, 50])
        Card.chance = randomizer.randrange(5, 31)
        Card.yahtzee_bonus = randomizer.choice([0, 100, 200, 300])
        Card.lower_total = "#"

        Card.grand_total = "#"


def game_end(debug=0):
    Card.upper_subtotal = Card.aces + Card.twos + Card.threes + Card.fours + Card.fives + Card.sixes
    if Card.upper_subtotal >= 63:
        Card.upper_bonus = 35
    else:
        Card.upper_bonus = 0
    Card.upper_total = Card.upper_subtotal + Card.upper_bonus
    Card.lower_total = Card.three_of_a_kind + Card.four_of_a_kind + Card.full_house + Card.small_straight + \
                  Card.large_straight + Card.yahtzee + Card.chance + Card.yahtzee_bonus
    Card.grand_total = Card.upper_total + Card.lower_total

    def leaderboard_input():
        player_name = input("Enter your name: ")
        leaderboard_txt = open("leaderboards.csv", "a")
        leaderboard_txt.write(f'{player_name}, {Card.grand_total}\n')
        leaderboard_txt.close()

    if debug == 0:
        leaderboard_input()
    else:
        pass

    print(f'███████████████████████\n'
          f'█ UPPER SECTION █\n'
          f'█---------------█\n'
          f'█          Aces █ {Card.aces}\n'
          f'█          Twos █ {Card.twos}\n'
          f'█        Threes █ {Card.threes}\n'
          f'█         Fours █ {Card.fours}\n'
          f'█         Fives █ {Card.fives}\n'
          f'█         Sixes █ {Card.sixes}\n'
          f'█---------------█\n'
          f'█   UPPER TOTAL █ {Card.upper_subtotal}\n'
          f'█         BONUS █ {Card.upper_bonus}\n'
          f'█         TOTAL █ {Card.upper_total}\n'
          f'███████████████████████\n'
          f'█ LOWER SECTION █\n'
          f'█---------------█\n'
          f'█   3 of a kind █ {Card.three_of_a_kind}\n'
          f'█   4 of a kind █ {Card.four_of_a_kind}\n'
          f'█    Full House █ {Card.full_house}\n'
          f'█  Sm. Straight █ {Card.small_straight}\n'
          f'█  Lg. Straight █ {Card.large_straight}\n'
          f'█       YAHTZEE █ {Card.yahtzee}\n'
          f'█        Chance █ {Card.chance}\n'
          f'█ YAHTZEE BONUS █ {Card.yahtzee_bonus}\n'
          f'█---------------█\n'
          f'█   LOWER TOTAL █ {Card.lower_total}\n'
          f'███████████████████████\n'
          f'█   GRAND TOTAL █ {Card.grand_total}\n'
          f'███████████████████████')
    input()


def main():
    dice1 = Dice()
    dice2 = Dice()
    dice3 = Dice()
    dice4 = Dice()
    dice5 = Dice()

    def play_round():

        def game_check():
            if "#" in [Card.aces, Card.twos, Card.threes, Card.fours, Card.fives, Card.sixes,
                       Card.three_of_a_kind, Card.four_of_a_kind, Card.full_house, Card.small_straight,
                       Card.large_straight, Card.yahtzee, Card.chance]:
                round_first_roll()
            else:
                game_end()

        # General Functions

        def show_board():
            clear_screen = '\n' * 100

            rbs1 = "#"
            rbs2 = "#"
            rbs3 = "#"
            rbs4 = "#"
            rbs5 = "#"

            rbk1 = "#"
            rbk2 = "#"
            rbk3 = "#"
            rbk4 = "#"
            rbk5 = "#"
            die_keep_list = [dice1.keep, dice2.keep, dice3.keep, dice4.keep, dice5.keep]
            die_value_list = [dice1.value, dice2.value, dice3.value, dice4.value, dice5.value]
            board_shuffle_list = [rbs1, rbs2, rbs3, rbs4, rbs5]
            board_keep_list = [rbk1, rbk2, rbk3, rbk4, rbk5]

            for i in range(5):
                if die_keep_list[i] == 1:
                    board_keep_list[i] = die_value_list[i]
                    board_shuffle_list[i] = " "
                elif die_keep_list[i] == 0:
                    board_keep_list[i] = " "
                    board_shuffle_list[i] = die_value_list[i]

            rolling_board = f'█████████████████████████████████████\n' \
                            f'█                                   █\n' \
                            f'█    |{board_shuffle_list[0]}|   |{board_shuffle_list[1]}|   ' \
                            f'|{board_shuffle_list[2]}|   |{board_shuffle_list[3]}|   ' \
                            f'|{board_shuffle_list[4]}|    █\n' \
                            f'█                                   █\n' \
                            f'█████████████████████████████████████\n' \
                            f'█    |{board_keep_list[0]}|   |{board_keep_list[1]}|   ' \
                            f'|{board_keep_list[2]}|   |{board_keep_list[3]}|   |{board_keep_list[4]}|    ' \
                            f'█\n' \
                            f'█████████████████████████████████████\n'
            print(f'{clear_screen}{rolling_board}')

        def show_scorecard():
            print(f'Upper Section -- Aces: {Card.aces}, Twos: {Card.twos}, Threes: {Card.threes}, Fours: {Card.fours}, '
                  f'Fives: {Card.fives}, Sixes: {Card.sixes}\n'
                  f'Lower Section -- Three of a kind: {Card.three_of_a_kind}, Four of a kind: {Card.four_of_a_kind}, '
                  f'Full House: {Card.full_house}, Small Straight: {Card.small_straight}, '
                  f'Large Straight: {Card.large_straight}, Yahtzee: {Card.yahtzee}, Chance: {Card.chance}, '
                  f'Yahtzee Bonus: {Card.yahtzee_bonus}')

        # incomplete
        def show_leaderboards():
            print("\n")
            import csv
            with open('leaderboards.csv', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                sortedlist = sorted(reader, key=lambda row: int(row[1]), reverse=True)
                if len(sortedlist) > 10:
                    for i in range(10):
                        print(f'{sortedlist[i][0]}: {sortedlist[i][1]}')
                else:
                    for i in range(len(sortedlist)):
                        print(f'{sortedlist[i][0]}: {sortedlist[i][1]}')

            print("\n")

        # Round Actions

        def round_keep():
            # User inputs the dice to keep

            _ = [{dice1.value}, {dice2.value}, {dice3.value}, {dice4.value}, {dice5.value}]

            # f'Keeps: {dice1.keep}, {dice2.keep}, {dice3.keep}, {dice4.keep}, {dice5.keep}'
            die_keep_list = input("Enter Dice Numbers (1 - 5) (Separated By a Space) ").split()
            for keeps in die_keep_list:
                if int(keeps) > 5 or int(keeps) < 1:
                    str(keeps)
                    die_keep_list = ""
                    print("Invalid Die Number")
                    round_keep()
            for keeps in die_keep_list:
                eval(f'dice{keeps}.keep_dice()')

            # f'Keep Check: {dice1.keep}, {dice2.keep}, {dice3.keep}, {dice4.keep}, {dice5.keep}'

        def round_unkeep():
            # User inputs the dice to unkeep

            _ = [{dice1.value}, {dice2.value}, {dice3.value}, {dice4.value}, {dice5.value}]

            # f'Keeps: {dice1.keep}, {dice2.keep}, {dice3.keep}, {dice4.keep}, {dice5.keep}'
            die_keep_list = input("Enter Dice Numbers (1 - 5) (Separated By a Space) ").split()
            for keeps in die_keep_list:
                if int(keeps) > 5 or int(keeps) < 1:
                    str(keeps)
                    die_keep_list = ""
                    print("Invalid Die Number")
                    round_keep()
            for keeps in die_keep_list:
                eval(f'dice{keeps}.unkeep_dice()')

            # f'Keep Check: {dice1.keep}, {dice2.keep}, {dice3.keep}, {dice4.keep}, {dice5.keep}'

        def round_analyze():
            # Upper Section

            # Aces
            ace_analyze = 0
            if dice1.value == 1:
                ace_analyze += 1
            if dice2.value == 1:
                ace_analyze += 1
            if dice3.value == 1:
                ace_analyze += 1
            if dice4.value == 1:
                ace_analyze += 1
            if dice5.value == 1:
                ace_analyze += 1

            if (ace_analyze > 0) and (Card.aces == "#"):
                ace_analyze_print = f'Aces: {ace_analyze}, '
            else:
                ace_analyze_print = ''

            # Twos
            two_analyze = 0
            if dice1.value == 2:
                two_analyze += 2
            if dice2.value == 2:
                two_analyze += 2
            if dice3.value == 2:
                two_analyze += 2
            if dice4.value == 2:
                two_analyze += 2
            if dice5.value == 2:
                two_analyze += 2

            if (two_analyze > 0) and (Card.twos == "#"):
                two_analyze_print = f'Twos: {two_analyze}, '
            else:
                two_analyze_print = ''

            # Threes
            three_analyze = 0
            if dice1.value == 3:
                three_analyze += 3
            if dice2.value == 3:
                three_analyze += 3
            if dice3.value == 3:
                three_analyze += 3
            if dice4.value == 3:
                three_analyze += 3
            if dice5.value == 3:
                three_analyze += 3

            if (three_analyze > 0) and (Card.threes == "#"):
                three_analyze_print = f'Threes: {three_analyze}, '
            else:
                three_analyze_print = ''

            # Fours
            four_analyze = 0
            if dice1.value == 4:
                four_analyze += 4
            if dice2.value == 4:
                four_analyze += 4
            if dice3.value == 4:
                four_analyze += 4
            if dice4.value == 4:
                four_analyze += 4
            if dice5.value == 4:
                four_analyze += 4

            if (four_analyze > 0) and (Card.fours == "#"):
                four_analyze_print = f'Fours: {four_analyze}, '
            else:
                four_analyze_print = ''

            # Fives
            five_analyze = 0
            if dice1.value == 5:
                five_analyze += 5
            if dice2.value == 5:
                five_analyze += 5
            if dice3.value == 5:
                five_analyze += 5
            if dice4.value == 5:
                five_analyze += 5
            if dice5.value == 5:
                five_analyze += 5

            if (five_analyze > 0) and (Card.fives == "#"):
                five_analyze_print = f'Fives: {five_analyze}, '
            else:
                five_analyze_print = ''

            # Sixes
            six_analyze = 0
            if dice1.value == 6:
                six_analyze += 6
            if dice2.value == 6:
                six_analyze += 6
            if dice3.value == 6:
                six_analyze += 6
            if dice4.value == 6:
                six_analyze += 6
            if dice5.value == 6:
                six_analyze += 6

            if (six_analyze > 0) and (Card.sixes == "#"):
                six_analyze_print = f'Sixes: {six_analyze}, '
            else:
                six_analyze_print = ''

            # Lower Section
            dice_lower_analyze = [str(dice1.value), str(dice2.value), str(dice3.value), str(dice4.value),
                                  str(dice5.value)]
            dice_lower_analyze = sorted(dice_lower_analyze)
            straight_dice_analyze = list(set(sorted([dice1.value, dice2.value, dice3.value, dice4.value, dice5.value])))

            # 3 of a Kind
            threeofakind_analyze = 0
            if dice_lower_analyze[0][0] == dice_lower_analyze[2][0] or \
                    dice_lower_analyze[1][0] == dice_lower_analyze[3][0] or \
                    dice_lower_analyze[2][0] == dice_lower_analyze[4][0]:
                threeofakind_analyze = dice1.value + dice2.value + dice3.value + dice4.value + dice5.value

            if (threeofakind_analyze > 0) and (Card.three_of_a_kind == "#"):
                threeofakind_analyze_print = f'3 of a kind: {threeofakind_analyze}, '
            else:
                threeofakind_analyze_print = ''

            # 4 of a Kind
            fourofakind_analyze = 0
            if dice_lower_analyze[0][0] == dice_lower_analyze[3][0] or \
                    dice_lower_analyze[1][0] == dice_lower_analyze[4][0]:
                fourofakind_analyze = dice1.value + dice2.value + dice3.value + dice4.value + dice5.value

            if (fourofakind_analyze > 0) and (Card.four_of_a_kind == "#"):
                fourofakind_analyze_print = f'4 of a kind: {fourofakind_analyze}, '
            else:
                fourofakind_analyze_print = ''

            # Full House
            fullhouse_analyze = 0
            if (dice_lower_analyze[0][0] == dice_lower_analyze[2][0] and dice_lower_analyze[3][0] ==
                dice_lower_analyze[4][0]) or \
                    (dice_lower_analyze[0][0] == dice_lower_analyze[1][0] and dice_lower_analyze[2][0] ==
                     dice_lower_analyze[4][0]):
                fullhouse_analyze = 25

            if (fullhouse_analyze > 0) and (Card.full_house == "#"):
                fullhouse_analyze_print = f'Full House: {fullhouse_analyze}, '
            else:
                fullhouse_analyze_print = ''

            # Small Straight
            small_analyze = 0
            small_analyze_test = 0
            if (straight_dice_analyze[0] == straight_dice_analyze[1] - 1 == straight_dice_analyze[2] - 2 ==
                    straight_dice_analyze[3] - 3) or (straight_dice_analyze[1] == straight_dice_analyze[2] - 1 ==
                                                      straight_dice_analyze[3] - 2 == straight_dice_analyze[4] - 3):
                small_analyze_test = 1

            if (small_analyze_test == 1) and (Card.small_straight == "#"):
                small_analyze = 30

            if small_analyze > 0:
                small_analyze_print = f'Small Straight: {small_analyze}, '
            else:
                small_analyze_print = ''

            # Large Straight
            large_analyze = 0
            large_analyze_test = 0
            if (straight_dice_analyze[0] == straight_dice_analyze[1] - 1 == straight_dice_analyze[2] - 2 ==
                straight_dice_analyze[3] - 3 == straight_dice_analyze[4] - 4) or (straight_dice_analyze[1] ==
                                                                                  straight_dice_analyze[2] - 1 ==
                                                                                  straight_dice_analyze[3] - 2 ==
                                                                                  straight_dice_analyze[4] - 3 ==
                                                                                  straight_dice_analyze[5] - 4):
                large_analyze_test = 1

            if (large_analyze_test == 1) and (Card.large_straight == "#"):
                large_analyze = 40

            if large_analyze > 0:
                large_analyze_print = f'Large Straight: {large_analyze}, '
            else:
                large_analyze_print = ''

            # Yahtzee
            yahtzee_analyze = 0
            if dice_lower_analyze[0] == dice_lower_analyze[1] == dice_lower_analyze[2] == \
                    dice_lower_analyze[3] == dice_lower_analyze[4]:
                yahtzee_analyze = 50

            if (yahtzee_analyze > 0) and (Card.yahtzee == "#"):
                yahtzee_analyze_print = f'Yahtzee: {yahtzee_analyze}, '
            elif (yahtzee_analyze > 0) and (Card.yahtzee != "#"):
                yahtzee_analyze = 100
                yahtzee_analyze_print = f'Yahtzee: {yahtzee_analyze}, '
            else:
                yahtzee_analyze_print = ''

            # Chance
            chance_analyze = dice1.value + dice2.value + dice3.value + dice4.value + dice5.value
            if (chance_analyze > 0) and (Card.chance == "#"):
                chance_analyze_print = f'Chance: {chance_analyze}, '
            else:
                chance_analyze_print = ''

            # Show Results
            print(f'Upper Section -- '
                  f'{ace_analyze_print}{two_analyze_print}{three_analyze_print}'
                  f'{four_analyze_print}{five_analyze_print}{six_analyze_print}')
            print(f'Lower Section -- '
                  f'{threeofakind_analyze_print}{fourofakind_analyze_print}{fullhouse_analyze_print}'
                  f'{small_analyze_print}{large_analyze_print}{yahtzee_analyze_print}{chance_analyze_print}')

        def round_end():
            dice_lower_analyze = [str(dice1.value), str(dice2.value), str(dice3.value), str(dice4.value),
                                  str(dice5.value)]
            dice_lower_analyze = sorted(dice_lower_analyze)
            straight_dice_analyze = [dice1.value, dice2.value, dice3.value, dice4.value, dice5.value]
            straight_dice_analyze = list(set(straight_dice_analyze))

            print("\nScorecard Entry Options:")
            round_analyze()
            end_round_input = input("Select Scorecard Slot: ")

            if (end_round_input.lower() in ["aces", "ace", "one", "ones"]) and (Card.aces == "#"):
                ace_end = 0
                if dice1.value == 1:
                    ace_end += 1
                if dice2.value == 1:
                    ace_end += 1
                if dice3.value == 1:
                    ace_end += 1
                if dice4.value == 1:
                    ace_end += 1
                if dice5.value == 1:
                    ace_end += 1

                if ace_end == 0:
                    ace_input = input("You are about to input a 0 value. Would you like to continue? (y/n) ")
                    if ace_input.lower() in ["y", "yes"]:
                        Card.aces = ace_end
                        play_round()
                    else:
                        round_end()
                else:
                    Card.aces = ace_end
                    play_round()
            elif (end_round_input.lower() in ["twos", "two"]) and (Card.twos == "#"):
                two_end = 0
                if dice1.value == 2:
                    two_end += 2
                if dice2.value == 2:
                    two_end += 2
                if dice3.value == 2:
                    two_end += 2
                if dice4.value == 2:
                    two_end += 2
                if dice5.value == 2:
                    two_end += 2

                if two_end == 0:
                    two_input = input("You are about to input a 0 value. Would you like to continue? (y/n) ")
                    if two_input.lower() in ["y", "yes"]:
                        Card.twos = two_end
                        play_round()
                    else:
                        round_end()
                else:
                    Card.twos = two_end
                    play_round()
            elif (end_round_input.lower() in ["threes", "three"]) and (Card.threes == "#"):
                three_end = 0
                if dice1.value == 3:
                    three_end += 3
                if dice2.value == 3:
                    three_end += 3
                if dice3.value == 3:
                    three_end += 3
                if dice4.value == 3:
                    three_end += 3
                if dice5.value == 3:
                    three_end += 3

                if three_end == 0:
                    three_input = input("You are about to input a 0 value. Would you like to continue? (y/n) ")
                    if three_input.lower() in ["y", "yes"]:
                        Card.threes = three_end
                        play_round()
                    else:
                        round_end()
                else:
                    Card.threes = three_end
                    play_round()
            elif (end_round_input.lower() in ["fours", "four"]) and (Card.fours == "#"):
                four_end = 0
                if dice1.value == 4:
                    four_end += 4
                if dice2.value == 4:
                    four_end += 4
                if dice3.value == 4:
                    four_end += 4
                if dice4.value == 4:
                    four_end += 4
                if dice5.value == 4:
                    four_end += 4

                if four_end == 0:
                    four_input = input("You are about to input a 0 value. Would you like to continue? (y/n) ")
                    if four_input.lower() in ["y", "yes"]:
                        Card.fours = four_end
                        play_round()
                    else:
                        round_end()
                else:
                    Card.fours = four_end
                    play_round()
            elif (end_round_input.lower() in ["fives", "five"]) and (Card.fives == "#"):
                five_end = 0
                if dice1.value == 5:
                    five_end += 5
                if dice2.value == 5:
                    five_end += 5
                if dice3.value == 5:
                    five_end += 5
                if dice4.value == 5:
                    five_end += 5
                if dice5.value == 5:
                    five_end += 5

                if five_end == 0:
                    five_input = input("You are about to input a 0 value. Would you like to continue? (y/n) ")
                    if five_input.lower() in ["y", "yes"]:
                        Card.fives = five_end
                        play_round()
                    else:
                        round_end()
                else:
                    Card.fives = five_end
                    play_round()
            elif (end_round_input.lower() in ["sixes", "six"]) and (Card.sixes == "#"):
                six_end = 0
                if dice1.value == 6:
                    six_end += 6
                if dice2.value == 6:
                    six_end += 6
                if dice3.value == 6:
                    six_end += 6
                if dice4.value == 6:
                    six_end += 6
                if dice5.value == 6:
                    six_end += 6

                if six_end == 0:
                    six_input = input("You are about to input a 0 value. Would you like to continue? (y/n) ")
                    if six_input.lower() in ["y", "yes"]:
                        Card.sixes = six_end
                        play_round()
                    else:
                        round_end()
                else:
                    Card.sixes = six_end
                    play_round()
            elif (end_round_input.lower() in ["three of a kind", "threeofakind", "three_of_a_kind", "3 of a kind",
                                              "3ofakind", "3_of_a_kind"]) and (Card.three_of_a_kind == "#"):
                threeofakind_end = 0
                if dice_lower_analyze[0][0] == dice_lower_analyze[2][0] or \
                        dice_lower_analyze[1][0] == dice_lower_analyze[3][0] or \
                        dice_lower_analyze[2][0] == dice_lower_analyze[4][0]:
                    threeofakind_end = dice1.value + dice2.value + dice3.value + dice4.value + dice5.value

                if threeofakind_end == 0:
                    threeofakind_input = input("You are about to input a 0 value. Would you like to continue? (y/n) ")
                    if threeofakind_input.lower() in ["y", "yes"]:
                        Card.three_of_a_kind = threeofakind_end
                        play_round()
                    else:
                        round_end()
                else:
                    Card.three_of_a_kind = threeofakind_end
                    play_round()
            elif (end_round_input.lower() in ["four of a kind", "fourofakind", "four_of_a_kind", "4ofakind",
                                              "4 of a kind", "4_of_a_kind"]) and (Card.four_of_a_kind == "#"):
                fourofakind_end = 0
                if dice_lower_analyze[0][0] == dice_lower_analyze[3][0] or \
                        dice_lower_analyze[1][0] == dice_lower_analyze[4][0]:
                    fourofakind_end = dice1.value + dice2.value + dice3.value + dice4.value + dice5.value

                if fourofakind_end == 0:
                    fourofakind_input = input("You are about to input a 0 value. Would you like to continue? (y/n) ")
                    if fourofakind_input.lower() in ["y", "yes"]:
                        Card.four_of_a_kind = fourofakind_end
                        play_round()
                    else:
                        round_end()
                else:
                    Card.four_of_a_kind = fourofakind_end
                    play_round()
            elif (end_round_input.lower() in ["full house", "fullhouse", "full_house"]) and (Card.full_house == "#"):
                fullhouse_end = 0
                if (dice_lower_analyze[0][0] == dice_lower_analyze[2][0] and dice_lower_analyze[3][0] ==
                    dice_lower_analyze[4][0]) or \
                        (dice_lower_analyze[0][0] == dice_lower_analyze[1][0] and dice_lower_analyze[2][0] ==
                         dice_lower_analyze[4][0]):
                    fullhouse_end = 25

                if fullhouse_end == 0:
                    fullhouse_input = input("You are about to input a 0 value. Would you like to continue? (y/n) ")
                    if fullhouse_input.lower() in ["y", "yes"]:
                        Card.full_house = fullhouse_end
                        play_round()
                    else:
                        round_end()
                else:
                    Card.full_house = fullhouse_end
                    play_round()
            elif (end_round_input.lower() in ["small straight", "smallstraight", "small_straight", "small"]) and \
                    (Card.small_straight == "#"):
                small_end = 0
                small_end_test = 0
                if (straight_dice_analyze[0] == straight_dice_analyze[1] - 1 == straight_dice_analyze[2] - 2 ==
                    straight_dice_analyze[3] - 3) or (straight_dice_analyze[1] == straight_dice_analyze[2] - 1 ==
                                                      straight_dice_analyze[3] - 2 == straight_dice_analyze[4] - 3):
                    small_end_test = 1

                if (small_end_test == 1) and (Card.small_straight == "#"):
                    small_end = 30

                if small_end == 0:
                    small_input = input("You are about to input a 0 value. Would you like to continue? (y/n) ")
                    if small_input.lower() in ["y", "yes"]:
                        Card.small_straight = small_end
                        play_round()
                    else:
                        round_end()
                else:
                    Card.small_straight = small_end
                    play_round()
            elif (end_round_input.lower() in ["large straight", "largestraight", "large_straight", "large"]) and \
                    (Card.large_straight == "#"):
                large_end = 0
                large_end_test = 0
                if (straight_dice_analyze[0] == straight_dice_analyze[1] - 1 == straight_dice_analyze[2] - 2 ==
                    straight_dice_analyze[3] - 3 == straight_dice_analyze[4] - 4) or (straight_dice_analyze[1] ==
                                                                                      straight_dice_analyze[2] - 1 ==
                                                                                      straight_dice_analyze[3] - 2 ==
                                                                                      straight_dice_analyze[4] - 3 ==
                                                                                      straight_dice_analyze[5] - 4):
                    large_end_test = 1

                if (large_end_test == 1) and (Card.large_straight == "#"):
                    large_end = 40

                if large_end == 0:
                    large_input = input("You are about to input a 0 value. Would you like to continue? (y/n) ")
                    if large_input.lower() in ["y", "yes"]:
                        Card.large_straight = large_end
                        play_round()
                    else:
                        round_end()
                else:
                    Card.large_straight = large_end
                    play_round()
            elif (end_round_input.lower() == "yahtzee") and (Card.yahtzee == "#"):
                yahtzee_end = 0
                if dice_lower_analyze[0] == dice_lower_analyze[1] == dice_lower_analyze[2] == \
                        dice_lower_analyze[3] == dice_lower_analyze[4]:
                    yahtzee_end = 50

                if yahtzee_end == 0:
                    yahtzee_input = input("You are about to input a 0 value. Would you like to continue? (y/n) ")
                    if yahtzee_input.lower() in ["y", "yes"]:
                        Card.yahtzee = yahtzee_end
                        play_round()
                    else:
                        round_end()
                else:
                    Card.yahtzee = yahtzee_end
                    play_round()
            elif (end_round_input.lower() == "yahtzee") and (Card.yahtzee != "#"):
                yahtzee_end = 0
                if dice_lower_analyze[0] == dice_lower_analyze[1] == dice_lower_analyze[2] == \
                        dice_lower_analyze[3] == dice_lower_analyze[4]:
                    yahtzee_end = 100

                if yahtzee_end == 0:
                    print("You cannot use Yahtzee Bonus as a dud input")
                    round_end()
                else:
                    if Card.yahtzee_bonus == "#":
                        Card.yahtzee = yahtzee_end
                        dice1.value = 0
                        dice2.value = 0
                        dice3.value = 0
                        dice4.value = 0
                        dice5.value = 0
                        print("Use must now use an empty square on your scorecard as a dud input")
                        round_end()
                    else:
                        Card.yahtzee_bonus += yahtzee_end
                        Card.yahtzee = yahtzee_end
                        dice1.value = 0
                        dice2.value = 0
                        dice3.value = 0
                        dice4.value = 0
                        dice5.value = 0
                        print("Use must now use an empty square on your scorecard as a dud input")
                        round_end()
            elif (end_round_input.lower() == "chance") and (Card.chance == "#"):
                chance_end = dice1.value + dice2.value + dice3.value + dice4.value + dice5.value

                if chance_end == 0:
                    chance_input = input("You are about to input a 0 value. Would you like to continue? (y/n) ")
                    if chance_input.lower() in ["y", "yes"]:
                        Card.chance = chance_end
                        play_round()
                    else:
                        round_end()
                else:
                    Card.chance = chance_end
                    play_round()
            else:
                print("Invalid Entry")
                round_end()

        # Rolling Functions

        def round_first_roll():
            # reset dice keeping settings
            dice1.unkeep_dice()
            dice2.unkeep_dice()
            dice3.unkeep_dice()
            dice4.unkeep_dice()
            dice5.unkeep_dice()

            # roll all dice
            dice1.roll()
            dice2.roll()
            dice3.roll()
            dice4.roll()
            dice5.roll()

            def round_input_pause():
                user_selection = input("What would you like to do? "
                                       "(reroll, keep, unkeep, analyze, scorecard, leaderboards, end rolls) ")

                if user_selection.lower() in ["reroll", "roll"]:
                    round_second_roll()
                    # begin second roll
                elif user_selection.lower() == "keep":
                    round_keep()
                    show_board()
                    round_input_pause()
                elif user_selection.lower() == "unkeep":
                    round_unkeep()
                    show_board()
                    round_input_pause()
                elif user_selection.lower() == "analyze":
                    round_analyze()
                    round_input_pause()
                elif user_selection.lower() == "scorecard":
                    show_scorecard()
                    round_input_pause()
                elif user_selection.lower() == "leaderboards":
                    show_leaderboards()
                    round_input_pause()
                elif user_selection.lower() in ["end rolls", "endrolls", "end"]:
                    round_end()
                    # new round start
                elif user_selection == "AdMiN DeBuG: END_STATE_DEBUG":
                    end_state_debug(0)
                    play_round()
                elif user_selection == "AdMiN DeBuG: END_STATE_DEBUG_RAND":
                    end_state_debug(1)
                    play_round()
                else:
                    print("Invalid Command")
                    round_input_pause()

            show_board()
            round_input_pause()

        def round_second_roll():
            # roll all unkept dice
            if dice1.keep == 0:
                dice1.roll()
            if dice2.keep == 0:
                dice2.roll()
            if dice3.keep == 0:
                dice3.roll()
            if dice4.keep == 0:
                dice4.roll()
            if dice5.keep == 0:
                dice5.roll()

            def round_input_pause():
                user_selection = input("What would you like to do? "
                                       "(reroll, keep, unkeep, analyze, scorecard, leaderboards, end rolls) ")

                if user_selection.lower() in ["reroll", "roll"]:
                    round_third_roll()
                    # begin second roll
                elif user_selection.lower() == "keep":
                    round_keep()
                    show_board()
                    round_input_pause()
                elif user_selection.lower() == "unkeep":
                    round_unkeep()
                    show_board()
                    round_input_pause()
                elif user_selection.lower() == "analyze":
                    round_analyze()
                    round_input_pause()
                elif user_selection.lower() == "scorecard":
                    show_scorecard()
                    round_input_pause()
                elif user_selection.lower() == "leaderboards":
                    show_leaderboards()
                    round_input_pause()
                elif user_selection.lower() in ["end rolls", "endrolls", "end"]:
                    round_end()
                    # new round start
                else:
                    print("Invalid Command")
                    round_input_pause()

            show_board()
            round_input_pause()

        def round_third_roll():
            # roll all unkept dice
            if dice1.keep == 0:
                dice1.roll()
            if dice2.keep == 0:
                dice2.roll()
            if dice3.keep == 0:
                dice3.roll()
            if dice4.keep == 0:
                dice4.roll()
            if dice5.keep == 0:
                dice5.roll()

            def round_input_pause():
                user_selection = input("What would you like to do? "
                                       "(analyze, scorecard, leaderboards, end rolls) ")
                if user_selection.lower() in ["reroll", "roll"]:
                    print("Cannot roll more than 3 times")
                    round_input_pause()
                elif user_selection.lower() == "keep":
                    round_keep()
                    show_board()
                    round_input_pause()
                elif user_selection.lower() == "unkeep":
                    round_unkeep()
                    show_board()
                    round_input_pause()
                elif user_selection.lower() == "analyze":
                    round_analyze()
                    round_input_pause()
                elif user_selection.lower() == "scorecard":
                    show_scorecard()
                    round_input_pause()
                elif user_selection.lower() == "leaderboards":
                    show_leaderboards()
                    round_input_pause()
                elif user_selection.lower() in ["end rolls", "endrolls", "end"]:
                    round_end()
                    # new round start
                else:
                    print("Invalid Command")
                    round_input_pause()

            show_board()
            round_input_pause()

        game_check()

    play_round()


if __name__ == '__main__':
    main()
