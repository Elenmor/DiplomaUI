from selene import have, be, by
from selene.support.shared import browser


class UIPage:

    def open(self):
        browser.open('https://www.dom-knigi.ru/')
        return self

    def login_form_open(self):
        browser.element('//span[contains(@class, "icon-txt")]').should(have.text('Войти')).click()
        return self

    def login_name_type(self, name):
        browser.element('[name="USER_LOGIN"]').type(name)
        return self

    def login_password_type(self, value):
        browser.element('[name="USER_PASSWORD"]').type(value)
        return self

    def login_submit(self):
        browser.element('[name="Login"]').press_enter()
        return self

    def login_error(self):
        browser.element("//div[contains(text(), 'Неверный логин или пароль.')]").should(
            be.visible)
        return self

    ##for search_test

    def searh_input(self, value):
        browser.element('#title-search-input').type(value).press_enter()
        return self

    def error_search(self):
        browser.element("//font[contains(text(), 'К сожалению, на ваш поисковый запрос ничего не найдено.')]")

    def search_book(self, value):
        browser.element('#title-search-input').type(value).press_enter()
        browser.element(by.partial_text(value)).should(
            be.visible)

    def add_to_cart(self):
        browser.element('#bx_3966226736_711691_7e1b8e3524755c391129a9d7e6f2d206_buy_link').click()

    def go_to_cart(self):
        browser.element("//button[contains(text(), 'Перейти в корзину')]").click()

    def cheack_cart(self):
        browser.element(by.partial_text('Волкодав')).should(be.visible)

    def press_delete(self):
        browser.element('a[href="/basket/?clear"]').click()

    def empty_cart(self):
        browser.element(by.partial_text('Ваша корзина пуста')).should(be.visible)

    def press_heart(self):
        browser.element('.border_svg').click()

    def go_to_wishlist(self):
        browser.element('#favour_in').click()

    def cheack_wishlist(self):
        browser.element(by.partial_text('Волкодав')).should(be.visible)

    def go_to_book(self):
        browser.element('a[href="/catalog/sovremennaya_rossiyskaya_literatura'
                        '/volkodav_yu_maestro_m_ast_2021_352s_eto_lichnoe/"]').click()
