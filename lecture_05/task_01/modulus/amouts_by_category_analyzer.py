from lecture_05.task_01.constants import KEY_ITEM_ID
from lecture_05.task_01.modulus.base.amouts_grouped_analyzer import AmountGroupedAnalyzer


class AmountsByCategoryAnalyzer(AmountGroupedAnalyzer):
    group_by_title = 'категории'

    def __init__(self, catalog):
        super().__init__()
        self.catalog = catalog

    def get_group_by_value(self, sale):
        item_id = sale[KEY_ITEM_ID]
        return self.catalog.get(item_id, None)