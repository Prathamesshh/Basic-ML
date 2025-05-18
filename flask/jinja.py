from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

@app.route('/success/<int:score>')
def success(score):
    return "The marks you got is " + str(score)


if __name__ == "__main__":
    app.run(debug=True)