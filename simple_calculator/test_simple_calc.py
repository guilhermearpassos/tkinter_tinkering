import tkinter as tk
import threading
import pytest

from simple_calculator.simple_calc import SimpleCalculator


@pytest.fixture(scope='session')
def start_gui():
    sc = SimpleCalculator()

    # t = threading.Thread(target=sc.start)
    # t.start()
    yield sc
    # sc.window.quit()
    # t.join()


@pytest.mark.parametrize(['first', 'other', 'result'],
                         [[1, 2, 3],
                          [1, 3, 4],
                          [2, 6, 8],
                          [1, -2, -1],
                          [1, -1, 0],
                          [1, 0, 1],
                          [0, 0, 0],
                          [1, 13, 14],
                          [9, 1, 10]
                          ])
def test_addition(start_gui: SimpleCalculator, first, other, result):
    start_gui.first.focus_set()
    start_gui.first.delete(0, tk.END)
    start_gui.first.insert(0, str(first))
    start_gui.other.focus_set()
    start_gui.other.delete(0, tk.END)
    start_gui.other.insert(0, str(other))
    start_gui.operation.set('+')
    start_gui.button.focus_set()
    start_gui.window.after(10, lambda: start_gui.message.destroy() )
    start_gui.button.invoke()
    assert start_gui.result == result


@pytest.mark.parametrize(['first', 'other', 'result'],
                         [[1, 2, -1],
                          [1, 3, -2],
                          [2, 6, -4],
                          [1, -2, 3],
                          [1, -1, 2],
                          [1, 0, 1],
                          [0, 0, 0],
                          [1, 13, -12],
                          [9, 1, 8],
                          ['a', 'b', None],
                          [1, 'b', None],
                          ['a', 1, None]
                          ])
def test_subtraction(start_gui: SimpleCalculator, first, other, result):
    start_gui.first.focus_set()
    start_gui.first.delete(0, tk.END)
    start_gui.first.insert(0, str(first))
    start_gui.other.focus_set()
    start_gui.other.delete(0, tk.END)
    start_gui.other.insert(0, str(other))
    start_gui.operation.set('-')
    start_gui.button.focus_set()
    start_gui.window.after(10, lambda: start_gui.message.destroy() )
    start_gui.button.invoke()
    assert start_gui.result == result


@pytest.mark.parametrize(['first', 'other', 'result'],
                         [[1, 2, 2],
                          [1, 3, 3],
                          [2, 6, 12],
                          [1, -2, -2],
                          [1, -1, -1],
                          [1, 0, 0],
                          [0, 0, 0],
                          [1, 13, 13],
                          [9, 1, 9]
                          ])
def test_mult(start_gui: SimpleCalculator, first, other, result):
    start_gui.first.focus_set()
    start_gui.first.delete(0, tk.END)
    start_gui.first.insert(0, str(first))
    start_gui.other.focus_set()
    start_gui.other.delete(0, tk.END)
    start_gui.other.insert(0, str(other))
    start_gui.operation.set('*')
    start_gui.button.focus_set()
    start_gui.window.after(10, lambda: start_gui.message.destroy() )
    start_gui.button.invoke()
    assert start_gui.result == result


@pytest.mark.parametrize(['first', 'other', 'result'],
                         [[1, 2, 0.5],
                          [1, 3, 1/3],
                          [2, 6, 1/3],
                          [1, -2, -0.5],
                          [1, -1, -1],
                          [1, 0, None],
                          [0, 0, None],
                          [1, 13, 1/13],
                          [9, 1, 9]
                          ])
def test_div(start_gui: SimpleCalculator, first, other, result):
    start_gui.first.focus_set()
    start_gui.first.delete(0, tk.END)
    start_gui.first.insert(0, str(first))
    start_gui.other.focus_set()
    start_gui.other.delete(0, tk.END)
    start_gui.other.insert(0, str(other))
    start_gui.operation.set('/')
    start_gui.button.focus_set()
    start_gui.window.after(10, lambda: start_gui.message.destroy() )
    start_gui.button.invoke()
    assert start_gui.result == result
