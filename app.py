from flask import Flask, render_template, request, redirect, session
import sqlite3, bcrypt, re, pyotp

app = Flask(__name__)
app.secret_key = "super-secret-key"

# ---------- DATABASE ----------
def get_db():
    return sqlite3.connect("database.db")

def init_db():
    db = get_db()
    cur = db.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password BLOB,
            otp_secret TEXT
        )
    """)
    db.commit()
    db.close()

init_db()

# ---------- PASSWORD RULE ----------
def strong_password(password):
    return (
        len(password) >= 8 and
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"[0-9]", password)
    )

# ---------- ROUTES ----------

@app.route("/", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"].encode()

        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT password, otp_secret FROM users WHERE username=?", (username,))
        user = cur.fetchone()
        db.close()

        if user and bcrypt.checkpw(password, user[0]):
            session["otp_user"] = username

            totp = pyotp.TOTP(user[1])
            otp = totp.now()

            # ✅ DEMO ONLY: store OTP in session
            session["demo_otp"] = otp

            return redirect("/otp")
        else:
            error = "Invalid username or password"

    return render_template("login.html", error=error)

@app.route("/otp", methods=["GET", "POST"])
@app.route("/otp", methods=["GET", "POST"])
@app.route("/otp", methods=["GET", "POST"])
def otp():
    error = None

    if "otp_user" not in session:
        return redirect("/")

    demo_otp = session.get("demo_otp")

    if request.method == "POST":
        entered_otp = request.form["otp"]
        username = session["otp_user"]

        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT otp_secret FROM users WHERE username=?", (username,))
        secret = cur.fetchone()[0]
        db.close()

        totp = pyotp.TOTP(secret)

        if totp.verify(entered_otp):
            # ✅ FIX: set logged-in user FIRST
            session["user"] = username

            # cleanup
            session.pop("otp_user", None)
            session.pop("demo_otp", None)

            print("✅ LOGIN SUCCESS, SESSION USER:", session["user"])  # DEBUG
            return redirect("/dashboard")
        else:
            error = "Invalid OTP"

    return render_template("otp.html", error=error, demo_otp=demo_otp)



@app.route("/dashboard")
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")
    return render_template("dashboard.html", user=session["user"])


@app.route("/register", methods=["GET", "POST"])
def register():
    error = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not strong_password(password):
            error = "Password must be 8+ chars with upper, lower & number"
        else:
            hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            otp_secret = pyotp.random_base32()

            try:
                db = get_db()
                cur = db.cursor()
                cur.execute(
                    "INSERT INTO users (username, password, otp_secret) VALUES (?, ?, ?)",
                    (username, hashed, otp_secret)
                )
                db.commit()
                db.close()
                return redirect("/")
            except:
                error = "Username already exists"

    return render_template("register.html", error=error)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
