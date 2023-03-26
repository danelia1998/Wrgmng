# pyOOPHomeTask.py and test_pyOOPHomeTask.py

This repository contains the implementation of a 2D drawing engine that supports drawing circles, triangles, and rectangles in Python. The implementation is split into two files: `pyOOPHomeTask.py`, which contains the implementation of the engine, and `test_pyOOPHomeTask.py`, which contains the test cases for the engine.

## pyOOPHomeTask.py

`pyOOPHomeTask.py` contains the implementation of the `Engine2D` class, which provides a simple 2D drawing engine. The engine supports adding shapes to a canvas, changing the color of the shapes, and drawing the shapes on the canvas.

The following classes are defined in `pyOOPHomeTask.py`:

- `Engine2D`: The main drawing engine class.
- `Circle`: A class representing a circle.
- `Triangle`: A class representing a triangle.
- `Rectangle`: A class representing a rectangle.

## test_pyOOPHomeTask.py

`test_pyOOPHomeTask.py` contains the test cases for the `pyOOPHomeTask.py` implementation. The test cases use the `pytest` testing framework.

The following test cases are defined in `test_pyOOPHomeTask.py`:

- `test_add_shape()`: A test case that checks that a shape can be added to the canvas of an `Engine2D` object.
- `test_change_color()`: A test case that checks that the color of an `Engine2D` object can be changed.
- `test_draw()`: A test case that checks that shapes can be added to the canvas of an `Engine2D` object, their color can be changed, and they can be drawn on the canvas.
- `test_draw_multiple_shapes()`: A test case that checks that multiple shapes can be added to the canvas of an `Engine2D` object, their color can be changed, and they can be drawn on the canvas.
- `test_circle()`: A test case that checks that a circle can be drawn using the `draw()` method of the `Circle` class.
- `test_triangle()`: A test case that checks that a triangle can be drawn using the `draw()` method of the `Triangle` class.

## Usage

To use the 2D drawing engine, simply import the `Engine2D`, `Circle`, `Triangle`, and `Rectangle` classes from `pyOOPHomeTask.py`, create an `Engine2D` object, and start adding shapes to the canvas. You can also change the color of the shapes and draw them on the canvas using the `draw()` method of the `Engine2D` object.



# Wiki Pytest

## pyTestHomeTask.py
- This script contains a get_languages() function that retrieves data from a table on the Wikipedia page "Programming languages used in most popular websites". The data is parsed and stored in a data class called Language.

## test_pyTestHomeTask.py
- This test script contains a single test function called test_popularity(). The function uses the get_languages() function to retrieve language data, and tests the popularity of each language against a set of expected values using the @pytest.mark.parametrize() decorator. If a language's popularity is less than the expected value, an error message is created and added to a list of errors. If there are no errors, the test passes.

To run the test, you can execute the following command in the terminal:


- pytest test_pyTestHomeTask.py

## Credits

This implementation was created as a home task. The task was completed by Davit Danelia.
