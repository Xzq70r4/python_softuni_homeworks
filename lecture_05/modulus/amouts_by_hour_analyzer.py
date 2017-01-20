from lecture_05.modulus.base.amouts_grouped_analyzer import AmountGroupedAnalyzer
from lecture_05.task_01.constants import KEY_TS


class AmountsByHourAnalyzer(AmountGroupedAnalyzer):
    group_by_title = 'категории'

    def get_group_by_value(self, sale):
        ts = sale[KEY_TS]
        ts = ts.replace(minute=0, second=0, microsecond=0)
        return ts
