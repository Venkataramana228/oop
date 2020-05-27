import math
class ComplexNumber:
    def __init__(self,real_part=0,imaginary_part=0):
        if type(real_part)==str and type(imaginary_part)==str:
            raise ValueError("Invalid value for real and imaginary part")
        elif type(real_part)==str:
            raise ValueError("Invalid value for real part")
        elif type(imaginary_part)==str:
            raise ValueError("Invalid value for imaginary part")
        self._real_part=real_part
        self._imaginary_part=imaginary_part
        
    @property
    def real_part(self):
        return self._real_part
    @property
    def imaginary_part(self):
        return self._imaginary_part
    
    def __str__(self):
        if self._imaginary_part<0:
            return ("{}-{}i".format(self._real_part,self._imaginary_part))
        else:
            return ("{}+{}i".format(self._real_part,self._imaginary_part))
            
    def conjugate(self):
        return ComplexNumber(self._real_part,-self._imaginary_part)
        
    def __add__(self,other):
        self.res_real=self._real_part+other._real_part
        self.res_img=self._imaginary_part+other._imaginary_part
        return ComplexNumber(self.res_real,self.res_img)
        
    def __sub__(self,other):
        self.res_real=self._real_part-other._real_part
        self.res_img=self._imaginary_part-other._imaginary_part
        return ComplexNumber(self.res_real,self.res_img)
    def __mul__(self,other):
        self.res_real=self._real_part*other._real_part - self._imaginary_part*other._imaginary_part
        self.res_img=self._real_part*other._imaginary_part + self._imaginary_part*other._real_part
       
        return ComplexNumber(self.res_real,self.res_img)
        
    def __truediv__(self,other):
        self.res_real=self._real_part*other._real_part + self._imaginary_part*other._imaginary_part
        self.res_img=self._imaginary_part*other._real_part - self._real_part*other._imaginary_part
        self.den=other._real_part**2+other._imaginary_part**2
        return ComplexNumber(self.res_real/self.den,self.res_img/self.den)
        
    def __abs__(self):
        self.res=math.sqrt(self._real_part**2 + self._imaginary_part**2)
        return round(self.res,3)
        
    def __eq__(self,other):
        if self._real_part==other._real_part and self._imaginary_part==other._imaginary_part:
            return True
        else:
            return False
        
        
    
    
        
    
class Item:
    def __init__(self,name=None,price=0,category=None):
        self._name=name
        if price<=0:
            raise ValueError("Invalid value for price, got {}".format(price))
        self._price=price
        self._category=category
        
    def __str__(self):
        return "{}@{}-{}".format(self._name,self._price,self._category)
        
class Query:
    op=["EQ","IN","LT","LTE","GT","GTE","CONTAINS","STARTS_WITH","ENDS_WITH"]

    def __init__(self,field=None,operation=None,value=None):
        self._field=field
        if operation not in self.op:
            raise ValueError("Invalid value for operation, got {}".format(operation))
        self._operation=operation
        self._value=value
    
    def __str__(self):
        return f'{self._field} {self._operation} {self._value}'

class Store:
    
    def __init__(self):
        self._items=[]

    def add_item(self,item):
        self._items.append(item)

        
    def __str__(self):
        if len(self._items)!=0:
            return "\n".join([str(x) for x in self._items])
        else:
            return "No items"
    
    def filter(self,query):
        items1=Store()
        if query._operation=="IN":
            for item in self._items:
                if item._name in query._value:
                    items1.add_item(item)
                elif item._category in query._value:
                    items1.add_item(item)
                elif item._price in query._value:
                    items1.add_item(item)

        
        elif query._operation=="EQ":
            for item in self._items:
                if query._field=="price" or query._field=="name" or query._field=="category":
                    if item._name == query._value:
                        items1.add_item(item)
                    elif item._category == query._value:
                        items1.add_item(item)
                    elif item._price == query._value:
                        items1.add_item(item)

            
        elif query._operation=="GT":
            for item in self._items:
                if query._field=="price":
                    if item._price > query._value:
                       items1.add_item(item) 
                       
        elif query._operation=="GTE":
            for item in self._items:
                if query._field=="price":
                    if item._price >= query._value:
                        items1.add_item(item)
               
        elif query._operation=="LT":
            for item in self._items:
                if query._field=="price":
                    if item._price < query._value:
                        items1.add_item(item)
            
        elif query._operation=="LTE":
            for item in self._items:
                if query._field=="price":
                    if item._price <= query._value:
                        items1.add_item(item)
            
               
        elif query._operation=="STARTS_WITH":
            for item in self._items:
                if query._field=="name" or query._field=="category":
                    if item._name.startswith(query._value) or item._category.startswith(query._value):
                        items1.add_item(item)
            
            
        elif query._operation=="ENDS_WITH":
            for item in self._items:
                if query._field=="name" or query._field=="category":
                    if item._name.endswith(query._value) or item._category.endswith(query._value):
                        items1.add_item(item)
                    
        
        elif query._operation=="CONTAINS":
            for item in self._items:
                if query._field=="name":
                    if query._value in item._name:
                        items1.add_item(item)
                elif query._field=="category":
                    if  query._value in item._category:
                        items1.add_item(item)
        return items1
        
        
    def exclude(self,query):
        items1=Store()
        if query._operation=="IN":
            for item in self._items:
                if query._field=="name":
                    if item._name  not in query._value:
                        items1.add_item(item)
                elif query._field=="category":
                    if item._category not in query._value:
                        items1.add_item(item)
                elif query._field=="price":
                    if item._price not in query._value:
                        items1.add_item(item)

        
        elif query._operation=="EQ":
            for item in self._items:
                if (query._field=="price"):
                    if item._price != query._value:
                        items1.add_item(item)
                        
                elif query._field=="name":
                    if item._name != query._value:
                        items1.add_item(item)
                        
                elif query._field=="category":
                    if item._category != query._value:
                        items1.add_item(item)

            
        elif query._operation=="GT":
            for item in self._items:
                if query._field=="price":
                    if not(item._price > query._value):
                        items1.add_item(item)
           
            
        elif query._operation=="GTE":
            for item in self._items:
                if query._field=="price":
                    if not(item._price >= query._value):
                        items1.add_item(item)
                    

               
        elif query._operation=="LT":
            for item in self._items:
                if query._field=="price":
                    if not(item._price < query._value):
                        items1.add_item(item)
            
            
        elif query._operation=="LTE":
            for item in self._items:
                if query._field=="price":
                    if not(item._price <= query._value):
                        items1.add_item(item)
                    
               
        elif query._operation=="STARTS_WITH":
            for item in self._items:
                if query._field=="name" or query._field=="category":
                    if not(item._name.startswith(query._value) or item._category.startswith(query._value)):
                       items1.add_item(item)
            
            
        elif query._operation=="ENDS_WITH":
            for item in self._items:
                if query._field=="name" or query._field=="category":
                    if not(item._name.endswith(query._value) or item._category.endswith(query._value)):
                       items1.add_item(item)
                    
        
        elif query._operation=="CONTAINS":
            for item in self._items:
                if query._field=="name":
                    if query._value not in item._name:
                        items1.add_item(item)
                elif query._field=="category":
                    if  query._value not in item._category:
                        items1.add_item(item)
        return items1
    
    def count(self):
            return len(self._items)
    
               
