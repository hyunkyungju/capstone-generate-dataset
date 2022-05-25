
import jsonlines
import pandas as pd

def make_df():
    rating_dict = {}
    with jsonlines.open("iclr2021_metadata.jsonl") as read_file:
        for line in read_file.iter():
            rating_dict[line['forum']] = line['rating']


    img_dict = {}
    with jsonlines.open("cnt.jsonl") as read_file:
        for line in read_file.iter():
            img_dict[line['forum']] = line['cnt']

    df = pd.DataFrame([rating_dict, img_dict])
    df.head()

def draw_scatter():
    make_df()