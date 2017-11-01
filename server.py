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

@app.route("/")
def hello():
    return flask.render_template('base.html')

@app.route("/search/")
def search(query=None):
    query = query if query else flask.request.args.get('query')
    found = []
    for paperid, paper in papers:
        if query.lower() in paper.lower():
            if paperid in keys:
                d = dict(id=paperid, title=keys[paperid]['content']['title'], data=keys[paperid])
                found.append(d)
    return flask.render_template('base.html', query=query, results=found)
