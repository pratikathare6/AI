from fastapi import Depends,FastAPI
from models import Product
from database import session,engine
import database_model_sqlalchemy   #import sqlalchamey model
from sqlalchemy.orm import Session

app = FastAPI()

products = [

        Product(id= 1,name='sample',description = 'this is a sample product',price = 12,quantity =5),
        Product(id= 2,name='sample2',description = 'this is a sample product2',price = 15,quantity =10),
        Product(id=3,name='sample3',description = 'this is a sample product3',price = 20,quantity =15),
        Product(id=4,name='sample4',description = 'this is a sample product4',price = 25,quantity =20),
        Product(id=5,name='sample5',description = 'this is a sample product5',price = 30,quantity =25)
       
]

#Reusable function to connect DB and close db session
def get_db():
    db = session()
    try: 
        yield db
    finally:
        db.close()

#############################---Add using the sqlalchemy in postgresql ----##########################
database_model_sqlalchemy.Base.metadata.create_all(bind=engine) #create the table in database

db = session()

def insert_data():

    count =  db.query(database_model_sqlalchemy.Product).count()
        
    if count == 0:
        for product in products:
            db.add(database_model_sqlalchemy.Product(**product.model_dump()))#convert pydantic object to sqlalchemy model
            #returns the dictionary (object) ** converts it into name='phone' price = 5000
        db.commit()
        db.close()

insert_data()






#######################-- Add or modify data using in memory storage --###############################

@app.get('/') # decorator for the path operation')
def greet():
    return 'welcome to fastapi world..'



@app.get('/products')
def products_data(db:Session = Depends(get_db)): #dependancy injection
    
    db_products = db.query(database_model_sqlalchemy.Product).all()
    return db_products



# @app.get('/product/{id}') # path parameter
# def get_prduct(id : int):

#     for product in products:
#         if product.id == id:
#             return product[id-1]
#         else:
#             return 'product not found'

@app.get('/product/{id}')
def get_product_db(id: int, db:Session = Depends(get_db)):
    db_product  = db.query(database_model_sqlalchemy.Product).filter(database_model_sqlalchemy.Product.id == id).all()

    if db_product:
        return db_product     
    return "Product not found"

    
# @app.post('/product')
# def add_product(product: Product): #Product is a pydantic model
#     products.append(product)

@app.post('/product')
def add_product_db(product: Product, db:Session = Depends(get_db)):
    db.add(database_model_sqlalchemy.Product(**product.model_dump()))
    db.commit()
    return product

    

# @app.put('/update-product')
# def update_product(id: int ,updated_product:Product):
#     for i in range(len(products)):
#         if products[i].id == id:
#             updated_product.id == id # ensures id stays same in update operation
#             products[i] = updated_product
#             return {"message":"Updated Sucessfully"}
    
#     return {"message": "Product not found"}


@app.put('/update-product/{id}')
def update_product_db(id: int, product:Product, db:Session = Depends(get_db)):
    db_product = db.query(database_model_sqlalchemy.Product).filter(database_model_sqlalchemy.Product.id == id).first()

    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return 'Product Updated'
    else:
        return 'No product found'



# @app.delete('/delete-product')
# def delete_product(id:int):
#     for i in range(len(products)):
#         if products[i].id == id:
#             del products[i]
#             return {"messgae":"product deleted.."}
        
#     return {"message":"Product not found"}

@app.delete('/delete-product')
def delete_product_db(id: int, db:Session = Depends(get_db)):
    db_product = db.query(database_model_sqlalchemy.Product).filter(database_model_sqlalchemy.Product.id == id).first()

    if db_product:
        db.delete(db_product)
        db.commit()
        return 'Product Deleted'
    else:
        return 'Product not found'
