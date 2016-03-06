#session 08 in class - 2/25/2016

# working on OO and class objects

class A:
    def hello(self):
        print("Hi")

class B(A):
    def hello(self):
        super().hello() #calls the super
        print("there")

b = B()
b.hello()

# ANIMAL KINGDOM

class Animal(object): # object is a master class

    def __init__(self):
        pass

class Mammal(Animal):
    warm_blood = True # put here because it is a total class attribute
    gestation_in_a_womb = True
    def __init__(self):
        pass


class Reptile(Animal):
    warm_blood = False
    gestation_in_a_womb = False
    def __init__(self):
        pass

class Bird(Reptile):
    warm_blood = True #over-wrote the super class attribute in Reptile: refer to that thing and put in a new definition in the child

    def __init__(self):
        pass

#creating an instance # need to be before it is called
my_mammal = Mammal()

my_reptile = Reptile()


class Snake(Reptile):

    def __init__(self):
        pass


class Dog(Mammal):
    #chases cats is not a global class feature

    def __init__(self,chases_cats=True):
        self.chases_cats = chases_cats # would go here - b/c true for most dogs, but not all, so
        #  this can be over-written (not a full class attribute)
        pass

    def make_me_cold_blooded(self):
        self.warm_blood = False
        pass


class Cat(Mammal):

    def __init__(self, hates_dogs = True):
        self.hates_dogs = hates_dogs # an individual individual object tracking characterisit , not a total cat thing
        pass


print( my_mammal.warm_blood)
print( my_reptile.warm_blood)

def main():
    pass

if __name__ =='__main__': #usually see this in bottom of files
    main()

my_dog = Dog(chases_cats=False)
my_cat = Cat()

print(dir(my_dog)


