import flask
app = flask.Flask(__name__)

import glob
import json

data = json.load(open('notes.json'))
keys = {}
for entry in data['notes']:
    keys[entry['id']] = entry

papers = []
for paper in glob.glob('text/papers/*'):
    papers.append([paper.split('id=')[1], open(paper, encoding='utf-8', errors='ignore').read()])
papers = sorted(papers)
print('Loaded {} papers'.format(len(papers)))

from reviewer import ratings, sorted_papers

@app.route("/")
def index():
    query = 'Top 100 papers'
    found = []
    for paperid, paper in papers:
        if paperid in sorted_papers[-100:]:
            if paperid in keys:
                rank = sorted_papers.index(paperid)
                d = dict(id=paperid, title=keys[paperid]['content']['title'], data=keys[paperid], rating=ratings[paperid], rank=rank, pct=int(100 * rank / len(sorted_papers)))
                found.append(d)
    found = sorted(found, key=lambda x: x['rank'], reverse=True)
    return flask.render_template('base.html', query=query, results=found, total_papers=len(sorted_papers))

@app.route("/search/")
def search(query=None):
    query = query if query else flask.request.args.get('query')
    found = []
    for paperid, paper in papers:
        if query.lower() in paper.lower():
            if paperid in keys:
                rank = sorted_papers.index(paperid)
                d = dict(id=paperid, title=keys[paperid]['content']['title'], data=keys[paperid], rating=ratings[paperid], rank=rank, pct=int(100 * rank / len(sorted_papers)))
                found.append(d)
    found = sorted(found, key=lambda x: x['rank'], reverse=True)
    return flask.render_template('base.html', query=query, results=found, total_papers=len(sorted_papers))
