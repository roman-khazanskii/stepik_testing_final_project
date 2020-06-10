from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    
    # holy smokes this is ugly
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "div#messages > div:nth-child(1) > div > strong")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, "div#messages > div:nth-child(3) > div > p > strong")