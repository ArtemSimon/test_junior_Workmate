from app.filters.interface_filter import IFilter
from typing import Any
from app.logs.logger import logger


class SmallerThanFilter(IFilter):

    def apply(self, data: list[dict[str,Any]], column:str, value:Any) -> list[dict[str,Any]]:
        
        """Тут мы возращаем строки удовлетворяющие условию >"""
        filtered_data = []
        
        # Проверяем существования колонки
        if column not in data[0]:
            error_msg = f"Колонка '{column}' не найдена"
            logger.error(error_msg)
            raise KeyError(error_msg)
        
        for row in data:
            column_value = row[column]

            try:
                if self.validate_number(column_value,value,"<"):
                    if float(column_value) < float(value):
                        filtered_data.append(row)

            except ValueError as e:
                logger.info(f'Пропуск строки {row}: {str(e)}')
      
        return filtered_data

