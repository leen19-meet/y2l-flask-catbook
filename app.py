from flask import Flask
from flask import render_template, request
from database import get_all_cats ,cats_info, create_cat

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>')
def profile_page(id):
    cat = cats_info(id)
    return render_template("cat.html",cat=cat)

@app.route('/vote_cat/<int:id>', methods=["POST"])
def add_votes(id):
    add_vote(id)
    return redirect("/")

@app.route('/cats/create',methods=['GET', 'POST'])
def new_cat():
    if request.method == 'GET' :
        return render_template("newcat.html")
    else:
        name = request.form["name"]
        create_cat(name)
        return redirect("/")

if __name__ == '__main__':
   app.run(debug = True)

