from flask import Flask, request , render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


app.config.update(
    SECERET_KEY='rishi123',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:rishi123@localhost/catalogDB',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)

class Publication(db.Model):
    __tablename__ = 'publications'

    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(80) , nullable=False)

    def __init__(self , id , name):
        self.id = id
        self.name = name


    def __repr__(self):
        return 'The id is {} , name {} '.format(self.id , self.name)
    




class Book(db.Model):
    __tablename__='book'

    id = db.Column(db.Integer , primary_key=True)
    title = db.Column(db.String(500) , nullable=False, index=True)
    author = db.Column(db.String(450))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    #relationship
    pub_id = db.Column(db.Integer , db.ForeignKey('publications.id'))

    def __init(self, title , author, avg_rating , book_format , image , num_pages ,pub_id):

        self.title = title
        self.author =author
        self.avg_rating = avg_rating
        self.format = book_format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

        def __repr__(sefl):
            return '{} by {}'.format(self.title , self.author)
        



@app.before_first_request
def create_database():
     db.create_all()







@app.route('/')
def hello_flask():
    return 'Hello flask'


@app.route('/new/')
def query_string(greeting = 'hello Sir'):
    query_val = request.args.get('greeting', greeting)
    return '<h1> The greetings is :{0}  </h1>'.format(query_val)

@app.route('/user')
@app.route('/user/<name>')
def no_query_strings(name='mina'):
    return '<h1> hello there : {} </h1>'.format(name)


@app.route('/numbers/<int:num>')
def working_with_numbers(num):
    return '<h1> the number you picked is: '+ str(num) +'<h1>'

@app.route('/addition/<int:num1>/<int:num2>')
def add_2_numbers(num1 , num2):
    return '<h1> addition of 2 numbers '+ str(num1)+' and '+str(num2)+' is '+ str(num1+num2) + '<h1>'

@app.route('/temp')
def using_template():
    return render_template('hello.html')


#JINJA TEMPLATE
@app.route('/watch')
def top_movies():
    movie_list=[
        'Autoppsy of jane doe',
        'matrix',
        'ghost in a shell',
        'jon wick',
        'batman'
    ]

    return render_template('movies.html', movies=movie_list , name='Harry')


@app.route('/tables')
def movies_plus():
    movies_dict ={
        'Autoppsy of jane doe': 02.20,
        'matrix':2.40,
        'ghost in a shell':1.90,
        'jon wick':2.51,
        'batman':3.40 
    }
    return render_template('table_data.html',
                           movies=movies_dict,
                           name='Sally')


@app.route('/filters')
def filter_data():
    movies_dict ={
        'Autoppsy of jane doe': 02.20,
        'matrix':2.40,
        'ghost in a shell':1.90,
        'jon wick':2.51,
        'batman':3.40 
    }

    return render_template('filter_data.html',
                           movies=movies_dict,
                           name=None,
                           file='a christmad carol')



@app.route('/macros')
def jinja_macros():
    movies_dict ={
        'Autoppsy of jane doe': 02.20,
        'matrix':2.40,
        'ghost in a shell':1.90,
        'jon wick':2.51,
        'batman':3.40}
      
    return render_template('using_macros.html' , movies=movies_dict)

if __name__ == '__main__':

    app.run(debug=True)
    