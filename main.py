# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import torch
from torch.utils.data import DataLoader

from torchvision import transforms
import openreview
from Converter import convert_pdf_to_img
from Crawler import crawl_iclr
from paper_data_set import PaperDataSet
import torchvision

def data_set_usage_ex(dataset_file_name):

    dataloader = DataLoader(dataset=torch.load(dataset_file_name),
                           batch_size=1,
                            shuffle=False,
                            drop_last=False)

    for epoch in range(1):
        print(f"epoch: {epoch}")
        for batch in dataloader:
            img, label = batch
            print(label)


def make_save_data_set(image_path, dataset_file_name):
    print("start to make data set")
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        # transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    dataset = PaperDataSet(image_path, transform=transform)
    print(f"data set length: {dataset.__len__()}")

    torch.save(dataset, dataset_file_name)
    print("save data sets")


if __name__ == '__main__':
    # pdf_path = "../dataset/pdf/"
    # image_path = "../dataset/image/"
    # dataset_file_name = 'dataset-iclr-3years.pt'

    # client = openreview.Client(
    #     baseurl='https://api.openreview.net',
    #     username='',
    #     password=''
    # )

    # years = ["2021", "2020", "2019"]
    # for year in years:
        # crawl_iclr(pdf_path, year)
        # convert_pdf_to_img(pdf_path+"iclr"+year+"/", image_path+"iclr"+year+"/")

    image_path = "./image/"
    dataset_file_name = 'dataset-iclr-2021.pt'

    make_save_data_set(image_path, dataset_file_name) # 한번만 실행하시고 주석처리해주세요.

    data_set_usage_ex(dataset_file_name)
