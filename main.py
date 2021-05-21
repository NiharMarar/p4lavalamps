from flask import Flask, render_template, request, redirect

import smtplib



app = Flask(__name__)


@app.route('/')
def home_route():
    return render_template("home.html")
    #if not session.get('logged_in'):
        #return render_template('login.html')
    #else:
        #return render_template("home.html")


@app.route('/bfsort', methods=['POST'])
def bfsort_bp():
    return render_template("bfsort.html")

@app.route('/Noahbubble', methods=['POST'])
def Noahbubblesort():
    return render_template("Noahbubble.html")


@app.route('/email', methods=['POST'])
def email():
    email = request.form['email']
    email_text = 'Subject: {}\n\n{}'.format("United States Data",
                                            'United States Total Cases 24,983,892; Total Deaths 2,080,972; Current Active Cases 25,361,201 ')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login('wildcatsp4@gmail.com', 'MrMadman33')
    server.sendmail('wildcatsp4@gmail.com', email, email_text)
    server.close()
    print("email sent to:", email)
    return render_template("home.html")


@app.route('/BubbleSort', methods=['POST'])
def BubbleSort():
    return render_template("testing.html")


@app.route('/bubblesort', methods=['POST'])
def bubblesort():
    return render_template("bubblesort.html")

@app.route('/niharbb', methods=['POST'])
def niharbb():
    return render_template("niharbb.html")


@app.route('/easteregg', methods=['POST'])
def easteregg_bp():
    return render_template("easteregg.html")


@app.route('/healthydinners', methods=['POST'])
def base():
    return render_template("healthydinners.html")


@app.route('/healthylunches')
def datatable():
    lunches = [
        {
            "name": "Chicken Parmesian",
            "price": 10
        },

        {
            "name": "Chicken Stir Fry",
            "price": 15
        },
    ]

    if request.method == 'POST':
        lunches.append({
            "name": request.form["name"],
            "price": request.form["price"]
        })
    return render_template("healthylunches.html", lunches=lunches)


@app.route('/main')
def main():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, port='5000', host='127.0.0.1')
