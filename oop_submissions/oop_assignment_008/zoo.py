class Animals:
    sound=""
    breath=""
    increment_food_in_kgs=0
    def __init__(self,age_in_months=0, breed=None, required_food_in_kgs=0):
        if age_in_months!=1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        self._age_in_months=age_in_months
        
        self._breed=breed
        if required_food_in_kgs<=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        self._required_food_in_kgs=required_food_in_kgs
        
    @property
    def age_in_months(self):
        return self._age_in_months
        
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
        
    @property
    def breed(self):
        return self._breed
        
    @classmethod
    def make_sound(cls):
        print(cls.sound)
    @classmethod
    def breathe(cls):
        print(cls.breath)
        
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=self.increment_food_in_kgs
          
    
class HuntAnimals:
    hunt_animal=""
    hunt_animal_name=""
    def hunt(self,zoo):
        for animal in zoo.animal_list:
            if self.hunt_animal in str(animal): 
                zoo.animal_list.remove(animal)
                break
        else:
            print("No {} to hunt".format(self.hunt_animal_name))
            

    
class Deer(Animals):
    sound="Buck Buck"
    breath="Breathe in air"
    increment_food_in_kgs=2
    
class Lion(Animals,HuntAnimals):
    sound="Roar Roar"
    breath="Breathe in air"
    increment_food_in_kgs=4
    hunt_animal="Deer"
    hunt_animal_name="deers"

class Shark(Animals,HuntAnimals):
    sound="Shark Sound"
    breath="Breathe oxygen from water"
    increment_food_in_kgs=8
    hunt_animal="GoldFish"
    hunt_animal_name ="GoldFish"

    
class GoldFish(Animals):
    sound="Hum Hum"
    breath="Breathe oxygen from water"
    increment_food_in_kgs=0.2
    
class Snake(Animals,HuntAnimals):
    sound="Hiss Hiss"
    breath="Breathe in air"
    increment_food_in_kgs=0.5
    hunt_animal="Deer"
    hunt_animal_name="deers"
    
class Zoo:
    all_animals=[]
    
    def __init__(self):    
        self._reserved_food_in_kgs=0
        self._animal_list=[]
        
    @property
    def animal_list(self):
        return self._animal_list
        
    @property  
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
        
    def add_food_to_reserve(self,food):
        self._reserved_food_in_kgs+=food
        
    def add_animal(self,animal):
        self._animal_list.append(animal)
        self.all_animals.append(animal)
    
  
    def count_animals(self):
        return len(self._animal_list)
        
    @classmethod
    def count_animals_in_all_zoos(cls):
        return len(cls.all_animals)
     
    @staticmethod    
    def count_animals_in_given_zoos(zoos):
        animals=0
        for zoo in zoos:
            l=len(zoo.animal_list)
            animals+=l
        return animals
        
    def feed(self,animal):
        #if self._reserved_food_in_kgs<=0:
            #return "add_food_to_reserve"
        if self._reserved_food_in_kgs>0:  
            self._reserved_food_in_kgs-=animal.required_food_in_kgs
            animal.grow()
        
z=Zoo()
deer=Deer(1,"elk",10)
lion=Lion(1,"elk",20)
z.add_animal(deer)
z.add_animal(lion)
deer.grow()
z.add_food_to_reserve(1000)
z.feed(deer)
#print(z.reserved_food_in_kgs)
print(Zoo.count_animals_in_all_zoos())
