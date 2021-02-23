from flask import Flask,render_template,url_for,redirect,request
from todo_app.data import session_items,trelloitems

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)

##@app.route('/')
##def root():
##    return redirect(url_for('index'))
 
@app.route('/Add', methods=['POST'])
def add_new():
    title = request.form["title"]   
    trelloitems.create_item(title)
    return redirect(url_for('index'))

##  if request.method == 'POST':
##        new_item = session_items.add_item('Title')
##    else:
##        items = session_items.get_items()
##        return ender_template('index.html',items=items)

@app.route('/UpdateToDone',methods=['POST', 'GET'])
def update():
    id = request.args.get('id')
    trelloitems.UpdateToDone(id)
    return redirect(url_for('index'))


@app.route('/')
def index():
    items = trelloitems.fetch_items()
    for cards in items:
        print(cards['name'] + cards['id'])
    ##new_item = session_items.add_item('Title') ## new line
    return render_template('index.html',items=items)
    

if __name__ == '__main__':
    app.run()
