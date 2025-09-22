from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3, hashlib

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for sessions

# ---------- DATABASE SETUP ----------
def init_db():
    conn = sqlite3.connect("fundsweb.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

# ---------- ROUTES ----------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    email = request.form["email"]
    password = hashlib.sha256(request.form["password"].encode()).hexdigest()  # hash password

    conn = sqlite3.connect("fundsweb.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        conn.commit()
        flash("User registered successfully! Please login.")
    except sqlite3.IntegrityError:
        flash("Email already exists!")
    conn.close()
    return redirect(url_for("home"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = hashlib.sha256(request.form["password"].encode()).hexdigest()

        conn = sqlite3.connect("fundsweb.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        user = c.fetchone()
        conn.close()

        if user:
            session["user_id"] = user[0]
            session["user_name"] = user[1]
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid credentials!")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user_id" in session:
        return render_template("dashboard.html", user_name=session["user_name"])
    else:
        flash("Please login first.")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for("home"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
