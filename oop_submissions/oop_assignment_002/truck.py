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
    
    
class Truck(Car):
    sound="Honk Honk"
    def __init__(self,color="red",max_speed=0,acceleration=0,tyre_friction=0,max_cargo_weight=0):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self._max_cargo_weight=max_cargo_weight
        self._cargo_weight=0
        
    @property
    def cargo_weight(self):
        return self._cargo_weight
        
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
    
    def load(self,load):
        if self._is_engine_started==False:
            if load<0:
                raise ValueError("Invalid value for cargo_weight")
            
            if self._current_speed==0:
                   
                if self._cargo_weight+load<=self._max_cargo_weight:
                    self._cargo_weight+=load
                else:
                    print("Cannot load cargo more than max limit: {}".format(self._max_cargo_weight))
            else:
                print("Cannot load cargo during motion")  
        else:
            if load<0:
                raise ValueError("Invalid value for cargo_weight")
            if self._current_speed==0:
                if self._cargo_weight+load<=self._max_cargo_weight:
                    self._cargo_weight+=load
                else:
                    print("Cannot load cargo more than max limit: {}".format(self._max_cargo_weight))
            else:
                print("Cannot load cargo during motion")
    def unload(self,load):
        if self._is_engine_started==False:
            if load<0:
                raise ValueError("Invalid value for cargo_weight")
            self._cargo_weight-=load
        else:
            if self._current_speed==0:
                self._cargo_weight-=load
            else:
                print("Cannot unload cargo during motion")
                
    def sound_horn(self):
        super().sound_horn()
            
        
        
    
    
        
        
        
        
    