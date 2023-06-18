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
        self.currentID = 0
        self.filename = ""

    def updateShows(self, filename:str):
        print("updating shows")
        self.filename = filename
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.showsList.append(row)
                self.currentID += 1

    def clearFile(self):
        with open(self.filename, 'r+') as file:
            file.truncate(0)
        self.updateShows(self.filename)

    def getCurrentID(self) -> int:
        return self.currentID
    
    def itemString(self, item:list) -> str:
        if len(item) == 8:
            ret = ""
            for field in item:
                ret += "," + str(field)
            return ret[1:] + "\n"

    def addShow(self, item:list):
        if len(item) == 8:
            self.showsList.append(item)
            with open(self.filename, 'a') as file:
                file.write(self.itemString(item))
            self.currentID += 1