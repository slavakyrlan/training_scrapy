# training_scrapy
Фреймворк Scrapy

python 3.12
scrapy 2.13.1

## Создание проекта:

```bash
scrapy startproject training_crapy .
```

## [Структура проекта](https://docs.scrapy.org/en/latest/topics/architecture.html):
```commandline
training_scrapy  
 ├── training_scrapy /
 |   ├── spiders/          <-- Директория для размещения пауков.
 |   |   └── __init__.py
 |   ├── __init__.py
 |   ├── items.py          <-- Описание моделей
 |   ├── middlewares.py    <-- Дополнительные обработки запросов
 |   ├── pipelines.py      <-- Обработчики собранных данных
 |   └── settings.py       <-- Настройки проекта
 ├── venv/
 └── scrapy.cfg            <-- Отдельные настройки, в том числе для деплоя
```

## Создание первого паука
```bash
scrapy genspider example example.com 
```
* example - имя паука
* example.com - домен, на котором будет работать паук

## Запуск паука yatube
```bash
scrapy crawl yatube -o ya.json
```