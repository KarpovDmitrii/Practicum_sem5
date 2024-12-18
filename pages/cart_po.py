from locators.cart import Cart

class CartPage:
    def __init__(self, page):
        self.page = page
        self.price = page.locator(Cart.PRICE)
