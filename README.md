# Проект по тестированию сайта dom-knigi.ru
> <a target="_blank" href="https://www.dom-knigi.ru/">Ссылка на сайт</a>

![This is an image](images/screenshots/domknigi.png)

<!-- Технологии -->
### Проект реализован с использованием:
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="images/logo/selene.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/jenkins.png"></code>
  <code><img width="5%" title="Selenoid" src="images/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/logo/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="images/logo/jira.png"></code>
  <code><img width="5%" title="Telegram" src="images/logo/tg.png"></code>
</p>

<!-- Тест кейсы -->

### Что проверяем
* Проверка авторизации с невалидными данными
* Проверка поиска отсутствующей книги
* Проверка поиска существующей книги
* Проверка добавления товара в корзину
* Проверка очистки корзины 
* Проверка добавления в избранное
* Проверка добавления в корзину из избранного


### <img width="5%" title="Jenkins" src="images/logo/jenkins.png"> Запуск проекта в Jenkins

### [Job](https://jenkins.autotests.cloud/job/005_Morilova_diplomaUI/)

##### При нажатии на "Собрать сейчас" начнется сборка тестов и их прохождение, через виртуальную машину в Selenide.
![This is an image](images/screenshots/job.png)

<!-- Allure report -->
## Локальный запуск автотестов
Пример командной строки:
```bash
pytest .
```

Получение отчёта:
```bash
allure.bat serve allure-results
```
<!-- Allure TestOps -->


### <img width="5%" title="Allure Report" src="images/logo/allure_report.png"> Allure report
### [Report](https://jenkins.autotests.cloud/job/005_Morilova_diplomaUI/26/allure/)
##### После прохождения тестов, результаты можно посмотреть в Allure отчете, где так же содержится ссылка на Jenkins
![This is an image](images/screenshots/Allure.png)

##### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритезации, по времени прохождения и др.
![This is an image](images/screenshots/grafs.png)

##### Во вкладке Suites находятся собранные тест кейсы, у которых описаны шаги и приложены логи, скриншот и видео о прохождении теста
![This is an image](images/screenshots/tests.png)

##### Видео прохождение теста
![This is an image](images/screenshots/test.gif)

<!-- Allure TestOps -->

### <img width="5%" title="Allure TestOps" src="images/logo/allure_testops.png"> Интеграция с Allure TestOps

### [Dashboard](https://allure.autotests.cloud/project/3519/dashboards)

##### Так же вся отчетность сохраняется в Allure TestOps, где строятся аналогичные графики.
![This is an image](images/screenshots/alluretestops.png)

#### Во вкладке со сьютами, мы можем:
- Управлять всеми тест-кейсами или с каждым отдельно
- Перезапускать каждый тест отдельно от всех тестов
- Настроить интеграцию с Jira
- Добавлять ручные тесты и т.д

![This is an image](images/screenshots/alluretestops1.png)


<!-- Jira -->

### <img width="5%" title="Jira" src="images/logo/jira.png"> Интеграция с Jira
##### Настроив через Allure TestOps интеграцию с Jira, в тикет можно пробросить результат прохождение тестов и список тест-кейсов из Allure

![This is an image](images/screenshots/jira.png)


<!-- Telegram -->

### <img width="5%" title="Telegram" src="images/logo/tg.png"> Интеграция с Telegram
##### После прохождения тестов, в Telegram bot приходит сообщение с графиком и небольшой информацией о тестах.

![This is an image](images/screenshots/telegram.png)
