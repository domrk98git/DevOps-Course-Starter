from flask import Flask,render_template,url_for,redirect,request
from todo_app.data import trelloitems
from todo_app.flask_config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/Add', methods=['POST'])
def add_new():
    title = request.form["title"]   
    trelloitems.create_item(title)
    return redirect(url_for('index'))

@app.route('/UpdateToDone',methods=['GET'])
def update():
    id = request.args.get('id')
    trelloitems.UpdateToDone(id)
    return redirect(url_for('index'))

@app.route('/')
def index():
    items = trelloitems.fetch_items(os.getenv('TODOID'),'TODO ITEMS')
    items += trelloitems.fetch_items(os.getenv('PENDINGID'),'PENDING ITEMS')
    items += trelloitems.fetch_items(os.getenv('DONEID'),'DONE ITEMS')

    return render_template('index.html',items=items)
    

if __name__ == '__main__':
    app.run()
