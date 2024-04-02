#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

@app.route("/")
def main():
    return '''
     <h2>This is a simple leap year calculator. Enter a year to find out if it's a leap year :)</h2>
     <form action="/check_leap_year" method="POST">
         Enter a year: <input name="year" type="number">
         <input type="submit" value="Check">
     </form>
     '''

@app.route("/check_leap_year", methods=["POST"])
def check_leap_year():
    try:
        year = int(request.form.get("year", ""))
        if is_leap_year(year):
            return f"{year} is a leap year."
        else:
            return f"{year} is not a leap year."
    except ValueError:
        return "Please enter a valid year."

if __name__ == "__main__":
    app.run(debug=True)
