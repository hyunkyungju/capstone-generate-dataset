import random

import jsonlines


def get_random(n):
    rating_dict = {}
    with jsonlines.open("../../data/rating-data/iclr2021_metadata.jsonl") as read_file:
        for line in read_file.iter():
            if int(line['rating'])==n:
                rating_dict[line['forum']] = line['rating']
    return rating_dict

def random_generator():
    for i in range(2, 9):
        dict_ = get_random(i)
        index = random.randint(0, len(dict_)-1)
        page_number = random.randint(2, 4)
        print(list(dict_.items())[index], "page:", page_number)