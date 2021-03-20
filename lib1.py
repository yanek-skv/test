# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Gruz_Transort():
    def __init__(self,marks,mton, svoboden=True):
        self.marks=marks
        self.mton=mton
        self.svoboden=svoboden

    def ton(self, ton):
        if ton <= self.mton:
            return True
        else:
            return False

    def free(self, svoboden):
        if self.svoboden:
            return True
        else:
            return False

class Garaz():
    garaze=dict()
    def __init__(self, name, kolvo):
        self.name=name
        self.kolvo=kolvo

    def add_to_garag(self,name, car):
        self.garaze[name] = car

    def chek(self):
        for name, car in self.garaze.items():
            if car.svoboden:
                print(name, 'свободен')
            else:
                print(name, 'не свободен')





