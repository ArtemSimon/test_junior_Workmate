from app.filters.interface_filter import IFilter
from app.filters.equals_filter import EqualsFilter
from app.filters.smaller_than_filter import SmallerThanFilter
from app.filters.larger_than_filter import LargerThanFilter
from app.logs.logger import logger

class Filter_Operators():

    def create_filter(self, operators:str) -> IFilter:
        filters = {
            ">": LargerThanFilter(),
            "<": SmallerThanFilter(),
            '=': EqualsFilter()
        }
        if operators not in filters:
            logger.error(f'Нету такого оператора {operators}')
        return filters[operators]
    
