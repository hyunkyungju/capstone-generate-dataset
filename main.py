import cv2
import os

from ImageToBinaryConverter_Split12 import image_to_binary_split

if __name__ == '__main__':
    # image_to_binary("../dataset/test/image/occlusion/", "../dataset/test/binary/occlusion/")
    # count_image_all_pdf()
    # draw_scatter()
    # random_generator()
    # make_compare()
    #image_to_binary_cut("../dataset/image/iclr2021/", "../dataset/binary/iclr2021_cut/")
    #image_cut("../dataset/image/iclr2021/", "../dataset/image/test/")
    # check_all_cut("../dataset/image/iclr2021/")
    image_to_binary_split("../dataset/image/iclr2021/", "../dataset/binary/iclr2021_split/")


    # binary_to_image()
    # crawl_iclr("../dataset/pdf/", "2021")
    # convert_pdf_to_img("../dataset/pdf/iclr2021/", "../dataset/image/iclr2021/")

    # image_to_binary("../dataset/image/iclr2021/", "../dataset/binary/iclr2021/")
    # make_save_data_set("../dataset/binary/", "dataset.pt")
    # data_set_usage_ex("dataset.pt")




