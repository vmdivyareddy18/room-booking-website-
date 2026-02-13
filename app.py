from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret123"

# Demo Data (Temporary Database)
users = []
rooms = [
    {"id": 1, "no": "101", "price": 1500, "status": "Available"},
    {"id": 2, "no": "102", "price": 1000, "status": "Available"},
    {"id": 3, "no": "103", "price": 1200, "status": "Available"}
]

bookings = []


@app.route('/')
def home():
    if 'user' not in session:
        return redirect('/login')

    return render_template("home.html", rooms=rooms)


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        users.append({
            "name": request.form['name'],
            "email": request.form['email'],
            "password": request.form['password']
        })

        return redirect('/login')

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        for user in users:
            if user['email'] == request.form['email'] and user['password'] == request.form['password']:

                session['user'] = user['email']
                return redirect('/')

    return render_template("login.html")


@app.route('/book/<int:id>')
def book(id):

    for room in rooms:
        if room['id'] == id and room['status'] == "Available":

            room['status'] = "Booked"

            bookings.append({
                "user": session['user'],
                "room": id
            })

    return redirect('/')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


if __name__ == "__main__":
    app.run(debug=True)
