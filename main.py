from flask import Flask, request , render_template

app = Flask(__name__)


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





if __name__ == '__main__':
    app.run(debug=True)
    