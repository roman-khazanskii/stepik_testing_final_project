from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self                       
    def test_guest_can_go_to_login_page(self, browser):     
        link = "http://selenium1py.pythonanywhere.com/"
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page = MainPage(browser, link)   
        # открываем страницу
        page.open()                      
        # выполняем метод страницы - переходим на страницу логина
        page.go_to_login_page()          

        page = LoginPage(browser, browser.current_url)
        page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # Гость открывает главную страницу 
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    #Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    #Ожидаем, что в корзине нет товаров
    #Ожидаем, что есть текст о том что корзина пуста 
    page.check_basket_empty()