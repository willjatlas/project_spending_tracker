from flask import Flask, render_template

from controllers.transactions_controller import transactions_blueprint
from controllers.tags_controller import tags_blueprint
from controllers.merchants_controller import merchants_blueprint
from controllers.users_controller import users_blueprint

app = Flask(__name__)

app.register_blueprint(transactions_blueprint)
app.register_blueprint(tags_blueprint)
app.register_blueprint(merchants_blueprint)
app.register_blueprint(users_blueprint)


@app.route('/')
def home():
    return render_template('home.html' , title= "Home")

if __name__ == '__main__':
    app.run(debug=True)