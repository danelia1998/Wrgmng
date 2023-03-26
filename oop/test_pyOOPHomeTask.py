import pytest

from pyOOPHomeTask import Engine2D, Circle, Triangle, Rectangle

# тест проверяющий канвас на добавление фигур Engine2D обьекта
def test_add_shape():
    engine = Engine2D()
    circle = Circle(0, 0, 1)
    engine.add_shape(circle)
    assert engine.canvas == [circle]

# тест проверяющий изминения цвета в Engine2D обьекте
def test_change_color():
    engine = Engine2D()
    engine.change_color('red')
    assert engine.color == 'red'

# тест проверяющий добавление фигуры и цвета в Engine2D и проверка чистки канваса после рисования
def test_draw():
    engine = Engine2D()
    circle = Circle(0, 0, 1)
    engine.add_shape(circle)
    engine.change_color('red')
    assert engine.draw() == ["Drawing Circle with color red: (0, 0) with radius 1"]
    assert engine.canvas == []

# Тест на все фигуры попадание на канвас и вывода их рисунком
def test_draw_multiple_shapes():
    engine = Engine2D()
    circle = Circle(0, 0, 1)
    triangle = Triangle((0, 0), (1, 1), (2, 2))
    rectangle = Rectangle((0, 0), 2, 2)
    engine.add_shape(circle)
    engine.add_shape(triangle)
    engine.add_shape(rectangle)
    engine.change_color('red')
    assert engine.draw() == ["Drawing Circle with color red: (0, 0) with radius 1",
                             "Drawing Triangle with color red: (0, 0), (1, 1), (2, 2)",
                             "Drawing Rectangle with color red: (0, 0) with width 2 and height 2"]
    assert engine.canvas == []

# capsys из библиотеки pytest для перехвата вывода в консоль
# Тест метода draw() для окружности
def test_circle(capsys):
    circle = Circle(0, 0, 5)
    circle.draw()
    captured = capsys.readouterr()
    assert captured.out == "Drawing Circle with color black: (0, 0) with radius 5\n"

# capsys из библиотеки pytest для перехвата вывода в консоль
# Тест метода draw() для треугольника
def test_triangle(capsys):
    triangle = Triangle((0, 0), (1, 1), (2, 2))
    triangle.draw()
    captured = capsys.readouterr()
    assert captured.out == "Drawing Triangle with color black: (0, 0), (1, 1), (2, 2)\n"

# capsys из библиотеки pytest для перехвата вывода в консоль
# Тест метода draw() для прямоугольника
def test_rectangle(capsys):
    rectangle = Rectangle((0, 0), 2, 3)
    rectangle.draw()
    captured = capsys.readouterr()
    assert captured.out == "Drawing Rectangle with color black: (0, 0) with width 2 and height 3\n"

# Тест на проверку наследование цвета при его изминение на одинаковые фигуры в Engine2D
def test_change_color_same_figures():
    # Создаем два экземпляра треугольника
    triangle1 = Triangle((0, 0), (1, 1), (2, 2))
    triangle2 = Triangle((1, 1), (2, 2), (3, 3))
    # Создаем экземпляр движка
    engine = Engine2D()
    # Добавляем первый треугольник и меняем цвет на красный
    engine.add_shape(triangle1)
    engine.change_color('red')
    # Добавляем второй треугольник
    engine.add_shape(triangle2)
    # Ожидаем, что при вызове метода draw() будут нарисованы оба треугольника красным цветом
    expected_output = [
        "Drawing Triangle with color red: (0, 0), (1, 1), (2, 2)",
        "Drawing Triangle with color red: (1, 1), (2, 2), (3, 3)"
    ]
    assert engine.draw() == expected_output

# Тест на проверку наследование цвета при его изминение на разные фигуры в Engine2D
def test_change_color_different_figures():
    # Создаем треугольник и прямоугольник
    triangle = Triangle((0, 0), (1, 1), (2, 2))
    rectangle = Rectangle((0, 0), 2, 3)
    # Создаем экземпляр движка
    engine = Engine2D()
    # Добавляем треугольник и меняем цвет на серый
    engine.add_shape(triangle)
    engine.change_color('grey')
    # Добавляем  прямоугольник
    engine.add_shape(rectangle)
    # Ожидаем, что при вызове метода draw() будут нарисованы обе фигуры серым цветом
    expected_output = [
        "Drawing Triangle with color grey: (0, 0), (1, 1), (2, 2)",
        "Drawing Rectangle with color grey: (0, 0) with width 2 and height 3"
    ]
    assert engine.draw() == expected_output