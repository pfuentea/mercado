from producto import Producto
from tienda import Tienda



tableton=Producto('Tabletón',2000,'Galletitas','1010')
competa=Producto('Galletas Competa',1000,'Galletitas','1020')
fruna=Tienda('Fruna')
fruna.add_product(tableton)
fruna.add_product(competa)
fruna.vitrina()  

fruna.sell_product_by_sku ('1010')  
fruna.vitrina()