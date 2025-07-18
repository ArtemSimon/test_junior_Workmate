import sys
from tabulate import tabulate
from typing import Any


class Printer():
    def __init__(self,table_format: str='grid'):
        self.table_format= table_format

    def print_data(self,data: list[dict[str,Any]]) -> None:
        """Метод для вывода уже обработанных данных в удобном формате"""
        if not data:
            self.print_error('Нет данных для вывода')
        print(tabulate(data,headers='keys',tablefmt=self.table_format))

    def print_aggregate(self,operation:str,result:float|int) -> None:
        """Вывод уже агрегированных данных в удобном формате"""
        table = [
            [operation],
            [result]
        ]
        print(tabulate(table,tablefmt=self.table_format))

    def print_error(self,message:str) -> None:
        """Единый интерфейс вывода ошибок"""
        print(f'[!] {message}',file=sys.stderr)



