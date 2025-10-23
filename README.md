# 🏔️ Mountain Passes API

**REST API** для добавления горных перевалов. Позволяет туристам отправлять данные о перевалах. После модерации и внесения информации в базу данных, туристы могут увидеть в мобильном приложении статус модерации, а также просматривать базу с объектами, внесёнными другими.

Данное приложение развернуто на удаленном сервере:

### 📄Deploy:
👉 **Swagger -** [https://igor39.pythonanywhere.com/swagger/](https://igor39.pythonanywhere.com/swagger/)  
👉 **DRF API -** [https://igor39.pythonanywhere.com/api/](https://igor39.pythonanywhere.com/api/) 

---

## 🚀 Возможности

- ➕ Добавление новых перевалов  
- 🔍 Просмотр информации о перевалах  
- ✏️ Редактирование перевалов (только со статусом `new`)  
- 👤 Получение всех перевалов пользователя   
- 📘 Автоматическая документация **Swagger**

---

### ⚙️ Статусы модерации

| Статус     | Описание |
|------------|-----------|
| `new`      | новый перевал (автоматически присваивается при создании) |
| `pending`  | модератор взял в работу |
| `accepted` | модерация прошла успешно |
| `rejected` | модерация не пройдена |

## ⚡ Локальный запуск проекта

1. Клонируем репозиторий<br>
git clone https://github.com/ваш-username/mountain_pass<br>
**cd mountain_pass**

2. Создаём виртуальное окружение<br>
**python -m venv mountain**

3. Активируем окружение
* Windows (PowerShell): 
**.\mountain\Scripts\Activate.ps1**
* Windows (cmd): 
**mountain\Scripts\activate.bat**
* Linux/macOS:
**source mountain/bin/activate**

4. Устанавливаем зависимости<br>
**pip install -r pereval/requirements.txt**

5. Применяем миграции
**python pereva/manage.py migrate**

6. Запускаем сервер разработки
**python manage.py runserver**

7. После запуска открываем:<br>
   Swagger: http://127.0.0.1:8000/swagger/
