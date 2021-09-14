import csv

with open('leaderboards.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    # sortedlist = sorted(reader, key=operator.itemgetter(1), reverse=True)
    sortedlist = sorted(reader, key=lambda row: int(row[1]), reverse=True)

    if len(sortedlist) > 10:
        for i in range(10):
            print(f'{sortedlist[i][0]}: {sortedlist[i][1]}')
    else:
        for i in range(len(sortedlist)):
            print(f'{sortedlist[i][0]}: {sortedlist[i][1]}')