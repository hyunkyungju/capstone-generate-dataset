from torch.utils.data import Dataset
import glob
from PIL import Image
import jsonlines
import os
from tqdm import tqdm

class PaperDataSet(Dataset):
    def __init__(self, overall_image_path, transform=None):
        print("initialize data sets")
        self.transform = transform
        rating_dict = {}
        self.image_list = list()
        self.score_list = list()
        years = ["2021", "2020", "2019"]
        for year in years:
            year_image_path = overall_image_path+year+"/"
            with jsonlines.open(f"iclr{year}_forum_rating.jsonl") as read_file:
                for line in read_file.iter():
                    rating_dict[line['forum']] = line['review_rating']
            input_paths = os.listdir(year_image_path)
            for one_file_image_path in tqdm(input_paths, desc="make data set"):
                image_path = year_image_path + one_file_image_path + "/"
                before_add_size = len(self.image_list)
                self.image_list.extend(glob.glob(image_path + "*.jpg")) # glob: 폴더 내의 파일 찾아줌
                rating = rating_dict[one_file_image_path]
                self.score_list.extend([rating] * (len(self.image_list)-before_add_size))

    def __len__(self):
        return len(self.image_list)

    def __getitem__(self, idx):
        image_path = self.image_list[idx]
        label = self.score_list[idx]
        img = Image.open(image_path)
        if self.transform is not None:
            img = self.transform(img)

        return img, label
