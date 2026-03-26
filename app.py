from flask import Flask, render_template, request, redirect
import sqlite3
import socket

app = Flask(__name__)

def get_db():
    return sqlite3.connect("database/voting.db")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        name = request.form["name"]
        age = int(request.form["age"])
        email = request.form["email"]
        phone = request.form["phone"]

        if age < 18:
            return "You must be 18 or older to vote."

        return redirect(f"/vote?phone={phone}")

    return render_template("login.html")


@app.route("/vote", methods=["GET","POST"])
def vote():

    phone = request.args.get("phone")

    conn = get_db()
    cursor = conn.cursor()

    if request.method == "POST":

        candidate_id = request.form["candidate"]
        phone = request.form.get("phone")

        cursor.execute("SELECT * FROM voters WHERE phone=?", (phone,))
        existing = cursor.fetchone()

        if existing:
            return "You have already voted."

        cursor.execute(
            "UPDATE candidates SET votes = votes + 1 WHERE id=?",
            (candidate_id,)
        )

        cursor.execute(
            "INSERT INTO voters(phone) VALUES(?)",
            (phone,)
        )

        conn.commit()
        conn.close()

        return redirect("/results")

    cursor.execute("SELECT * FROM candidates")
    candidates = cursor.fetchall()

    conn.close()

    return render_template("vote.html", candidates=candidates, phone=phone)


@app.route("/results")
def results():

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM candidates")
    candidates = cursor.fetchall()

    conn.close()

    return render_template("results.html", candidates=candidates)


@app.route("/admin")
def admin():

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM candidates")
    candidates = cursor.fetchall()

    conn.close()

    return render_template("admin.html", candidates=candidates)


@app.route("/reset")
def reset_votes():

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("UPDATE candidates SET votes = 0")
    cursor.execute("DELETE FROM voters")

    conn.commit()
    conn.close()

    return redirect("/admin")


if __name__ == "__main__":

    # Get local IP address
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    print("\nServer running on:")
    print(f"http://127.0.0.1:5000")
    print(f"http://{local_ip}:5000  (Use this on other devices)\n")

    app.run(host="0.0.0.0", port=5000, debug=True)