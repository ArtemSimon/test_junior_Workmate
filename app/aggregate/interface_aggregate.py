from abc import ABC, abstractmethod
import time
from typing import Any
from app.logs.logger import logger 

class IAggregation(ABC):

    """Абстраткный класс для так же удобства маштабирования и реализации"""
    
    
    def aggregated(self, data:list[dict[str,Any]],column: str) ->  Any:
        """Основной метод который реализуется во всех дочерних классах для общего логирования"""
        
        start_time = time.perf_counter()
        
        try:
            logger.info(
                f"Начало агрегации {self.__class__.__name__} "
                f"по колонке '{column}' ({len(data)} строк)"
            )
            
            self.validation_number(data, column)
            result = self.aggregated_secondory(data, column)
            
            logger.info(
                f"Агрегация успешна. Результат: {result:.2f} | "
                f"Время: {time.perf_counter() - start_time:.4f} сек"
            )
            
            return result
        
        except Exception as e:
            logger.error(
                f"Ошибка агрегации {self.__class__.__name__}: {str(e)} | "
                f"Колонка: {column} | "
                f"Время: {time.perf_counter() - start_time:.4f} сек"
            )
            raise
    
    @abstractmethod
    def aggregated_secondory(self, data: list[dict[str, Any]], column: str) -> float|int:
        """Сама логика агрегации для реализации в подклассах"""
        pass


    def validation_number(self,data: list[dict[str,Any]],column:str) -> None:
        """Проверка числового типа в колонке, тк аггрегация применяется только к числовому типу"""

        if not all(isinstance((row.get(column)), (int,float)) for row in data if column in row):
            message_for_error = f"Колонка '{column}' содержит нечисловые данные"
            logger.error(message_for_error)
            raise ValueError(message_for_error)
        

