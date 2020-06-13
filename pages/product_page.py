from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException 
from selenium.common.exceptions import NoSuchElementException 

import math
import time

class ProductPage(BasePage):
    def add_to_basket(self):
        
        expected_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        expected_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        
        print(f"Exp Name = {expected_product_name}, exp price = {expected_product_price}")
        
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        btn.click()
        
    def check_success_message_not_present(self):
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message should not appear"
        
    def check_success_message_disappeared(self):
        # Проверяем, что сообщение об успехе пропадает
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message should disappear"

    def add_to_basket_promo(self):
        
        expected_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        expected_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        
        print(f"Exp Name = {expected_product_name}, exp price = {expected_product_price}")
        
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        btn.click()
        
        # получаем код, которым доказываем, что мы не человек
        self.solve_quiz_and_get_code()
                
        # название товара в корзине должно совпадать с добавляемым
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert expected_product_name == added_product_name, "Added product is not the one that was supposed to be added!"
        
        # и полная цена корзины из одного товара должна совпадать с ценой товара
        total_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        assert expected_product_price == total_price, "Total price is not equal to product price"
       
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        time.sleep(1)
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
