import csv

COLUMN_ITEM_ID = 0
COLUMN_CATEGORY = 5

def load_catalog(file_path: str) -> dict:
    """
    Expected columns in catalog file:
     1. Id number
     2. Product name
     3. Product color/colors
     4. Group of product
     5. Sports, for which the article is intended
     6. Category
     7. Sub Category
     8. Gender and Age Group (Men, Women, Unisex, Infant)

    :param file_path: File path
    :return result:
        {
            # item_id : category name
            "J11328": "SHOES",
            ...
        }
    """

    result = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            item_id = row[COLUMN_ITEM_ID]
            category = row[COLUMN_CATEGORY]
            result[item_id] = category

    return result
