import math
class Car:
    sound="Beep Beep"
    def __init__(self,color,max_speed=0,acceleration=0,tyre_friction=0):
        self._color=color
        if max_speed<0:
            raise ValueError("Invalid value for max_speed")
        
        self._max_speed=max_speed
        if acceleration<0:
            raise ValueError("Invalid value for acceleration")
        self._acceleration=acceleration
        
        if tyre_friction<0:
            raise ValueError("Invalid value for tyre_friction")
        self._tyre_friction=tyre_friction
        
        if acceleration>=self._max_speed:
            self._acceleration=self._max_speed
        self._acceleration=acceleration
    
        self._is_engine_started=False
        self._current_speed=0
        
    @property
    def current_speed(self):
        return self._current_speed
        
    @property   
    def color(self):
        return self._color
        
    @property   
    def is_engine_started(self):
        return self._is_engine_started
        
    @property   
    def max_speed(self):
        return self._max_speed
        
    @property   
    def acceleration(self):
        return self._acceleration
        
    @property   
    def tyre_friction(self):
        return self._tyre_friction
        
    def start_engine(self):
        self._is_engine_started=True
        
    def accelerate(self):
        if self._is_engine_started==True:
            if self._current_speed + self._acceleration<=self._max_speed:
                self._current_speed+=self._acceleration
            else:
                self._current_speed=self._max_speed
        else:
            print("Start the engine to accelerate")
    
    def apply_brakes(self):
    
        self._current_speed-=self._tyre_friction
        if self._current_speed<self._tyre_friction:
            self._current_speed=0
        
    def stop_engine(self):
        if self._is_engine_started==True:
            self._is_engine_started=False

    def sound_horn(self):
        if self._is_engine_started==True:
            print(self.sound)
        else:
            print("Start the engine to sound_horn")

class RaceCar(Car):
    sound="Peep Peep\nBeep Beep"
    def __init__(self,color="red",max_speed=0,acceleration=0,tyre_friction=0):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self._nitro=0
        
    @property
    def nitro(self):
        return self._nitro
        
    def sound_horn(self):
        super().sound_horn()
        
    def apply_brakes(self):
        if self._current_speed>=self._max_speed//2:
            self._nitro+=10
        super().apply_brakes()
        
    def accelerate(self):
        if self._nitro>0:
            self._acceleration+=(math.ceil(self._acceleration*30/100))
            self._nitro-=10
        super().accelerate()
        
'''race=RaceCar("red",250,100,30)
race.start_engine()
race.accelerate()
race.apply_brakes()
#race.accelerate()
race.apply_brakes()
#race.accelerate()
race.apply_brakes()
race.apply_brakes()
print(race._nitro)
print(race._current_speed)'''