from playwright.sync_api import expect
from pages.login_po import LoginPage
from pages.products_po import ProductsPage
from pages.cart_po import CartPage

def test_add_one_to_cart(page):
    login_page = LoginPage(page)
    productsPage = ProductsPage(page)
    cartPage = CartPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    expect(productsPage.count_in_cart).to_be_hidden()
    productsPage.add_to_cart()
    expect(productsPage.count_in_cart).to_be_visible()
    expect(productsPage.count_in_cart).to_contain_text("1")

    productsPage.go_to_cart()
    expect(cartPage.price).to_be_visible()
