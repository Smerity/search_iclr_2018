import glob
import json
from collections import defaultdict

import numpy as np

def extract_ratings(data):
    ratings = []
    for x in data['notes']:
        if 'content' not in x: continue
        if 'rating' not in x['content']: continue
        rate = int(x['content']['rating'].split(':')[0])
        conf = int(x['content']['confidence'].split(':')[0])
        ratings.append((rate, conf))
    return sorted(ratings, reverse=True)

comments = {}
for fn in glob.glob('reviews/*'):
    try:
        key = fn.split('/')[1]
        comments[key] = json.loads(open(fn, encoding='utf-8', errors='ignore').read())
    except json.JSONDecodeError:
        pass
print('Total reviews:', len(comments))

ratings = defaultdict(list)
for key in comments.keys():
    ratings[key] = extract_ratings(comments[key])

sorted_ratings = [(k, [v[0] for v in vals]) for k, vals in ratings.items()]
sorted_ratings = sorted(sorted_ratings, key=lambda v: np.mean(v[1]) if v[1] else 0)
sorted_papers = [x[0] for x in sorted_ratings]
