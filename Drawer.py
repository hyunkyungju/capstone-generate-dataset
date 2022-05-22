from time import sleep

import matplotlib.pyplot as plt
from torch.utils.data import Dataset
import glob
from PIL import Image
import jsonlines
import os
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np


def draw_graph():
    years = ["2021", "2020", "2019"]
    # years = ["2021"]
    for year in years:
        print(year)
        x = range(0, 10)
        ratings = list()
        with jsonlines.open(f"iclr{year}_metadata.jsonl") as read_file:
            for line in read_file.iter():
                ratings.append(line['rating'])
        y = [0 for _ in range(10)]
        cnt = 0
        for rating in ratings:
            y[int(rating)] += 1
            cnt +=1
        print(y)
        print("total:", cnt)
        plt.xticks(np.arange(0, 10))
        plt.xlabel('Rating')
        plt.yticks(np.arange(0, 1100, 100))
        plt.ylabel('Number of Papers')
        plt.bar(x, y, color='#1f77b4')
        plt.ylim(0, 1000)
        for i, v in enumerate(x):
            plt.text(v, y[i], y[i],
                     fontsize=9,
                     color='#1f77b4',
                     horizontalalignment='center',  # horizontalalignment (left, center, right)
                     verticalalignment='bottom')  # verticalalignment (top, center, bottom)
        plt.title(f'{year} Rating Distribution', pad=10)

        plt.savefig(f'rating_graph_{year}')
        plt.show()
        sleep(0.5)


def draw_all_graph():
    years = ["2021", "2020", "2019"]
    x = range(0, 10)
    ratings = list()
    for year in years:
        with jsonlines.open(f"iclr{year}_metadata.jsonl") as read_file:
            for line in read_file.iter():
                ratings.append(line['rating'])
    y = [0 for _ in range(10)]
    cnt = 0
    for rating in ratings:
        y[int(rating)] += 1
        cnt +=1
    print(y)
    print("total:", cnt)
    plt.xticks(np.arange(0, 10))
    plt.xlabel('Rating')
    plt.yticks(np.arange(0, 2100, 200))
    plt.ylim(0, 2000)
    plt.ylabel('Number of Papers')
    plt.bar(x, y, color='#1f77b4')
    for i, v in enumerate(x):
        plt.text(v, y[i], y[i],
                 fontsize=9,
                 color='#1f77b4',
                 horizontalalignment='center',  # horizontalalignment (left, center, right)
                 verticalalignment='bottom')  # verticalalignment (top, center, bottom)
    plt.title(f'2021 ~ 2019 Rating Distribution', pad=10)

    plt.savefig(f'rating_graph_all')
    plt.show()
    sleep(0.5)


class Drawer:
    def __init__(self):
        pass
