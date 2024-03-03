# Проект по тестированию UI части интернет-магазина Офисмаг
> <a target="_blank" href="https://www.officemag.ru/">Ссылка на Интернет-магазин</a>

#### Список проверок, реализованных в UI автотестах
- [x] Проверка наличия категорий товаров
- [x] Проверка акционных товаров
- [x] Проверка товаров участвующих в распродаже
- [x] Проверка поиска товаров через поисковую строку

#### Список проверок, реализованных в API автотестах
- [x] Проверка успешной авторизации
- [x] Проверка добавления товара в козину
- [x] Проверка неудачного добавления товара в корзину
- [x] Проверка поиска товара
- [x] Проверка отправки емайл

### Структура проекта

### Проект реализован с использованием
Python Pytest Selene Jenkins Selenoid Jenkins Allure reports Allure TestOps Telegram 

<p  align="center">
  <code><img width="5%" title="Python" src="design_resources/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="design_resources/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="design_resources/logo/selene.png"></code>
  <code><img width="5%" title="Jenkins" src="design_resources/logo/jenkins.png"></code>
  <code><img width="5%" title="Selenoid" src="design_resources/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="design_resources/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="design_resources/logo/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="design_resources/logo/jira.png"></code>
  <code><img width="5%" title="Telegram" src="design_resources/logo/tg.png"></code>
</p>


### Для запуска автотестов в Jenkins
# Запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/project_bashurova_python">Ссылка на проект в Jenkins</a>
#### 1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/project_bashurova_python">проект</a>

![This is an image](/design_resources/screens/Jenkins.jpg)

#### 2. Выбрать пункт **Собрать с параметрами**
#### 3. В случае необходимости изменить параметры, выбрав значения из выпадающих списков
#### 4. Нажать **Собрать**
#### 5. Результат запуска сборки можно посмотреть в отчёте Allure

![This is an image](/design_resources/screens/Allure.jpg)

----
### Локальный запуск

> Для локального запуска тестов необходимо выполнить команду в СLI:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
environment='remote' pytest tests/ui_tests && pytest tests/api_tests
```
Получение отчёта allure:
```bash
allure serve allure-results

----

``` 
<!-- Allure report -->
----
### <img width="5%" title="Allure Report" src="resources/logo/allure_report.png"> Allure report
### [Report](https://jenkins.autotests.cloud/job/project_bashurova_python/2/allure/)
#### Результаты тестов в Allure отчете
![This is an image](/design_resources/screens/Allure_results.jpg)  

### Пример видеозаписи прохождения теста
![This is an image](/design_resources/screens/видео.mp4)

<!-- Telegram -->
----
### <img width="5%" title="Telegram" src="design_resources/logo/tg.png"> Telegram

#### Уведомление в Telegram bot после прохождения тестов

![This is an image](design_resources/screens/Телеграм.jpg)