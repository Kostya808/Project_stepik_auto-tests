from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
	def should_not_be_item(self):
   		assert self.is_not_element_present(*BasketPageLocators.ITEM), "Items in cart is presented, but should not be"

	def cart_empty_message(self):
   		assert self.is_element_present(*BasketPageLocators.CART_IS_EMPTY_TEXT), "No message about empty cart"
