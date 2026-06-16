from fastapi import FastAPI
from models import Product
app = FastAPI()

@app.get('/') # decorator for the path operation')
def greet():
    return 'welcome to fastapi world..'


products = [

        Product(id= 1,name='sample',description = 'this is a sample product',price = 12,quantity =5),
        Product(id= 2,name='sample2',description = 'this is a sample product2',price = 15,quantity =10),
        Product(id=3,name='sample3',description = 'this is a sample product3',price = 20,quantity =15),
        Product(id=4,name='sample4',description = 'this is a sample product4',price = 25,quantity =20),
        Product(id=5,name='sample5',description = 'this is a sample product5',price = 30,quantity =25)
       
]

@app.get('/products')
def products_data():
    return products

@app.get('/product/{id}') # path parameter
def get_prduct(id : int):

    for product in products:
        if product.id == id:
            return product[id-1]
        else:
            return 'product not found'

@app.post('/product')
def add_product(product: Product): #Product is a pydantic model
    products.append(product)
    

@app.put('/update-product')
def update_product(id: int ,updated_product:Product):
    for i in range(len(products)):
        if products[i].id == id:
            updated_product.id == id # ensures id stays same in update operation
            products[i] = updated_product
            return {"message":"Updated Sucessfully"}
    
    return {"message": "Product not found"}