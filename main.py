# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import torch
from torch.utils.data import DataLoader

from torchvision import transforms
import openreview
from Converter import convert_pdf_to_img
from Crawler import crawl_iclr
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
    pdf_path = "../dataset/pdf/"
    image_path = "../dataset/image/"
    dataset_file_name = 'dataset.pt'

    # crawl_iclr(pdf_path, "2021")

    client = openreview.Client(
        baseurl='https://api.openreview.net',
        username='',
        password=''
    )

    year = "2021"

    iclr19_invitations_iterator = openreview.tools.iterget_invitations(
        client, regex='NeurIPS.cc/2020/Conference')

    for invitation in iclr19_invitations_iterator:
        print(invitation.id)
# Public_Comment

    """
    NeurIPS.cc/2021/Conference/-/Reduced_Load
    NeurIPS.cc/2021/Conference/-/Recruit_Reviewers
    NeurIPS.cc/2021/Conference/-/Recruit_Ethics_Reviewers
    NeurIPS.cc/2021/Conference/-/Blind_Submission
    NeurIPS.cc/2021/Conference/Paper79/-/Withdraw
    NeurIPS.cc/2021/Conference/Paper11535/-/Official_Comment
    NeurIPS.cc/2021/Conference/Paper5854/-/Decision
    NeurIPS.cc/2021/Conference/Paper327/-/Public_Comment
    NeurIPS.cc/2021/Conference/Paper10608/-/Desk_Reject
    """

    #reviews2 = openreview.tools.iterget_notes(
    #   client, invitation='NeurIPS.cc/2021/Conference/Paper.*/-/Withdraw')
    #  =f'NeurIPS.cc/{year}/Conference/Paper.*/-/Official_Review')
    #print(sum(1 for _ in reviews2))

    #for r in reviews2:
    #    print(r)
    #    break

    # 리뷰가 10749개나 된다... 뭐지.. 

    # convert_pdf_to_img(pdf_path, image_path)

    # make_save_data_set(image_path, dataset_file_name)

    # data_set_usage_ex(dataset_file_name)
