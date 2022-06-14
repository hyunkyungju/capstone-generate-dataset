import argparse
import json
import os
from collections import defaultdict
from tqdm import tqdm
import openreview


# [error] forum: _qJXkf347k

def crawl_iclr(pdf_path, year):
    client = openreview.Client(
        baseurl='https://api.openreview.net',
        username='',
        password=''
    )

    print(f'start crawl iclr {year}')

    # Get submission lists
    submissions = openreview.tools.iterget_notes(
        client, invitation=f'ICLR.cc/{year}/Conference/-/Blind_Submission')
    submissions_by_forum = {n.forum: n for n in submissions}
    print(f"number of forums: {submissions_by_forum.__len__()}")

    # Get reviews
    '''
    2021: 2595, 2979    
    2020: 2213, 2561
    2019: 1419, 1565
    
    뉴립스
    2021: 2769, 2763
    '''

    if year == "2019":
        reviews = openreview.tools.iterget_notes(
            client, invitation=f'ICLR.cc/{year}/Conference/-/Paper.*/Official_Review')
    else:
        reviews = openreview.tools.iterget_notes(
            client, invitation=f'ICLR.cc/{year}/Conference/Paper.*/-/Official_Review')

    reviews_by_forum = defaultdict(list)
    for review in reviews:
        reviews_by_forum[review.forum].append(review)
    print(f"number of reviews: {reviews_by_forum.__len__()}")

    # Build a list of metadata
    metadata = []
    for forum in submissions_by_forum:
        forum_reviews = reviews_by_forum[forum]
        review_ratings = [n.content['rating'] for n in forum_reviews]
        value = 0
        for review in review_ratings:
            value += int(review[0])
        rating = value / len(review_ratings)
        forum_metadata = {
            'forum': forum,
            'rating': rating
        }
        metadata.append(forum_metadata)

    print('writing metadata to file')
    with open(os.path.join("../../", f'iclr{year}_metadata.jsonl'), 'w') as file_handle:
        for forum_metadata in metadata:
            file_handle.write(json.dumps(forum_metadata) + '\n')

    outdir = pdf_path+"iclr"+year+"/"
    print('start to save pdf')
    os.makedirs(outdir)
    for forum_metadata in tqdm(metadata, desc=f'iclr {year} getting pdfs'):
        try:
            pdf_binary = client.get_pdf(forum_metadata['forum'])
            pdf_outfile = os.path.join(outdir, '{}.pdf'.format(forum_metadata['forum']))
            with open('../../output.pdf', 'wb') as op:
                op.write(pdf_binary)
            with open(pdf_outfile, 'wb') as file_handle:
                file_handle.write(pdf_binary)
        except:
            print(f"[error][crawl pdf][iclr {year}] forum: {forum_metadata['forum']}")


class Crawler:
    def __init__(self):
        pass
