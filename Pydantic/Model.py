from pydantic import BaseModel,Field,field_validator,model_validator,computed_field,ConfigDict
from typing import Optional,Literal

class Category(BaseModel): #defines specific field data only accepted
    name: Literal['starter','main course','beverage']

class Model(BaseModel):
    #when user sends the extra field in that case what to do that decides the model_config 
    model_config = ConfigDict(

        extra = 'add', #allow = add the extra field,forbid = raise error,ignore = just ignore it
        frozen = True, # freez the model 
        strict = False, # sometimes pydantic auto covert data like str into int if strict is true it will not convert itself  
        validate_assignment = True #validate all fields on edit of one field 
    )

    id : int
    name: str  = Field(...,min_length=3,max_length = 50,description='name field.') # required Field
    price : float
    category : Category
    is_available: bool
    description: Optional[str] = None #optional Field

    #field validator 
    @field_validator('name') #PANNer TikkA --> Panner Tikka
    @classmethod

    def title_name(cls,value):
        return value.title()
    
    #Model Validator -> checks more than one field
    @model_validator(mode = 'after')
    def check_available(self):
        if self.is_available and self.price <=0:
            raise('available items price must be greater than 0')
        return self

    #computed Fields -> populate field on execution automatically
    @computed_field
    @property

    def price_with_tax(self) -> float:
        return round(self.price * 10.5,2)


item = Model(id= 3,name='PaNNer TiKKA',price = 10,category = Category(name = 'main course'),is_available = True,spicy = False) 
print('#####--Original Item--######')
print(item)
print('##############################')

print('#####--IN Serialization--> Object into ->> Dictionary ######')
print(item.model_dump())
print('##############################')

print('#####--OUT Serialization--> Object into ->> JSON ######')
print(item.model_dump_json())


