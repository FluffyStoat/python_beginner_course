1. Создать класс Name, который принимает имя и фамилию в качестве аргументов при конструировании.
   Класс должен поддерживать атрибуты:
   
   ```
   first_name, возвращающий имя
   last_name, возвращающий фамилию
   full_name, возвращающий имя и фамилию
   initials, возвращающий инициалы
   ```
   
   Класс должен приводить переданные имя и фамилию в форму при которой имя и фамилия начинаются с заглавной буквы, 
   а все остальные буквы в нижнем регистре (поскольку вызывающий код может передавать такие строки как "JOHN", 'jOHN', 
   'sMiTh' и т.д.)

   Примеры вызовов и возвратов:
   ```
   a1 = Name('jonh', 'SMITH')
   a1.first_name -> 'John' 
   a1.last_name -> 'Smith'
   a1.full_name -> 'John Smith'
   a1.initials -> 'J.S'
   ```

   **(person.py)**
   
2. Создайте класс Calculator который поддерживает:
   - сложение двух чисел
   - вычисление разницы между двумя числами
   - умножение двух чисел
   - деление одного числа на другое
   
   Примеры вызовов и возвратов:
   ```
   calculator = Calculator()
   calculator.add(10, 5) -> 15 
   calculator.subtract(10, 5) -> 5
   calculator.multiply(10, 5) -> 50
   calculator.divide(10, 5) -> 2
   ```
   
   **(calculator.py)**
   
3. Создать класс Employee, который принимает имя, фамилию и зарплату в качестве аргументов при конструировании.
   
   Класс должен поддерживать:
   - атрибут first_name, возвращающий имя
   - атрибут last_name, возвращающий фамилию
   - атрибут salary, возвращающий зарплату
   - функцию from_string, которая принимает имя, фамилию и зарплату в формате 'first_name-last_name-salary', 
   парсит строку и возвращает экземпляр Employee

   **Примеры:**
   
   ```
   emp1 = Employee('Mary', 'Sue', 60000)
   emp2 = Employee.from_string('John-Smith-55000')
   
   emp1.first_name -> 'Mary'
   emp1.salary -> 60000
   
   emp2.first_name -> 'John'
   emp2.salary -> 55000

   ```
    
   **(employee.py)**
   
4. Создайте класс Pizza, который принимает список ингредиентов.
   
   Класс поддерживает:
   - атрибут order_number, который возвращает текущий номер заказа 
   (подсказка: используйте статический атрибут в качестве сквозного счётчика)
   - атрибут ingredients, который возвращает список, принятый в конструкторе
   - функции (garden_feast, hawaiian, meat_festival) создания видов пицц, ингредиенты которых заранее 
   известны (см. таблицу)
   
   Name             Ingredients
   hawaiian         - ham, pineapple
   meat_festival    - beef, meatball, bacon
   garden_feast     - spinach, olives, mushroom
   
   Примеры вызовов и возвратов:
   ```
   p1 = Pizza(['bacon', 'parmesan', 'ham'])
   p2 = Pizza.garden_feast()
   p1.ingredients -> ['bacon', 'parmesan', 'ham']
   p2.ingredients -> ['spinach', 'olives', 'mushroom']
   p1.order_number -> 1
   p2.order_number -> 2
   ```
   
   **(pizza.py)**
   
5. Создайте класс Circle который конструируется с передачей радиуса в качестве аргумента.
   Класс Circle должен предоставлять две функции: 
   - get_area, которая возвращает площадь круга
   - get_perimeter, которая возвращает длину окружности
   
    Примеры использования:
   ```
   circle = Circle(10)
   circle.get_area() # Возвращает прощадь
   circle.get_perimeter() # Возрващает периметер
   ```
   
   **(circle.py)**