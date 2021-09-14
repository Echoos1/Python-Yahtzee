dice = [(3), (6), (4), (5), (1)]
hand = sorted(dice)
hand = set(hand)
hand = list(hand)
print(hand)
test = 0
for i in range(len(hand)-1):
    if hand[i] == hand[i + 1] - 1:
        test += 1
    print(f'{i} Test:{test}    if {hand[i]} == {hand[i + 1]}-1')


if test == 4:
    print("Large Straight")
if test >= 3:
    print("Small Straight")
else:
    print("Not a Straight")

