from .common_ops import CommonOps
from data import test_data
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AmazonPage(CommonOps):

    cart = (By.XPATH,'//span[@class="cart-icon"]')
    search = (By.XPATH,'//input[@placeholder="Search in Daraz"]')
    min_price = (By.XPATH,'//input[@placeholder="Min"]')
    max_price = (By.XPATH,'//input[@placeholder="Max"]')
    apply_button = (By.XPATH,'//button[normalize-space()="Apply"]')
    product_select = (By.XPATH,'//div[@data-qa-locator="general-products"]/div[1]//div[@id="id-product-img"]')
    increase_quantity = (By.XPATH,'//span[@class="next-number-picker-handler-up-inner"]')
    add_to_cart_button = (By.XPATH,'//button/span[normalize-space()="Add to Cart"]')
    go_to_cart_button = (By.XPATH,'//button[normalize-space()="GO TO CART"]')
    clear_cart = (By.XPATH,'//span[@class="automation-btn-delete"]')
    remove_button = (By.XPATH,'//button[normalize-space()="REMOVE"]')
    continue_shopping_button = (By.XPATH,'//button[normalize-space()="CONTINUE SHOPPING"]')
    free_delivery_button = (By.XPATH,'//div[@data-spm="filter"]/div[2]/div/div/div/div[normalize-space()="Free Delivery"]')
     

    def case1(self):

        self.wait_for(self.search).send_keys(test_data.data['search'])
        self.wait_for(self.search).send_keys(Keys.ENTER)
        self.wait_for(self.min_price).send_keys(test_data.data['data_set_1']['min_price'])
        self.wait_for(self.max_price).send_keys(test_data.data['data_set_1']['max_price'])
        self.wait_for(self.apply_button).click()
        self.wait_for(self.product_select).click()
        for i in range(1,6):
            self.wait_for(self.increase_quantity).click()

    
    def case2(self):

        self.wait_for(self.add_to_cart_button).click()
        self.wait_for(self.go_to_cart_button).click()
        self.wait_for(self.clear_cart).click()
        self.wait_for(self.remove_button).click()


    def case3(self):

        self.wait_for(self.continue_shopping_button).click()
        self.wait_for(self.search).send_keys(test_data.data['search'])
        self.wait_for(self.search).send_keys(Keys.ENTER)
        self.wait_for(self.max_price).send_keys(test_data.data['data_set_2']['max_price'])
        self.wait_for(self.apply_button).click()
        self.wait_for(self.free_delivery_button).click()
        self.wait_for(self.product_select).click()
        self.wait_for(self.add_to_cart_button).click()
        self.wait_for(self.go_to_cart_button).click()
        

    