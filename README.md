# Дипломный проект по автоматизации тестирования для интернет-магазинов
> <a target="_blank" href="https://www.officemag.ru/">UI тесты</a>
> <a target="_blank" href="http://shop.bugred.ru/">Api тесты</a>

#### Список проверок, реализованных в UI автотестах на интернет - магазин ОфисМаг
- [x] Проверка наличия категорий товаров
- [x] Проверка акционных товаров
- [x] Проверка товаров участвующих в распродаже
- [x] Проверка поиска товаров через поисковую строку

#### Список проверок, реализованных в API тестах - тестовый интернет магазин shop.bugred
- [x] Проверка успешного создания товара на сайте
- [x] Проверка неудачного создания товара на сайте
- [x] Проверка получения информации о товаре
- [x] Проверка неудачное получение информации о товаре
- [x] Проверка обновление информации о товаре
- [x] Проверка удаления товара с сайта

### Структура проекта

### Проект реализован с использованием
Python Pytest Selene Jenkins Selenoid Jira Allure reports Allure TestOps Telegram 

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

<!-- Jenkins -->
----
## <img width="5%" title="Jenkins" src="design_resources/logo/jenkins.png"> Запуск автотестов выполняется на сервере  Jenkins
#### 1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/project_bashurova_python">проект</a>

![This is an image](/design_resources/screens/Jenkins.jpg)

#### 2. Выбрать пункт **Собрать с параметрами**
#### 3. В случае необходимости изменить параметры, выбрав значения из выпадающих списков
#### 4. Нажать **Собрать**
#### 5. Результат запуска сборки можно посмотреть в отчёте Allure-testops

## <img width="5%" title="Отчет Allure" src="design_resources/logo/allure_testops.png"> Отчет в Allure-testops
## [Ссылка на Allure-testops](https://allure.autotests.cloud/project/4080/dashboards)
![This is an image](/design_resources/screens/allure_testops.jpg)

----
# Локальный запуск

1. Скачайте репозиторий себе на компьютер
2. Создайте и активируйте виртуальное окружение
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  ```
3. Установите зависимости с помощью pip
  ```bash
  pip install -r requirements.txt
  ```
4. Для запусков тестов локально используйте команды:
  ```bash
  pytest -sv -m web
  pytest -sv -m api
  ```
Получение отчёта allure:
```bash
allure serve allure-results
```

<!-- Jira -->
----
## <img width="5%" title="Задача в Jire" src="design_resources/logo/jira.png"> Создание задачи в Jira
## [Ссылка на задачу в Jira](https://jira.autotests.cloud/browse/HOMEWORK-1138)
![This is an image](/design_resources/screens/Jira_task.jpg) 

<!-- Allure report -->
----
## <img width="5%" title="Allure Report" src="design_resources/logo/allure_report.png"> Просмотр отчета по пройденным автотестам Allure Report
## [Ссылка на отчет Allure report](https://jenkins.autotests.cloud/job/project_bashurova_python/48/allure/)
### Результаты тестов в Allure report
![This is an image](/design_resources/screens/Allure_results.jpg)  

### Пример видеозаписи прохождения теста
![This is an image](/design_resources/screens/видео.gif)

<!-- Telegram -->
----
## <img width="5%" title="Telegram" src="design_resources/logo/tg.png"> Отчет в Telegram

### Уведомление в Telegram bot после прохождения тестов

![This is an image](design_resources/screens/Телеграм.jpg)