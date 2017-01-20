from lecture_05.modulus.base.base_analyzer import BaseAnalyzer
from lecture_05.task_01.constants import KEY_PRICE


class AmountGroupedAnalyzer(BaseAnalyzer):
    group_by_title = ''

    def __init__(self):
        super().__init__()
        self.amounts_by_category = {}  # key : category name  ,  value : accumulated sum of sales

    def analyze_sale(self, sale):
        price = sale[KEY_PRICE]
        group_by_value = self.get_group_by_value(sale)
        if group_by_value not in self.amounts_by_category:
            self.amounts_by_category[group_by_value] = 0
        self.amounts_by_category[group_by_value] += price

    def get_group_by_value(self, sale):
        ...

    def print_results(self):
        amounts_by_category_sorted = sorted(self.amounts_by_category.items(), key=lambda x: x[1], reverse=True)
        print("""
Сума на продажби по {} (top 5)
-----------------------------
        """.format(self.group_by_title))

        for category_name, total_amount, in amounts_by_category_sorted[:5]:
            print("    {}: {:.2f} €".format(category_name, total_amount))
