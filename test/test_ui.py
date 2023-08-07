from models.ui import UIPage
import allure
from allure_commons.types import Severity

uipage = UIPage()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Morilova")
@allure.description('Проверка авторизации')
@allure.feature('Проверка невалидной авторизации')
@allure.link('https://www.dom-knigi.ru/')
def test_error_auth():
    with allure.step('Открываем главную страницу'):
        uipage.open()
    with allure.step('Открываем форму авторизации'):
        uipage.login_form_open()
    with allure.step('Вводим неверный логин'):
        uipage.login_name_type('gfigwwf')
    with allure.step('Вводим неверный пароль'):
        uipage.login_password_type('12345')
    with allure.step('Нажимаем кнопку Войти'):
        uipage.login_submit()
    with allure.step('Проверяем наличие ошибки'):
        uipage.login_error()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Morilova")
@allure.description('Проверка поиска')
@allure.feature('Проверка поиска отсутствующей книги')
@allure.link('https://www.dom-knigi.ru/')
def test_error_search():
    with allure.step('Открываем главную страницу'):
        uipage.open()
    with allure.step('В строке поиска вводим набор букв'):
        uipage.searh_input('rfhvgjk')
    with allure.step('Проверяем наличие ошибки'):
        uipage.error_search()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Morilova")
@allure.description('Проверка поиска')
@allure.feature('Проверка поиска существующей книги')
@allure.link('https://www.dom-knigi.ru/')
def test_search_book():
    with allure.step('Открываем главную страницу'):
        uipage.open()
    with allure.step('Вводим название книги с строке поиска и проверяем ее наличие'):
        uipage.search_book('Мастер и Маргарита')


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Morilova")
@allure.description('Проверка корзины')
@allure.feature('Проверка добавления товара в корзину')
@allure.link('https://www.dom-knigi.ru/')
def test_add_to_cart():
    with allure.step('Открываем главную страницу'):
        uipage.open()
    with allure.step('Ищем книгу'):
        uipage.search_book('Волкодав')
    with allure.step('Добавляем книгу в корзину'):
        uipage.add_to_cart()
    with allure.step('Переходим в корзину'):
        uipage.go_to_cart()
    with allure.step('Проверяем наличие книги в корзине'):
        uipage.cheack_cart()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Morilova")
@allure.description('Проверка корзины')
@allure.feature('Проверка очистки корзины')
@allure.link('https://www.dom-knigi.ru/')
def test_clear_cart():
    with allure.step('Открываем главную страницу'):
        uipage.open()
    with allure.step('Ищем книгу'):
        uipage.search_book('Волкодав')
    with allure.step('Добавляем книгу в корзину'):
        uipage.add_to_cart()
    with allure.step('Переходим в корзину'):
        uipage.go_to_cart()
    with allure.step('Нажимаем кнопку Очисить корзину'):
        uipage.press_delete()
    with allure.step('Проверяем, что корзина пуста'):
        uipage.empty_cart()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Morilova")
@allure.description('Проверка избранного')
@allure.feature('Проверка добавления в избранное')
@allure.link('https://www.dom-knigi.ru/')
def test_add_wishlist():
    with allure.step('Открываем главную страницу'):
        uipage.open()
    with allure.step('Ищем книгу'):
        uipage.search_book('Волкодав')
    with allure.step('Переходим на книгу'):
        uipage.go_to_book()
    with allure.step('Нажимаем сердечко'):
        uipage.press_heart()
    with allure.step('Переходим в избранное'):
        uipage.go_to_wishlist()
    with allure.step('Проверяем наличие книги в избранном'):
        uipage.cheack_wishlist()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Morilova")
@allure.description('Проверка избранного')
@allure.feature('Проверка добавления в корзину из избранного')
@allure.link('https://www.dom-knigi.ru/')
def test_add_cart_from_wishlist():
    with allure.step('Открываем главную страницу'):
        uipage.open()
    with allure.step('Ищем книгу'):
        uipage.search_book('Волкодав')
    with allure.step('Переходим на книгу'):
        uipage.go_to_book()
    with allure.step('Нажимаем сердечко'):
        uipage.press_heart()
    with allure.step('Переходим в избранное'):
        uipage.go_to_wishlist()
    with allure.step('Добавляем книгу в корзину'):
        uipage.add_to_cart()
    with allure.step('Переходим в корзину'):
        uipage.go_to_cart()
    with allure.step('Проверяем наличие книги в корзине'):
        uipage.cheack_cart()
