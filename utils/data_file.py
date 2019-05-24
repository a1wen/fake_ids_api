import csv


class DataFile:
    """Класс для работы с файлом, в котором описаны тесты"""

    def __init__(self, file):
        csv_data = csv.DictReader(file, delimiter=',')

        self._data = {
            data['msisdn']: data for data in csv_data
        }

    def get(self, msisdn, default=None):
        return self._data.get(msisdn, default)
