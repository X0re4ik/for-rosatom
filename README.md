# for-rosatom
Решение для компании Росатом

Выполнил: Мочалов Антон Вячеславович

Как установить:
1) `git clone git@github.com:X0re4ik/for-rosatom.git`
2) `python -m venv .env`
3) `.\.env\Scripts\activate`
4) `pip install -r requirements.txt`
5) Установить свои параметры базы данных

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        "NAME": "djtest",
        "USER": "postgres",
        "PASSWORD": "kuka",
        "HOST": "127.0.0.1",
        "PORT": "5433"
    }
}
```
6) `python manage.py migrate`
7) `python manage.py makemigrations questionnaire`
8) `python manage.py loaddata questionnaire/data_for_division.json`
9) `python manage.py runserver`

```
# Запрос на получение всех доступных дивизионов
command: http GET http://127.0.0.1:8000/questionnaire/api/v1/list_of_divisions
answer: 
  ...
  Content-Type: application/json
  
  [
      {
          "id": 1,
          "name": "Топливный"
      },
      {
          "id": 2,
          "name": "Машиностроение"
      },
      {
          "id": 3,
          "name": "ЯОК"
      },
      {
          "id": 4,
          "name": "Энергетический"
      }
  ]
```

```
# Запрос на получение статистики
command: http GET http://127.0.0.1:8000/questionnaire/api/v1/statistics
answer: 
  ...
  Content-Type: application/json

  [
      {
          "company": "ОА \"УМЗА\"",
          "division": "Топливный",
          "total": 1
      },
      {
          "company": "ОА \"УМЗЫ\"",
          "division": "Машиностроение",
          "total": 2
      }
  ]
```
```
# Получение списка анкет
command: http GET http://127.0.0.1:8000/questionnaire/api/v1/list
answer: 
  ...
  Content-Type: application/json

  [
      {
          "id": 1,
          "company": {
              "id": 1,
              "name": "ОА \"УМЗА\"",
              "division": 1
          },
          "question": "Возьмете Антона на работу?",
          "email": "xoore4ik@gmail.com",
          "time_of_creat": "2023-09-05T18:40:06.635954Z"
      },
      {
          "id": 2,
          "company": {
              "id": 2,
              "name": "ОА \"УМЗЫ\"",
              "division": 2
          },
          "question": "А когда премия?",
          "email": "xoore4ik@gmail.com",
          "time_of_creat": "2023-09-05T18:40:06.635954Z"
      },
      {
          "id": 3,
          "company": {
              "id": 2,
              "name": "ОА \"УМЗЫ\"",
              "division": 2
          },
          "question": "Сколько ждать?",
          "email": "xoore4ik@gmail.com",
          "time_of_creat": "2023-09-05T18:40:06.635954Z"
      }
  ]
```
```
# Получения компании из дивизиона
command: http GET http://127.0.0.1:8000/questionnaire/api/v1/companies_from/1
answer: 
  ...
  Content-Type: application/json

  [
      {
          "id": 1,
          "name": "ОА \"УМЗА\"",
          "division": 1
      }
  ]
```

```
# Добавления компании
command: http POST http://127.0.0.1:8000/questionnaire/api/v1/add_company "name"="АОО \"УМЗА\"" "division"=1
answer: 
  ...
  Content-Type: application/json

  {
      "id": 3,
      "name": "АОО УМЗА",
      "division": 1
  }
```

```
# Добавления анкеты
command: http POST http://127.0.0.1:8000/questionnaire/api/v1/add "question"="Когда же премия?" "company"=12
answer: 
  ...
  Content-Type: application/json

  {
      "id": 4,
      "question": "Когда же премия?",
      "email": null,
      "time_of_creat": "2023-09-05T18:40:06.635954Z",
      "company": 1
  }
```

```
# HTML страница для получения статистики
command: http GET http://127.0.0.1:8000/questionnaire/statistics
answer:
  ...
  Content-Type: text/html; charset=utf-8
```

```
# HTML страница для создания анкеты
command: http GET http://127.0.0.1:8000/questionnaire
answer:
  ...
  Content-Type: text/html; charset=utf-8
```
