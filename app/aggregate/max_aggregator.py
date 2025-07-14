from app.aggregate.interface_aggregate import IAggregation
from typing import Any
from app.logs.logger import logger


class MaxAggregator(IAggregation):

    def aggregated_secondory(self, data: list[dict[str,Any]], column:str) -> float|int:
        """Тут реализуем метод основной метод, который аггрегирует данные находя максимальное значение"""

        valid_data_for_max = [row[column] for row in data if column in row]        
 
        return max(valid_data_for_max)
