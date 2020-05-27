class Item:
    def __init__(self,name=None,price=0,category=None):
        self.name=name
        if price<=0:
            raise ValueError("Invalid value for price, got {}".format(price))
        self.price=price
        self.category=category
        
    def __str__(self):
        return "{}@{}-{}".format(self.name,self.price,self.category)
        
class Query:
    op=["EQ","IN","LT","LTE","GT","GTE","CONTAINS","STARTS_WITH","ENDS_WITH"]

    def __init__(self,field=None,operation=None,value=None):
        self.field=field
        if operation not in self.op:
            raise ValueError("Invalid value for operation, got {}".format(operation))
        self.operation=operation
        self.value=value
    
    def __str__(self):
        return f'{self.field} {self.operation} {self.value}'

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
       
        for item in self._items:
            if query.operation=="IN" and getattr(item,query.field) in query.value:
                items1.add_item(item)
            elif query.operation=="EQ" and  getattr(item,query.field) == query.value:
                items1.add_item(item)
            elif query.operation=="GT" and getattr(item,query.field) > query.value:
                items1.add_item(item)
            elif query.operation=="GTE" and getattr(item,query.field) >= query.value:
                items1.add_item(item)
            elif query.operation=="LT" and getattr(item,query.field) < query.value:
                items1.add_item(item)
            elif query.operation=="LTE" and getattr(item,query.field) <= query.value:
                items1.add_item(item)
            elif (query.operation=="STARTS_WITH" or query.operation=="ENDS_WITH" or query.operation=="CONTAINS") and (query.value) in getattr(item,query.field):
                items1.add_item(item)
        return items1        
        
    def exclude(self,query):
        items1=Store()
       # exclude=filter(self,query)
        for item in self._items:
            if item not in self.items1:
                items1.add_item(item)
        return items1
            
                
        
            
                   
  
        
    
    
    def count(self):
            return len(self._items)
    
s=Store()
i=Item("oreo",30,"Food")
i1=Item("good day",20,"Food")
i2=Item("soap",40,"kit")
s.add_item(i)
s.add_item(i1)
s.add_item(i2)
query = Query(field="price", operation="GT", value=30)  
r=s.exclude(query)
print(r)
