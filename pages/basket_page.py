from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def check_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket should be empty"
        assert self.is_element_present(
            *BasketPageLocators.BASKET_EMPTY_TEXT), "'Basket is empty' text should be present"

        empty = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text
        assert "basket is empty" in empty, "Page should contain a message about empty basket"
