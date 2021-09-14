dice = [2, 4, 3, 1, 5]
dice = list(set(sorted(dice)))
print(dice)

if (dice[0] == dice[1]-1 == dice[2]-2 == dice[3]-3 == dice[4]-4) or (dice[1] == dice[2]-1 == dice[3]-2 == dice[4]-3 == dice[5]-4):
    print("True")
else:
    print("False")
