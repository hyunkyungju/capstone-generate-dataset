# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import torch
from torch.utils.data import DataLoader

from torchvision import transforms

from Converter import convert_pdf_to_img
from Crawler import crawl_iclr_2021
from paper_data_set import PaperDataSet


def data_set_usage_ex(dataset_file_name):
    dataset_file_name = 'dataset.pt'
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
    pdf_path = "../dataset/pdf/iclr21/"
    image_path = "../dataset/image/iclr21/"
    dataset_file_name = 'dataset.pt'

    # crawl_iclr_2021(pdf_path)

    convert_pdf_to_img(pdf_path, image_path)

    make_save_data_set(image_path, dataset_file_name)

    # data_set_usage_ex(dataset_file_name)
