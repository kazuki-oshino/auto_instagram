import csv
import sys

csv_path_dict = {
    1: '/Users/kazuki/PycharmProjects/auto_instagram/tag/auto_like_tag1.csv',
    2: '/Users/kazuki/PycharmProjects/auto_instagram/tag/auto_like_tag2.csv',
    3: '/Users/kazuki/PycharmProjects/auto_instagram/tag/auto_like_tag3.csv',
    4: '/Users/kazuki/PycharmProjects/auto_instagram/tag/auto_like_tag4.csv',
    5: '/Users/kazuki/PycharmProjects/auto_instagram/tag/auto_like_tag_holi1.csv',
    6: '/Users/kazuki/PycharmProjects/auto_instagram/tag/auto_like_tag_holi2.csv',
    7: '/Users/kazuki/PycharmProjects/auto_instagram/tag/auto_like_tag_holi3.csv',
    8: '/Users/kazuki/PycharmProjects/auto_instagram/tag/auto_like_tag_holi4.csv'
}


def make_tag_dict() -> dict:
    # 対象CSVを起動時引数から取得
    target_csv_key: int = 1
    args = sys.argv
    if len(args) > 1:
        target_csv_key = int(args[1])

    res = {}
    with open(csv_path_dict[target_csv_key]) as f:
        reader = csv.reader(f)
        for row in reader:
            res[str(row[0]).strip()] = int(str(row[1]).strip())
    return res
