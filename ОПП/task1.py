# python - объекто - орентированный язык 
# python - и в тоже время  процедурный язык

# print(dir(str))

class Character:
    gender = ''
    name = ''
    height = 0
    weight = 0
    hands = 2
    weapom = []

peter = Character()
bruce = Character()
peter.weapom = 'gun'
print(peter.weapom)
print(bruce.weapom)