from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time

PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.registered_user
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # открыть страницу регистрации
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        # зарегистрировать нового пользователя
        email: str = str(time.time()) + "@fakemail.org"
        password = "7NZ25eE267Z2BmK"
        page.register_new_user(email, password)
        # проверить, что пользователь залогинен
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        # Открываем страницу товара 
        page = ProductPage(browser, PRODUCT_LINK)
        page.open()
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        page.check_success_message_not_present()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = ProductPage(browser, PRODUCT_LINK)
        # открываем страницу
        page.open()
        # пытаемся добавить товар в корзину
        page.add_to_basket()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket_promo(browser, link):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page = ProductPage(browser, link)
    # открываем страницу
    page.open()
    # пытаемся добавить товар в корзину
    page.add_to_basket_promo()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page = ProductPage(browser, link)
    # открываем страницу
    page.open()
    # пытаемся добавить товар в корзину
    page.add_to_basket_promo()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):

    page = ProductPage(browser, PRODUCT_LINK)
    page.open()

    page.go_to_login_page()

    page = LoginPage(browser, browser.current_url)
    page.should_be_login_page()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Открываем страницу товара 
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    # Добавляем товар в корзину 
    page.add_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.check_success_message_not_present()


def test_guest_cant_see_success_message(browser):
    # Открываем страницу товара
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.check_success_message_not_present()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    # Добавляем товар в корзину
    page.add_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page.check_success_message_disappeared()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Гость открывает страницу товара
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    # Переходит в корзину по кнопке в шапке 
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    # Ожидаем, что в корзине нет товаров
    # Ожидаем, что есть текст о том что корзина пуста
    page.check_basket_empty()
