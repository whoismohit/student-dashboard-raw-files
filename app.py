from flask import Flask, render_template, request, redirect, url_for, session, flash
import db

app = Flask(__name__)
app.secret_key = "supersecretkey"


@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = db.validate_user(username, password)
        if user:
            session["username"] = username
            flash("Login successful!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid credentials, try again.", "danger")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))


@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))

    students = db.get_students()
    return render_template("dashboard.html", students=students)


@app.route("/add", methods=["POST"])
def add_student():
    if "username" not in session:
        return redirect(url_for("login"))

    name = request.form["name"]
    email = request.form["email"]
    course = request.form["course"]

    db.add_student(name, email, course)
    flash("Student added successfully!", "success")
    return redirect(url_for("dashboard"))


@app.route("/update/<int:id>", methods=["POST"])
def update_student(id):
    if "username" not in session:
        return redirect(url_for("login"))

    name = request.form["name"]
    email = request.form["email"]
    course = request.form["course"]

    db.update_student(id, name, email, course)
    flash("Student updated successfully!", "success")
    return redirect(url_for("dashboard"))


@app.route("/delete/<int:id>")
def delete_student(id):
    if "username" not in session:
        return redirect(url_for("login"))

    db.delete_student(id)
    flash("Student deleted successfully!", "danger")
    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    db.init_db()
    app.run(debug=True)
