from app.aggregate.interface_aggregate import IAggregation
from typing import Any
from app.logs.logger import logger



class MinAggregate(IAggregation):


    def aggregated_secondory(self, data: list[dict[str,Any]], column:str) -> float|int:
        """Тут реализуем метод основной метод, который аггрегирует данные находя минимальное значение"""

        valid_data_for_min = [row[column] for row in data if column in row]

        return min(valid_data_for_min)
    
