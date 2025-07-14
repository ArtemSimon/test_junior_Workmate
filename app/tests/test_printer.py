import sys
from io import StringIO
from unittest.mock import patch
import pytest
from app.printer import Printer

@pytest.fixture
def printer():
    return Printer(table_format='grid')

@pytest.fixture
def sample_data():
    return [
        {"name": "iPhone", "price": 999},
        {"name": "Galaxy", "price": 899}
    ]

def test_print_data(printer, sample_data, capsys):
    printer.print_data(sample_data)
    captured = capsys.readouterr()
    assert "iPhone" in captured.out
    assert "Galaxy" in captured.out
    assert "price" in captured.out  # Проверяем заголовки

def test_print_data_empty_list(printer, capsys):
    with patch.object(printer, 'print_error') as mock_error:
        printer.print_data([])
        mock_error.assert_called_once_with('Нет данных для вывода')

def test_print_aggregate(printer, capsys):
    printer.print_aggregate("avg", 150.5)
    captured = capsys.readouterr()
    assert "avg" in captured.out
    assert "150.5" in captured.out

def test_print_aggregate_integer(printer, capsys):
    printer.print_aggregate("count", 5)
    captured = capsys.readouterr()
    assert "5" in captured.out

def test_print_error(printer):
    with patch('sys.stderr', new_callable=StringIO) as mock_stderr:
        printer.print_error("Test error")
        assert "[!] Test error" in mock_stderr.getvalue()

def test_print_error_empty_message(printer):
    with patch('sys.stderr', new_callable=StringIO) as mock_stderr:
        printer.print_error("")
        assert "[!] " in mock_stderr.getvalue()

