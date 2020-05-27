class Pokemon:
    c=0
    sound=""
    Pokemon_name=""
    def __init__(self,name,level):
        if name=="":
            raise ValueError("name cannot be empty")
        self._name=name
        if level<=0:
            raise ValueError("level should be > 0")
        self._level=level
        self._master=None
        
    
        
    @property
    def name(self):
        return self._name
        
    @property
    def level(self):
        return self._level
        
    @property
    def master(self):
        if self._master==None:
            print("No Master")
        else:
            return self._master
        
    @classmethod    
    def make_sound(cls):
        print(cls.sound)
        
    @classmethod   
    def run(cls):
        print("{} running...".format(cls.Pokemon_name))   
        
    @classmethod
    def swim(cls,pokemon):
        '''if pokemon.isinstance(Water_pokemon):'''
        print("{} swimming...".format(cls.Pokemon_name))  
        '''else:
            print("it cannot swim")'''
            
            
        
         
    @classmethod
    def fly(cls):
        print("{} flying...".format(cls.Pokemon_name))  
    
        
    def __str__(self):
        return("{} - Level {}".format(self._name,self._level))
        
'''class Water_pokemon(Pokemon):
    @classmethod
    def swim(cls):
        print("{} swimming...".format(cls.Pokemon_name))  
    '''
    
    
    
class Pikachu(Pokemon):
    
    sound="Pika Pika"
    Pokemon_name="Pikachu"
    
    def attack(self):
        print("Electric attack with {} damage".format(self._level*10))
        
        
class Squirtle(Pokemon):
    sound="Squirtle...Squirtle"
    Pokemon_name="Squirtle"
    def attack(self):
        print("Water attack with {} damage".format(self._level*9))
    
class Pidgey(Pokemon):
    sound="Pidgey...Pidgey"
    Pokemon_name="Pidgey"
    def attack(self):
        print("Air attack with {} damage".format(self._level*5))
        
class Swanna(Pokemon):
    sound="Swanna...Swanna"
    Pokemon_name="Swanna"
    def attack(self):
        print("Water attack with {} damage".format(self._level*9))
        print("Air attack with {} damage".format(self._level*5))
        
class Zapdos(Pokemon):
    sound="Zap...Zap"
    Pokemon_name="Zapdos"
    def attack(self):
        print("Electric attack with {} damage".format(self._level*10))
        print("Air attack with {} damage".format(self._level*5))
    


class Island:
    islands_list=[]
    pokemon_list=[]
    def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs):
        self._name=name
        self._max_no_of_pokemon=max_no_of_pokemon
        self._total_food_available_in_kgs=total_food_available_in_kgs
        self._pokemon_left_to_catch=0
        self.islands_list.append(self)
       
    @property
    def name(self):
        return self._name
        
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
        
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
    
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
    
    def add_pokemon(self,pokemon):
        if self._pokemon_left_to_catch < self._max_no_of_pokemon:
            self.pokemon_list.append(pokemon)
            self._pokemon_left_to_catch+=1
        elif self._pokemon_left_to_catch == self._max_no_of_pokemon:
            print("Island at its max pokemon capacity")
            
    def __str__(self):
        return ("{} - {} pokemon - {} food".format(self._name,self._pokemon_left_to_catch,self._total_food_available_in_kgs))
  
    @classmethod
    def get_all_islands(cls):
        return cls.islands_list
        
class Trainer:
    
    moved_islands=[]
    def __init__(self,name):
        self._name=name
        self._experience=100
        self._max_food_in_bag=10*self._experience
        self._food_in_bag=0
        self._current_island=None
        self._is_on_island=False
        self.caught_pokemon_list=[]
    @property
    def name(self):
        return self._name
    @property
    def experience(self):
        return self._experience
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
    @property
    def food_in_bag(self):
        return self._food_in_bag
        
    @property
    def current_island(self):
        if self._current_island==None:
            print("You are not on any island")
        else:
            return self._current_island
                
        
    def __str__(self):
        return self._name
        
    def move_to_island(self,island):
        self._current_island=island
        self._is_on_island=True
        
    def collect_food(self):
        if self._is_on_island==True:
            if self.food_in_bag==self.max_food_in_bag:
                pass
            elif self._max_food_in_bag < self.current_island._total_food_available_in_kgs:
                self._food_in_bag+=self._max_food_in_bag
                self.current_island._total_food_available_in_kgs-=self._food_in_bag
            else:
                self._food_in_bag+=self.current_island._total_food_available_in_kgs
                self.current_island._total_food_available_in_kgs=0
        else:
            print("Move to an island to collect food")
            
    def catch(self,pokemon):
        if self._experience>=100*pokemon.level:
            print("You caught {}".format(pokemon.name))
            self._experience+=20*pokemon.level
            self.caught_pokemon_list.append(pokemon)
            pokemon._master=self
        else:
            print("You need more experience to catch {}".format(pokemon.name))
    def get_my_pokemon(self):
        return self.caught_pokemon_list
    
        
i = Island(name="Island1", max_no_of_pokemon=5, total_food_available_in_kgs=10000)        
t=Trainer("ram")
i1= Island(name="Island2", max_no_of_pokemon=5, total_food_available_in_kgs=10000)        
i2= Island(name="Island3", max_no_of_pokemon=5, total_food_available_in_kgs=10000)        
'''print(t)
t.collect_food()
t.move_to_island(i1)
print(t.food_in_bag)
#print(t.current_island==i1)
print(t.current_island)
print(i.total_food_available_in_kgs)
#print(Island.islands_list)
print(t.get_my_pokemon())'''
Pokemon.swim_or_not(Pikachu)

q="select date,(select sum(positive) from covid),(select sum(deaths) from covid) where date=18 group by date;"