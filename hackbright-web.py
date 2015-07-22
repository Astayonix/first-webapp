from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github)
    return html

@app.route("/make_new_student", methods=["GET","POST"])
def make_new_student():
    """Add a new student and print confirmation.

    Given a first name, last name, and GitHub account, add student to the
    database and print a confirmation message.
    """
    render_template("make_new_student.html")
    first_name = request.form.get('f')
    last_name = request.form.get('l')
    github = request.form.get('g')
    hackbright.make_new_student(first_name, last_name, github)
    return render_template("make_new_student.html")

@app.route('/confirmation', methods=["POST"])
def confirm_entry():
    first_name = request.form.get('f')
    last_name = request.form.get('l')
    return render_template("confirmation.html", first_name=first_name, last_name=last_name)

@app.route("/student_search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

if __name__ == "__main__":
    app.run(debug=True)