from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestItems:
    def test_item_has_btn_add_to_basket(self, browser):
        browser.get(link)
        button_add_to_basket = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        assert button_add_to_basket.is_displayed(), "The add to basket button should be displayed"

