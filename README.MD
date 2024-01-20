# Фреймворк для автоматизации тестирования API Restful-Booker
> <a target="_blank" href="https://restful-booker.herokuapp.com/apidoc/index.html">API документация</a>

----
![main page screenshot](/images/main_api.JPG)
----
> ### Особенности проекта

* Оповещения о тестовых прогонах в Telegram
* Проверки выполнены на request body, response body, status code
* Валидация Pydantic
* Сборка проекта в Jenkins
* Отчеты Allure Report
* Интеграция с Allure TestOps
* Автоматизация отчетности о тестовых прогонах и тест-кейсах в Jira

### Список проверок, реализованных в автотестах
- [x] Успешная и неуспешная авторизации
- [x] Получение списка броней
- [x] Удаление брони
- [x] Создание новой брони
- [x] Редактирование существующей брони

----

### Используемый стэк

<img title="Python" src="images/python-original.svg" height="40" width="40"/> <img title="Pytest" src="images/pytest-original.svg" height="40" width="40"/> <img title="Jira" src="images/jira-original.svg" height="40" width="40"/> <img title="Allure Report" src="images/Allure_Report.png" height="40" width="40"/> <img title="Allure TestOps" src="images/AllureTestOps.png" height="40" width="40"/> <img title="GitHub" src="images/github-original.svg" height="40" width="40"/> <img title="Pycharm" src="images/pycharm.png" height="40" width="40"/> <img title="Telegram" src="images/tg.png" height="40" width="40"/> <img title="Jenkins" src="images/jenkins-original.svg" height="40" width="40"/> <img title="requests" src="images/requests.png" height="40" width="40"/> <img title="pydantic" src="images/pydantic.png" height="40" width="40"/> 

----

### Локальный запуск автотестов

#### Для запуска автотестов выполнить в cli:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```

#### Генерация отчёта:
```bash
allure serve 
```
----
### Проект в Jenkins
   
#### Проект
> <a target="_blank" href="https://jenkins.autotests.cloud/job/C08-itpmkz-diploma-api/">Ссылка</a>

#### Запуск автотестов в Jenkins
Является параметризированным. На выбор доступны параметры, описанные выше.
Для запуска достаточно:
1. Открыть проект
2. Нажать "Build Now"

Сопроводительный скриншот:
<img title="Jenkins" src="images/jenkins.JPG"/>

----
### Allure отчет
Пример выполнения Allure отчета доступен по ссылке:
> <a target="_blank" href="https://jenkins.autotests.cloud/job/C08-itpmkz-diploma-api/5/allure/">Ссылка</a>

Отчет:
<img title="Allure Report" src="images/allure_report.JPG"/>

Детали:
<img title="Report Details" src="images/allure_details.JPG"/>


----
### Интеграция с Allure TestOps
Пример интеграции доступен по ссылке:
> <a target="_blank" href="https://allure.autotests.cloud/project/3987/launches">Ссылка</a>

Запуск тестовых прогонов:
<img title="TestOps" src="images/testops.JPG"/>

Детали тестового прогона:
<img title="TestOps Details" src="images/testops_details.JPG"/>

----
### Интеграция с Jira
> <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-1068">Ссылка</a>

Тикет:
<img title="TestOps Details" src="images/jira.JPG"/>

----
### Оповещения в Telegram
![telegram_allert](images/tgnotify_api.JPG)
