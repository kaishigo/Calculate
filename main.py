from flask import Flask, render_template, request

app = Flask(__name__, static_folder="templates")


@app.route("/calculate")
def index():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def sum_dollars():
    value_monthly_salary = request.form["value_monthly_salary"]
    working_days_month = request.form["working_days_month"]
    days_worked = request.form["days_worked"]

    try:
        sum_1 = int(value_monthly_salary) / int(working_days_month) * int(days_worked)
        sum_2 = sum_1 * 0.13
        sum_ = sum_1 - sum_2
        return render_template("index.html", dollars=f"{'%.2f' % sum_}руб", text_wrap=f"Ваша зп после НДФЛ")
    except ValueError:
        return render_template("index.html")


app.run(port=200)
