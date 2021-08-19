import csv


def make_tag_dict() -> dict:
    res = {}
    with open('/Users/kazuki/PycharmProjects/auto_instagram/tag/auto_like_tag.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            res[str(row[0]).strip()] = int(str(row[1]).strip())
    return res
