from abc import abstractmethod, ABC
from typing import Any
from app.logs.logger import logger

class IFilter(ABC):
    """Реализуем абстрактный класс для всех фильтров для удобства потом маштабирования различный функций"""

    @abstractmethod
    def apply(self,data: list[dict[str,Any]],column:str,value: Any) -> list[dict[str,Any]]:
        """Тут реализуется общий метод для фильтрации данных"""
        
        pass 

    
    def validate_number(self, column_value: Any, value:Any, operator: str) -> None:
        
        try:
            # Пробуем преобразовать в float (если это строка с числом)
            column_num = float(column_value) if isinstance(column_value, str) else column_value
            value_num = float(value) if isinstance(value, str) else value
            
            # Проверяем, что оба значения — числа
            if not isinstance(column_num, (float, int)) or not isinstance(value_num, (float, int)):
                    raise ValueError("Тут есть нечисловое значение")
            
            return True
        except (ValueError, TypeError):
            message = (
                f"Оператор '{operator}' требует числа. "
                f"Получено: {column_value!r} ({type(column_value)}) и {value!r} ({type(value)})"
            )
            logger.error(message)
            raise ValueError(message)