Название проекта: "Сравнение различных библиотек для визуализации данных"

1. Название проекта

    Данный проект проводит машинное сравнение библиотек Matplotlib, Seaborn, Plotly для визуализации данных.
    Для этого в программе используются данные расхода памяти и времени для построения графиков.
    Каждая библиотека строит одиннадцать аналогичных друг другу графиков.

2. Описание проекта

    Проект направлен на анализ расхода памяти и затраченного времени на построение графиков выполненных разными библиотеками.
    Реализованы модули для расчета данных визуализации, обработки машинных затрат, база данных для хранения результатов, 
    декоратор для получения данных, визуализация полученных данных и три модуля для построения графиков исследуемыми библиотеками соответственно.
    Проект дает понятия о возможностях и быстродействия библиотек.

3. Установка проекта

   1. Клонируйте проект с GitHub:

   2. Перейдите в папку проекта:

       cd app

   3. Создайте виртуальное окружение (если используется):  

        python -m venv.venv
        source venv/bin/activate  # Для macOS/Linux
        venv\Scripts\activate  # Для Windows

   4. Установите зависимости:  

       pip install -r requirements.txt
    
4. Использование проекта  

    Запуск основного скрипта:
    
    python main.py
    
    Пример вызова одной из функций:  
    
    from resultat import plot_statistic
    
    plot_statistic() - Обработка результатов
    
5. Основной функционал проекта  

    Главные модули и их функции:
    
    main.py - Главный файл запуска
    
    data.py - Файл функций для расчетов данных
    
    database.py - Файл функций для работы с базой данных
    
    decorators.py - Файл функций для сбора статистики
    
    resultat.py - Файл функций для обработки данных полученных из базы данных и построения графика
    
    README.md - Документация проекта
    
    requirements.txt - Список зависимостей
    
    data/data.db - База данных для хранения данных
    
    methods/__init__.py - Файл списков импортируемых функций
    
    methods/test_matplotlib.py - Файл функций для построения графиков при помощи библиотеки Matplotlib
    
    methods/test_plotly.py - Файл функций для построения графиков при помощи библиотеки Plotly
    
    methods/test_seaborn.py - Файл функций для построения графиков при помощи библиотеки Seaborn
    
6. Структура проекта
    
    data/data.db
    methods/__init__.py
    methods/test_matplotlib.py
    methods/test_plotly.py
    methods/test_seaborn.py
    main.py
    data.py
    database.py
    decorators.py
    resultat.py
    README.md
    requirements.txt

7. Автор проекта
    
    Владимир Шарый,  студент UrbanUniversyti python разработчик