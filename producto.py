class Producto:
    def __init__(self,p_nombre,p_precio,p_categoria,p_sku):
        self.nombre=p_nombre
        self.precio=p_precio
        self.categoria=p_categoria
        self.sku=p_sku
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.precio+=self.precio*percent_change
        else: 
            self.precio-=self.precio*percent_change
    def print_info(self):
        print(f"Nombre:{self.nombre}, Precio:{self.precio}, Categoria:{self.categoria}, Codigo:{self.sku}")
