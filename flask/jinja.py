'''
Flask Jinja2 Template Example
{{...}} expression to print output in html
{%...%} conditions , for loops
{#...#} this is for comments
'''

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
    res=""
    if score >= 50:
        res = "You have passed the exam."
    else:
        res = "You have failed the exam."
    return render_template('result.html', result=res)



if __name__ == "__main__":
    app.run(debug=True)