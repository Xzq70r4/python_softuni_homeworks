from lecture_05.task_01.constants import KEY_CITY
from lecture_05.task_01.modulus.base.amouts_grouped_analyzer import AmountGroupedAnalyzer


class AmountsByCityAnalyzer(AmountGroupedAnalyzer):
    group_by_title = 'категории'

    def get_group_by_value(self, sale):
        return sale[KEY_CITY]