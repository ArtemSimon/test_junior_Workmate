from app.aggregate.interface_aggregate import IAggregation
from typing import Any
from app.logs.logger import logger


class AvgAggregator(IAggregation):

    def aggregated_secondory(self, data: list[dict[str, Any]], column:str) -> float|int:
        """Тут реализуем метод основной метод, который аггрегирует данные находя средне арифметическое"""

        valid_data = [row[column] for row in data if column in row]
        return sum(valid_data) / len(valid_data)
    


