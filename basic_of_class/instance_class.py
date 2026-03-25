class Animal:

    name_of_animal = 'start'
    animal_sound = 'start'

    def __init__(self,nameOfAnomal,AnimalSound):
       
        self.name_of_animal = nameOfAnomal
        self.animal_sound = AnimalSound

        print('inside class animal name = ',self.name_of_animal)
        print('inside class  animal sound = ',self.animal_sound)



# invoke
# an1 and an2 are instance class
an1 = Animal('dog','bark')

print('outside of class animal_sound ', an1.animal_sound)
print('outside of class name_of_animal ', an1.name_of_animal)

print('')
print('')
print('')
print('')
print('')
an2 = Animal('cat', 'meaw')
