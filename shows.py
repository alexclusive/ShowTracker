import csv

class shows:
    # 0 = id
    # 1 = title
    # 2 = status
    # 3 = season
    # 4 = episode
    # 5 = hour
    # 6 = min
    # 7 = sec
    def __init__(self):
        self.showsList = []

    def updateShows(self, filename:str):
        print("updating shows")
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.showsList.append(row)

    def printCurrentShows(self):
        for row in self.showsList:
            print(row)