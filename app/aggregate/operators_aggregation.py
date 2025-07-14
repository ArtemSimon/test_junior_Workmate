from app.aggregate.avg_aggregator import AvgAggregator
from app.aggregate.max_aggregator import MaxAggregator
from app.aggregate.min_aggeregator import MinAggregate
from app.aggregate.interface_aggregate import IAggregation
from app.logs.logger import logger


class OperatorsAggregation():


    @staticmethod
    def create_aggregator(aggregator_operation:str) -> IAggregation:
        """Создаем аггрегатор по типу операции"""
        aggregators ={
            'avg': AvgAggregator(),
            'max': MaxAggregator(),
            'min': MinAggregate()
        }

        if aggregator_operation not in aggregators:
            error_message = f"Неподдерживаемый тип агрегации: {aggregator_operation}"
            logger.error(error_message)
            raise ValueError(error_message)
        
        return aggregators[aggregator_operation.lower()]
    
