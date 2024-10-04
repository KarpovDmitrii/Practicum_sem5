from locators.products import Products

class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart_button = page.locator(Products.ADD_TO_CART_BUTTON)
        self.go_to_cart_link = page.locator(Products.GO_TO_CART_LINK)
        self.count_in_cart = page.locator(Products.COUNT_IN_CART)

    def add_to_cart(self) -> None:
        self.add_to_cart_button.click()

    def go_to_cart(self) -> None:
        self.go_to_cart_link.click()