import allure
from selene import have
from pages.configs import Helpers


class CategoryPageName(Helpers):

    def select_subcategory(self, subcategory):
        with allure.step(f'Выбрать подкатегорию: "{subcategory}"'):
            self.click_element('#bx_3909807802_458770')
            self.elements('[href="/catalog/3888/"]').should(have.text(subcategory))


category_name = CategoryPageName()