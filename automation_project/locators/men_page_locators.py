from selenium.webdriver.common.by import By


class MenPageLocators:
    """Object Repository for Login Page Elements."""


    MEN_CATEGORY_LINK = (By.XPATH, "(//ul[@class='nav-pills categorymenu']//li[6])[2]")

    Add_Cream = (By.XPATH, "(//div[@class='pricetag jumbotron']//i)[1]")
    Click_AddCart = (By.XPATH, "//ul[@class='productpagecart']//a")