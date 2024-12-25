# Конвертер конфигурационного языка

Этот проект представляет собой инструмент командной строки, который преобразует данные из формата JSON в формат учебного конфигурационного языка. Входные данные принимаются в формате JSON через стандартный ввод, а результат выводится в стандартный вывод в формате конфигурационного языка.

## Особенности

- Преобразует массивы, словари и простые значения из JSON в учебный конфигурационный язык.
- Поддерживает объявления и вычисления констант.
- Обрабатывает синтаксические ошибки и выводит соответствующие сообщения.
- Возможность тестировать конфигурации через различные примеры.

## Синтаксис конфигурационного языка

### Массивы

В JSON массивы преобразуются в формат:
#( значение значение значение ... )

shell
Копировать код

### Словари

В JSON объекты (словаря) преобразуются в формат:
{ имя = значение имя = значение имя = значение ... }


### Константы

- Объявление константы:
имя := значение;

diff
Копировать код

- Вычисление константы:
@[имя]


### Примеры конфигураций

#### Пример 1: Словарь
JSON:
```json
{
"name": "John",
"age": 30,
"city": "New York"
}
```
```json
Конфигурация:
{
  name = John
  age = 30
  city = New York
}
```
Пример 2: Массив
JSON:
```json
[1, 2, 3, 4]
```
Конфигурация:
```json
#( 1 2 3 4 )
```
Пример 3: Сложная структура
JSON:
``` json
{
  "config": {
    "host": "localhost",
    "port": 8080
  },
  "services": [
    {
      "name": "service1",
      "enabled": true
    }
  ]
}
```
Конфигурация:
```json
{
  config = {
    host = localhost
    port = 8080
  }
  services = #( {
    name = service1
    enabled = true
  } )
}
```
Установка
Скачайте или клонируйте репозиторий:

```bash
git clone https://github.com/yourusername/config-converter.git
cd config-converter
```
Убедитесь, что у вас установлен Python 3.x.

Установите зависимости (если есть) с помощью pip:

```pip
pip install -r requirements.txt
```
Использование
Для использования инструмента командной строки передайте JSON в стандартный ввод, и результат будет выведен в формате конфигурационного языка.

Пример:

```bash
echo '{"name": "John", "age": 30, "city": "New York"}' | python config_converter.py
```
Примечания
В случае ошибок в синтаксисе (например, неправильные имена переменных) программа выведет сообщение об ошибке.
Программа использует регулярные выражения для проверки правильности имен, которые должны состоять только из маленьких латинских букв.
Тесты
Для запуска тестов с примерами конфигураций:

```bash
python config_converter.py < тест_файл.json
```
