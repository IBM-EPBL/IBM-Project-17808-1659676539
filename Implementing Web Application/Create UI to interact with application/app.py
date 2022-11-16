from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    login_page = True
    print(request.values.get('page'))
    if request.values.get('page') == "register":
        login_page = False
    return render_template('index.html', login=login_page)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form
        print(user)
        if user["email"] == "hello":
            return redirect(url_for('tracker'))
        else:
            return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        user = request.form
        print(user)
        if user["email"] == "hello":
            return redirect(url_for('tracker'))
        else:
            return redirect(url_for('home', page="register"))


@app.route('/tracker')
def tracker():
    return render_template('home.html')


@app.route('/add-expenditure', methods=['GET', 'POST'])
def add_expenditure():
    if request.method == "POST":
        details = request.form
        print(details)
        return redirect(url_for('tracker'))


if __name__ == '__main__':
    app.run(debug=True)