from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    print("*"*80)
    print("in index function")
    return render_template('index.html', phrase="hello", times=5 )

@app.route('/play')
def play():
    print("*"*80)
    print("In play function")
    return render_template('play.html', times=3, color="lightblue")

@app.route('/play/<num>')
def play2(num):
    print("*"*80)
    print("In play 2 function")
    return render_template('play.html', times=int(num), color="lightblue")

@app.route('/play/<num>/<color>')
def play3(num, color):
    print("*"*80)
    print("In play 3 function")
    return render_template('play.html', times=int(num), color=color)




@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say(name):
    return f'Hi (name)!'

@app.route('/repeat/<num>/<name>')
def repeat(num, name):
    return f'{name} ' * int(num)

if __name__=='__main__':
    app.run(debug=True)