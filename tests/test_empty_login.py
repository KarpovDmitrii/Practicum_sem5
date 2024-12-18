from playwright.sync_api import expect
from pages.login_po import LoginPage

def test_empty_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("", "")
    expect(login_page.error).to_contain_text("Epic sadface: Username is required")
