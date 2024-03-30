from user import User
from cart import Cart
from wallet import Wallet

class Customer:
    def __init__(self, name):
        self.name = name
        self.wallet = Wallet(self)  # Inicializar la billetera con el propietario como argumento.
        self.cart = Cart(self)  # Inicializar el carrito con el propietario como argumento.

    def show_items(self):
        # Mostrar los elementos seleccionados por el cliente
        self.cart.show_items()