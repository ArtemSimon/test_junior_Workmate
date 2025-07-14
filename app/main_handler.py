from app.args_parser import ArgsParser
from app.csv_loader import CSVLoader
from app.filters.filter_operators import Filter_Operators
from app.aggregate.operators_aggregation import OperatorsAggregation
from app.printer import Printer
from app.logs.logger import logger

class MainHandler:
    """Главный класс, координирующий работу всех компонентов"""
    
    def __init__(self):
        self.parser = ArgsParser()
        self.loader = CSVLoader()
        self.filter_factory = Filter_Operators()
        self.aggregator_factory = OperatorsAggregation()
        self.printer = Printer()

    def main_func(self) -> None:
        """Основной метод выполнения команд"""
        try:
            # 1 Парсим аргументы
            args = self.parser.parse()
            logger.info(f"Получены аргументы: {args}")

            # 2 Загружаем данные 
            data = self.loader.load_file(args.file)
            logger.info(f"Загружено {len(data)} строк")

            # 3 Применяем фильтр (если есть)
            if args.where:
                column, operator, value = self.parser._parse_condition(args.where)
                logger.info(f"Применение фильтра: {column} {operator} {value}")
                filter_operation = self.filter_factory.create_filter(operator)
                data_filters = filter_operation.apply(data, column, value)
                    
                if not args.aggregate:
                    self.printer.print_data(data_filters)

            # 4 Применяем аггрегацию (если есть)
            if args.aggregate:
                column, operation = self.parser._parse_aggregate(args.aggregate)
                logger.info(f"Выполнение агрегации: {operation}({column})")

                aggregator = self.aggregator_factory.create_aggregator(operation)
                if args.where:
                    result = aggregator.aggregated(data_filters, column)
                else:
                    result = aggregator.aggregated(data, column)
            
                self.printer.print_aggregate(operation,result)

            # Выполняется если ничего не указано 
            if not args.where and not args.aggregate:
                self.printer.print_data(data)

        except Exception as e:
            logger.critical(f"Ошибка выполнения: {str(e)}")
            self.printer.print_error(str(e))
            raise

    @classmethod
    def run(cls):
        """Точка входа в приложение"""
        handler = cls()
        handler.main_func()

main_comand = MainHandler()
main_comand.run()