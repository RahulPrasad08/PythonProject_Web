from pages.base_page import BasePage
from locators.men_page_locators import MenPageLocators

class MenPage(BasePage):
    """Action methods for the Login / Account Page."""


    def add_to_cart(self):
            self.click(MenPageLocators.MEN_CATEGORY_LINK)
            self.click(MenPageLocators.Add_Cream)
            self.click(MenPageLocators.Click_AddCart)

