class Zoo:
    animals=[]
    
    def __init__(self):    
        self._reserved_food_in_kgs=0
        self._anm=[]
        
    @property
    def anm(self):
        return self._anm
        
    def add_food_to_reserve(self,food):
        self._reserved_food_in_kgs+=food
        
    def add_animal(self,animal):
        self._anm.append(animal)
        self.animals.append(animal)
        
    @property  
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
  
    def count_animals(self):
        return len(self._anm)
        
    @classmethod
    def count_animals_in_all_zoos(cls):
        return len(cls.animals)
     
        
        
    @staticmethod    
    def count_animals_in_given_zoos(zoos):
        all_animals=0
        for zoo in zoos:
            l=len(zoo.anm)
            all_animals+=l
        return all_animals
        
    
   
    def feed(self,animal):
        if self._reserved_food_in_kgs<=0:
            return "add_food_to_reserve"
        self._reserved_food_in_kgs-=animal._required_food_in_kgs
        animal.grow()
    

class Deer:
    sound="Buck Buck"
    breath="Breathe in air"
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
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=2
    @classmethod
    def make_sound(cls):
        print(cls.sound)
    @classmethod
    def breathe(cls):
        print(cls.breath)
    
    
    
class Lion:
    sound="Roar Roar"
    breath="Breathe in air"
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
        
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=4
        
    @classmethod
    def make_sound(cls):
        print(cls.sound)
        
    @classmethod
    def breathe(cls):
        print(cls.breath)
    
    def hunt(self,zoo):
        for i in zoo.anm:
            if "Deer" in str(i): 
                zoo.anm.remove(i)
                break
        else:
            print("No deers to hunt")
            
   
    
    
class Shark:
    sound="Shark Sound"
    breath="Breathe oxygen from water"
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
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=8
    @classmethod
    def make_sound(cls):
        print(cls.sound)
    @classmethod
    def breathe(cls):
        print(cls.breath)
        
    def hunt(self,zoo):
        for i in zoo.anm:
            if "GoldFish" in str(i): 
                zoo.anm.remove(i)
                break
        else:
            print("No GoldFish to hunt")
            
    
    
    
    
class GoldFish:
    sound="Hum Hum"
    breath="Breathe oxygen from water"
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
        
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=0.2
    
    @classmethod
    def make_sound(cls):
        print(cls.sound)
    @classmethod
    def breathe(cls):
        print(cls.breath)



class Snake:
    
    sound="Hiss Hiss"
    breath="Breathe in air"
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
        
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=0.5
        
    @classmethod
    def make_sound(cls):
        print(cls.sound)
        
    @classmethod
    def breathe(cls):
        print(cls.breath)
        
    def hunt(self,zoo):
        for i in zoo.anm:
            if "Deer" in str(i): 
                zoo.anm.remove(i)
                break
        else:
            print("No deers to hunt")
            

