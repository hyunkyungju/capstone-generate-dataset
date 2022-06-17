
import jsonlines


def make_compare():
    lst = list()
    with jsonlines.open("../../data/rating-data/iclr2021_metadata.jsonl") as read_file:
        for line in read_file.iter():
            lst.append(float(line['rating']))

    avg = sum(lst)/len(lst)
    print("avg:", avg)

    diff_list = list()

    for rating in lst:
        diff_list.append(abs(rating-avg))

    print(sum(diff_list)/len(diff_list))