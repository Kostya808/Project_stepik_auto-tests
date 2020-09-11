from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
	def adding_item_to_the_cart(self):
		button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
		button.click()

	def checking_name_added_product(self):
		product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
		name_appended = self.browser.find_element(*ProductPageLocators.NAME_APPENDED).text
		print(product_name)
		print(name_appended)
		assert product_name == name_appended, "The name of the added file does not match what is expected"

	def checking_basket_price(self):
		price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
		basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
		assert price_product == basket_price, "The basket price does not match the product price"
