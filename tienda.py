class Tienda:
    def __init__(self,p_nombre):
        self.nombre=p_nombre
        self.productos=[]
    def add_product (self, new_product) :
        self.productos.append(new_product)
        return self
    def sell_product (self, id) :
        #self.productos[id]=self.productos[len(self.productos)-1]
        self.productos.pop(id)
        return self
    def sell_product_by_sku (self, p_sku) :
        self.productos=list(filter(lambda x:x.sku!=p_sku,self.productos))        
        return self
    def inflation(self, percent_increase):
        for item in self.productos:
            item.update_price(percent_increase,True)
        return self
    def set_clearance (self, category, percent_discount):
        for item in self.productos:
            if item.categoria==category:
                item.update_price(percent_discount,False)
        return self
    def vitrina(self):
        print(f"Productos de la tienda {self.nombre}:")
        for item in self.productos:
            item.print_info()
        return self


