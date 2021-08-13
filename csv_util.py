import csv


def make_tag_dict() -> dict:
    res = {}
    with open('tag/auto_like_tag.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            res[str(row[0]).strip()] = int(str(row[1]).strip())
    return res
