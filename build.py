from sphinx.websupport import WebSupport

import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SRCDIR = os.path.join(ROOT, '.')
BUILDDIR = os.path.join(ROOT, '_build')
INDEXDIR = os.path.join(BUILDDIR, "data", "db")


support = WebSupport(srcdir=SRCDIR,
                     builddir=BUILDDIR)

support.build()

#from sphinx.websupport.errors import *

#@app.route('/<path:docname>')
#def doc(docname):
    #username = g.user.name if g.user else ''
    #moderator = g.user.moderator if g.user else False
    #try:
        #document = support.get_document(docname, username, moderator)
    #except DocumentNotFoundError:
        #abort(404)
    #return render_template('doc.html', document=document)


#@app.route('/search')
#def search():
    #q = request.args.get('q')
    #document = support.get_search_results(q)
    #return render_template('doc.html', document=document)


#@app.route('/docs/add_comment', methods=['POST'])
#def add_comment():
    #parent_id = request.form.get('parent', '')
    #node_id = request.form.get('node', '')
    #text = request.form.get('text', '')
    #proposal = request.form.get('proposal', '')
    #username = g.user.name if g.user is not None else 'Anonymous'
    #comment = support.add_comment(text, node_id='node_id',
                                  #parent_id='parent_id',
                                  #username=username, proposal=proposal)
    #return jsonify(comment=comment)

#@app.route('/docs/get_comments')
#def get_comments():
    #username = g.user.name if g.user else None
    #moderator = g.user.moderator if g.user else False
    #node_id = request.args.get('node', '')
    #data = support.get_data(node_id, username, moderator)
    #return jsonify(**data)




#@app.route('/docs/process_vote', methods=['POST'])
#def process_vote():
    #if g.user is None:
        #abort(401)
    #comment_id = request.form.get('comment_id')
    #value = request.form.get('value')
    #if value is None or comment_id is None:
        #abort(400)
    #support.process_vote(comment_id, g.user.id, value)
    #return "success"


