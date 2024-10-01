# battle of heroes
 simple console game

***Разработка простой текстовой консольной игры "Битва героев" на Python с использованием классов, где игрок и компьютер управляют героями с различными характеристиками.
Игра состоит из раундов, в каждом раунде игроки по очереди наносят урон друг другу, пока у одного из героев не закончится здоровье.***

___Разработка производится в соответствии с Планом проекта в несколько этапов___

### Этап 1: Анализ требований и проектирование
#### A. Сбор требований:
Подробно изучить требования к игре и определить функциональность, которую необходимо реализовать.</br>

Требования:
1. Используй ООП (Объектно-Ориентированное Программирование) для создания классов героев.
2. Игра должна быть реализована как консольное приложение.

Классы:

Класс Hero:
- Атрибуты:
- Имя (name)
- Здоровье (health), начальное значение 100
- Сила удара (attack_power), начальное значение 20
- Методы:
- attack(other): атакует другого героя (other), отнимая здоровье в размере своей силы удара
- is_alive(): возвращает True, если здоровье героя больше 0, иначе False

Класс Game:
- Атрибуты:
- Игрок (player), экземпляр класса Hero
- Компьютер (computer), экземпляр класса Hero
- Методы:
- start(): начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет. Выводит информацию о каждом ходе (кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.


#### B. Проектирование классов: 
- Определить, какие классы и методы будут необходимы.
- Спроектировать структуру классов Hero и Game.

### Этап 2: Реализация класса Hero
1. Создать класс Hero:
   - Добавить атрибуты name, health, и attack_power с соответствующими начальными значениями.
   - Реализовать метод attack(other), который уменьшает здоровье другого героя.
   - Реализовать метод is_alive(), который проверяет, жив ли герой.

### Этап 3: Реализация класса Game
1. Создать класс Game:
   - Добавить атрибуты player и computer как экземпляры класса Hero.
   - Реализовать метод start(), который будет содержать логику игры.
   - В методе start() организовать чередование атак между игроком и компьютером, используя методы класса Hero.

### Этап 4: Реализация игрового цикла
1. Разработать логику игрового цикла:
   - В методе start() реализовать цикл, который продолжается, пока один из героев жив.
   - Выводить информацию о каждом ходе, включая, кто атаковал и сколько здоровья осталось у противника.
   - Объявить победителя после окончания игры.

### Этап 5: Тестирование игры
1. Тестирование отдельных компонентов:
   - Проверить методы класса Hero на корректность работы.
   - Убедиться, что класс Game корректно инициализирует игру и запускает игровой процесс.
2. Тестирование игры в целом:
   - Провести несколько пробных игр, чтобы убедиться, что игра работает без ошибок и соответствует требованиям.

### Этап 6: Оптимизация и улучшение
1. Оптимизация кода: Убедиться, что код чистый и понятный.
2. Добавление дополнительных функций: По желанию, можно добавить новые функции, такие как выбор уровня сложности, возможность игры против другого игрока, улучшение UI и т.д.

### Этап 7: Документация и завершение проекта
1. Документирование кода: Добавить комментарии и документацию к коду для облегчения понимания и поддержки.
2. Создание пользовательской документации: Написать краткое руководство по использованию игры.