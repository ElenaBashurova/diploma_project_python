# Проект по тестированию UI части сайта интернет-магазина Офисмаг
> <a target="_blank" href="https://www.officemag.ru/">Ссылка на Интернет-магазин</a>

#### Список проверок, реализованных в автотестах
- [x] Проверка наличия категорий товаров
- [x] Проверка акционных товаров
- [x] Провека товаров участвующих в распродаже
- [x] Проверка поиска товаров через поисковую строку

### Структура проекта

### Проект реализован с использованием
Python Pytest Selene Jenkins Selenoid Jenkins Allure reports Allure TestOps Jira Telegram 

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
# Запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/project_bashurova_python">Ссылка на проект в Jenkins</a>

### Для запуска автотестов в Jenkins
#### 1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/project_bashurova_python">проект</a>

![This is an image](/design_resources/screens/)

#### 2. Выбрать пункт **Собрать с параметрами**
#### 3. В случае необходимости изменить параметры, выбрав значения из выпадающих списков
#### 4. Нажать **Собрать**
#### 5. Результат запуска сборки можно посмотреть в отчёте Allure

![This is an image](/design_resources/screens/)

----
### Локальный запуск

> Для локального запуска необходимо выполнить команду в СLI:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest tests/
```

----
### <img width="5%" title="Jenkins" src="design_resources/logo/jenkins.png"> Запуск проекта в Jenkins

### [Jenkins](https://jenkins.autotests.cloud/job/project_bashurova_python)

#### При нажатии на "Build with Parameters" начнется сборка тестов и их прохождение, через виртуальную среду в Selenoid
![This is an image](design_resources/logo/jenkins.png)

Получение отчёта allure:
```bash
allure serve allure-results
``` 
<!-- Allure report -->
----
### <img width="5%" title="Allure Report" src="resources/logo/allure_report.png"> Allure report
### [Report](https://jenkins.autotests.cloud/job/project_bashurova_python/2/allure/)
#### Результаты тестов в Allure отчете
![This is an image](/design_resources/screens/Allure_results.jpg)  

### Пример видеозаписи прохождения теста
![This is an image](/design_resources/screens/Allure_results.jpg)

<!-- Telegram -->
----
### <img width="5%" title="Telegram" src="design_resources/logo/tg.png"> Telegram

#### Уведовление в Telegram bot после прохождения тестов

![This is an image](design_resources/images/)