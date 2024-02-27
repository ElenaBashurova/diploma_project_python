from selene import browser, Element


class Helpers:

    @staticmethod
    def elements(path) -> Element:
        return browser.element(path)

    @staticmethod
    def click_element(xpath_or_selector: str, element_number=0) -> None:
        if element_number == 0:
            browser.element(xpath_or_selector).click()
        else:
            browser.all(xpath_or_selector)[element_number].click()
