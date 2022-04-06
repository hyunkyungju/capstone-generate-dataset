import argparse
import json
import os
from collections import defaultdict
from tqdm import tqdm
import openreview


def download_iclr21(client, outdir='./'):
    print('getting metadata...')
    # get all ICLR '19 submissions, reviews, and meta reviews, and organize them by forum ID
    # (a unique identifier for each paper; as in "discussion forum").
    submissions = openreview.tools.iterget_notes(
        client, invitation='ICLR.cc/2021/Conference/-/Blind_Submission')
    submissions_by_forum = {n.forum: n for n in submissions}
    print(f"number of forums: {submissions_by_forum.__len__()}")

    # Build a list of metadata.
    # For every paper (forum), get the review ratings, the decision, and the paper's content.
    metadata = []
    for forum in submissions_by_forum:
        forum_metadata = {
            'forum': forum,
        }
        metadata.append(forum_metadata)

    print('start to save pdf')

    # os.makedirs(outdir)
    for forum_metadata in tqdm(metadata, desc='getting pdfs'):
        try:
            pdf_binary = client.get_pdf(forum_metadata['forum'])
            pdf_outfile = os.path.join(outdir, '{}.pdf'.format(forum_metadata['forum']))
            with open(pdf_outfile, 'wb') as file_handle:
                file_handle.write(pdf_binary)
        except:
            print("[error] forum:", forum_metadata['forum'])
# [error] forum: _qJXkf347k

def crawl_iclr_2021(pdf_path):
    client = openreview.Client(
        baseurl='https://api.openreview.net',
        username='',
        password=''
    )
    download_iclr21(client, pdf_path)


class Crawler:
    def __init__(self):
        pass
