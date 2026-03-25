class Animal:

    name_of_animal = 'start'
    sound = 'start'

    def __init__(self,nameOfAnomal):
        name_of_animal = 'test'
        print('this is class init method')
        print('self', self)
        print('animal name = ',self.name_of_animal)
        print('animal sound = ',self.sound)
        print('name_of_animal local ',name_of_animal)
        self.name_of_animal = nameOfAnomal
        self.sound = 'bark'
        name_of_animal = 'test2'
        print('animal name = ',self.name_of_animal)
        print('animal sound = ',self.sound)
        print('name_of_animal local ',name_of_animal)



# invoke
# an1 and an2 are instance class
an1 = Animal('dog')

print('-'*50)
print('-'*50)
print('-'*50)
an2 = Animal('cat')