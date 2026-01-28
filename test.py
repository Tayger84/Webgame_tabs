
class Dog:
    def __init__(self, name, age, kennel = None):
        self.name = name
        self.age = age
        self.kennel = kennel
        
    def bark(self):
        print(f'{self.name.capitalize()} štěká! Je mu {self.age} let')
        
    def birthday(self):
        self.age += 1
        print(f'Pes {self.name} má {self.age} let')
        
    def info(self):
        if self.kennel:
            print(f'Pes {self.name} je v hotelu {self.kennel.name}')
        else: 
            print(f'Pes {self.name} není v žádném hotelu')
        
        
class Kennel:
    def __init__(self, name: str):
        
        self.name = name
        self.dogs: list[Dog] = []
        
    def add_dog(self, dog):
        
        if not isinstance(dog, Dog):
            raise TypeError("Can add only Dog instances")
        if dog in self.dogs:
            return
        
        dog.kennel = self
        self.dogs.append(dog)
        
    def list_dogs(self):
       
        print(f'V psím hotelu { self.name } jsou tito psi: ')
        
        if not self.dogs:
            print("- žádný pes -")
            return
        
        for dog in self.dogs:
            print(f' - {dog.name}')


            
        
       
       
ben = Dog("Ben", 8)
dan = Dog("Dan", 12)
punta = Dog("Punta", 3)

psi_hotel = Kennel("Alhambra")
psi_hotel.add_dog(ben)
psi_hotel.add_dog(dan)

psi_hotel.list_dogs()

ben.info()
punta.info()


