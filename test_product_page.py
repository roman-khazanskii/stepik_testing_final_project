from .pages.product_page import ProductPage
import pytest

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  # pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
    # # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    # # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    # page = ProductPage(browser, link)   
    # # открываем страницу
    # page.open()                      
    # # пытаемся добавить товар в корзину
    # page.add_to_basket_promo()       
    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):     
    # Открываем страницу товара 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   
    page.open()                      
    # Добавляем товар в корзину 
    page.add_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.check_success_message_not_present()
    
def test_guest_cant_see_success_message(browser): 
    #Открываем страницу товара 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   
    page.open()                      
    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.check_success_message_not_present()
    
def test_message_disappeared_after_adding_product_to_basket(browser): 
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   
    page.open()                      
    # Добавляем товар в корзину
    page.add_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page.check_success_message_disappeared()