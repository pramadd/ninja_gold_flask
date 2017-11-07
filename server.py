from flask import Flask, render_template, request, redirect, session
import random, datetime
from time import gmtime, strftime

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def defaultPage():
    print "At the index page"
    if 'gold' not in session:
        print "gold was not in session"
        session['gold'] = 0
    if 'activities' not in session:
        print "activities was not in session"
        session['activities'] = []
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    print "What's in session?", session
    location = request.form['building']
    time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    if location == 'farm':
        goldcoins = random.randrange(10, 21) 
        info = {'money':goldcoins, 'place':location, "time": time}
    elif location == 'cave':
        goldcoins = random.randrange(5,11)
        info = {'money':goldcoins, 'place':location, "time": time}
    elif location == 'house':
        goldcoins = random.randrange(2,6)
        info = {'money':goldcoins, 'place':location, "time": time}
    elif location == 'casino':
        goldcoins = random.randrange(-50,51)
        info = {'money':goldcoins, 'place':location, "time": time}
     
    
    if goldcoins >= 0:
        activity = "Earned {} from the {}! {} ".format(goldcoins,location,time)
       
    else: 
        activity = "Entered a {} and lost {} gold ... Ouch! {}".format(location,-1 * goldcoins,time)    
    session['activities'].append(activity)
    session['gold'] += goldcoins     
    return redirect('/')

app.run(debug=True)