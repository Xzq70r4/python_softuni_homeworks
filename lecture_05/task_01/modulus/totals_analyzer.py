from lecture_05.task_01.constants import KEY_PRICE, KEY_TS
from lecture_05.task_01.modulus.base.base_analyzer import BaseAnalyzer


class TotalsAnalyzer(BaseAnalyzer):

    def __init__(self):
        super().__init__()
        self.total_count = 0
        self.total_amount = 0
        self.min_timestamp = None
        self.max_timestamp = None

    def analyze_sale(self, sale: dict):
        self.total_amount += sale[KEY_PRICE]
        self.total_count += 1
        ts = sale[KEY_TS]

        if self.min_timestamp is None or ts < self.min_timestamp:
            self.min_timestamp = ts
        if self.max_timestamp is None or ts > self.max_timestamp:
            self.max_timestamp = ts

    def print_results(self):
        print("""
Обобщение
---------

    Общ брой продажби: {total_count}
    Общо сума продажби: {total_amount:.2f} €
    Средна цена на продажба: {average_price: .2f} €
    Начало на период на данните: {min_ts}
    Край на период на данните: {max_ts}
        """.format(
            total_count=self.total_count,
            total_amount=self.total_amount,
            average_price=self.total_amount / self.total_count if self.total_count else None,
            min_ts=self.min_timestamp,
            max_ts=self.max_timestamp,
        ))
