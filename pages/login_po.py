from locators.auth import Auth

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator(Auth.USERNAME)
        self.password = page.locator(Auth.PASSWORD)
        self.login_button = page.locator(Auth.LOGIN_BUTTON)
        self.title = page.locator(Auth.TITLE)
        self.error = page.locator(Auth.ERROR)

    def navigate(self) -> None:
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
