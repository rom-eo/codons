from flask import Flask, render_template, request
import sys
from io import StringIO
import contextlib


app = Flask(__name__)

@app.route('/')
def hello_world():
   html = '''<h1> Notre titre</h1> Salut'''
   return html

@app.route('/problem/<number>')
def probleme(number): 
   return render_template('problem'+number+'.html', name = number)

 

@app.route('/valider', methods=['POST'])
def val():
   d= request.form
   myglobal = None
   code = d['code']
   try:
       exec(code+ "\nassert factorial(3) == 4: 'Faux'")
       return 'Good'
       pass
   except:
       return 'BAD!'
        

   return str(s.getvalue())#'good'#str(myglobal[factorial](3))

#render_template('problem'+number+'.html', name = number)

if __name__ == '__main__':
   app.run()

 
