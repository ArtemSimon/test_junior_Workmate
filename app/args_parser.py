import argparse
import os


class ArgsParser():
    def __init__(self, csv_column: list[str]|None = None):
        self.csv_column = csv_column
    
    def parse(self) -> argparse.Namespace:
        """Создаем парсер, затем парсим и валидируем аргументы командной строки"""
        parser = self._create_parser()
        args = parser.parse_args()
        self._validate_args(args)
        return args
        
    
    def _create_parser(self) -> argparse.ArgumentParser:
        """Отдельная функция для создания парсера
        сделал это чтобы разделить функциональность и уменьшить код в самой функции"""

        parser = argparse.ArgumentParser(
            description='Необходим для обработки CSV-файлов(фильтрация и агрегация)'
        )
        parser.add_argument(
            '--file',
            required=True,
            help='Указывается путь к csv-файлу (обязательный аргумент!)'
        )
        parser.add_argument(
            '--where',
            help="Указываем условия фильтрации"
        )
        parser.add_argument(
            '--aggregate',
            help='Указываем условия агрегации'
        )
        return parser
    
    def _validate_args(self,args:argparse.Namespace) -> None:
        """Тут проверяем корректность аргументов"""
        if not os.path.exists(args.file):
            raise FileExistsError(f'Файл {args.file} не найден')
        
        if not args.file.endswith('.csv'):
            raise ValueError(f'Файл не с тем разширением, должен быть .csv')
        
        if self.csv_column:
            if args.where:
                column,_,_ = self._parse_condition(args.where)
                if column not in self.csv_column:
                    raise ValueError(f'Колонка {column} не найдена. Имеющиеся колонки {self.csv_column}')
            
            if args.aggregate:
                column,_ = self._parse_aggregate(args.aggregate)
                if column not in self.csv_column:
                    raise ValueError(f'Колонка {column} не найдена. Имеющиеся колонки {self.csv_column}')
    
    @staticmethod
    def _parse_condition(condition:str) -> tuple[str,str,str]:
        """Тут мы парсим фильтрацию на tuple (колонка, оператор, значение)"""
        operators = ['>', '=', '<']
        for operator in operators:
            if operator in condition:
                col,val = condition.split(operator,maxsplit=1)
                return col.strip(),operator,val.strip()
        raise ValueError(f'Неверный формат для фильтрации {condition}')
    
    @staticmethod
    def _parse_aggregate(aggregate:str) -> tuple[str,str]:
        """Тут мы парсим агрегацию на тот же tuple (колонка, операция)"""

        if '=' not in aggregate:
            raise ValueError(f'Неверный формат для фильтрации {aggregate}')
        col,agg_action = aggregate.split('=',maxsplit=1)
        if agg_action not in ['min','max','avg']:
            raise ValueError(f'Недопустимая операция для агрегации {agg_action}')
        
        return col.strip(),agg_action.strip()
