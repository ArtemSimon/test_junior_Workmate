import csv
from typing import Any


class CSVLoader():
    
    def load_file(self,file_path: str) -> list[dict[str,Any]]:
        """ Загружаем csv файл и возвращаем данные в формате списка словарей
        почему такой формат, одна из причин с таким форматом удобно работать в python и tabulate принимает как раз такой формат"""
        
        try:
            with open(file_path,'r',encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                return [self._parse_row(row) for row in reader]
        
        except FileNotFoundError:
            raise ValueError(f'Файл {file_path} не найден')
        except Exception as e:
            raise {f'Ошибка при чтении CSV файла {e}'}
    
    def _return_csv_column(self, data: list[dict[str,Any]]) -> list[str]:
        """Вспомогательная функция для вывода всех колонок"""
        new_data = data[0]
        list_csv_colums = []
        for column in new_data.keys():
            list_csv_colums.append(column)
        return list_csv_colums

    def _parse_row(self,row: dict[str,str]) -> dict[str,Any]:
        """ Конвертируем (парсим) строковые значения в числа при возможности 
        мы это делаем чтобы мы могли работать с числами при фильтрации и агрегации, делаем это сразу"""
        
        parse_dict = {}
        for key,value in row.items():
            try: 
                parse_dict[key] = float(value) if '.' in value else int(value)
            except ValueError:
                parse_dict[key] = value.strip()
        return parse_dict

