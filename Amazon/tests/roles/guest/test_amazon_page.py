from pages.amazon_shoping import AmazonPage
from data import test_data
import pytest
import allure


@pytest.mark.run(order=1)
class Test_Login():
    @allure.title("Add to cart All Samsung mobiles with Price Value greater than 25K and Less than 80K. Move to the checkout screen and update quantity to 5 for any phone model in the cart.")
    def test_case1(self,driver):
        amazon_obj = AmazonPage(driver)
        amazon_obj.case1()

    @allure.title("Add to cart all Samsung mobiles with operating System Android 12. Move to the checkout screen and remove any phone model from the cart.")
    def test_case2(self,driver):
        amazon_obj = AmazonPage(driver)
        amazon_obj.case2()

    @allure.title("Add to cart all Samsung mobiles with free delivery where Price range is less than 50K")
    def test_case3(self,driver):
        amazon_obj = AmazonPage(driver)
        amazon_obj.case3()

