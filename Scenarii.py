class ModeLevel:
    def __init__(self):
        self.mode = ["CleanAll","BuildPlus","BuildEqual"]
        self.number_of_molecules = 0
        self.number_of_atoms = 0
        self.type_of_mode = -1

    def setMode(self, typeMode):
        self.type_of_mode = typeMode

    def setNumberMolecules(self,numMol):
        self.number_of_molecules = numMol

    def setNumberAtoms(self,numAt):
        self.number_of_atoms = numAt

class PlayGround:
    def __init__(self):
        self.nbRows = 8         # l'aire de jeu est de 8 par 8
        self.nbColumns = 8
        self.playGround = [[0] * self.nbColumns for i in range(self.nbRows)]

    def setBlock(self,row,column):
        self.playGround[row,column] = 1

    def setPlayGround(self,level):

class Level:
    def __init__(self):
        self.levelNumber = -1
        self.number_of_Hydrogen = -1
        self.number_of_Oxygen = -1
        self.number_of_Nitrogen = -1
        self.number_of_Carbon = -1
        self.number_of_atoms = -1
        self.modeLevel = ModeLevel()
        self.playGround = PlayGround()

    def setNumbers(self,listeNumbers):
        self.number_of_Hydrogen = listeNumbers[0]
        self.number_of_Oxygen = listeNumbers[1]
        self.number_of_Nitrogen = listeNumbers[2]
        self.number_of_Carbon = listeNumbers[3]

    def getNumberOfAtoms(self):
        return self.number_of_Hydrogen+self.number_of_Oxygen+self.number_of_Nitrogen+self.number_of_Carbon

    def setModelLevel(self):


class Scenario:
    def __init__(self):
        self.level = Level()
        self.liste_of_atoms = [0 for i in range(self.level.playGround.nbRows*self.level.playGround.nbColumns)]

    def getModelLevel(self):
        return self.level.modeLevel

    def getLevel(self):
        return self.level

    def generateScenario(self,levelNb):
        listeNumbers = [0 for i in range(4)]
        listeNumbers[0] = 2
        listeNumbers[1] = 0
        listeNumbers[2] = 0
        listeNumbers[3] = 0
        self.level.setNumbers(listeNumbers)
        self.level.levelNumber = levelNb



class Scenarii:
    def __init__(self):
        self.number_of_levels = 25 # nous générons 25 niveaux de jeu de difficulté à peu près croissante
        self.scenarii = [Scenario() * self.number_of_levels]

    def exportScenarii(self):
        toto = 0

    def generateScenarii(self):
        for levelNb in range(self.number_of_levels):
            self.scenarii[levelNb].generateScenario(levelNb)

def import_settings():
    toto = 0

def main():
    for index in range(25) :
        print(index)

if __name__ == '__main__':
    main()