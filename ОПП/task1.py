# python - объекто - орентированный язык 
# python - и в тоже время  процедурный язык

# print(dir(str))

# class Character:
#     gender = ''
#     name = ''
#     height = 0
#     weight = 0
#     hands = 2
#     weapom = []

# peter = Character()
# bruce = Character()
# peter.weapom = 'gun'
# print(peter.weapom)
# print(bruce.weapom)

class Cow():
    def __init__(self, weight, sound='my-my'):
        self.weight = weight
        self.sound = sound

    def eat(self, food):
        self.weight -= food

    def domilk(liter):
        weight -= liter * 0.7

class Goose():
    weight = ''
    sound = 'cri-cri'
    def eat(self, food):
        self.weight -= food

class Sheep():
    weight = ''
    sound = 'be-be'
    def eat(self, food):
        self.weight -= food

class Chicken():
    def __init__(self, weight=0, sound='ko-ko', agg=0):
        self.weight = ''
        self.sound = 'ko-ko'
        self.agg = agg


    def eat(self, food):
        self.weight -= food

class Goat():
    weight = ''
    sound = 'be-be-be'
    def eat(self, food):
        self.weight -= food

    def domilk(liter):
        weight -= liter * 0.7

class Duck():
    weight = ''
    sound = 'cry-cry'
    def eat(self, food):
        self.weight -= food


koko = Chicken(agg=20)

print(koko.agg)
 