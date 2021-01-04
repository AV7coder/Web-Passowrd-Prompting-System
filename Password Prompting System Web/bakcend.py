from flask import Flask, redirect, url_for, request ,render_template
app = Flask(__name__) 
  
@app.route('/success/<name>') 
def success(name): 
   return '%s' % name 
def fail(name):
   return name 
@app.route('/login',methods = ['POST', 'GET']) 
def login(): 
   if request.method == 'POST': 
      user = request.form['name']
      password = request.form['password']
      if user == "AV7coder" and password =="hello":
         return redirect(url_for('success',name = "Welcome "+user))
      else:
         return redirect(url_for('success',name = "Inavlid data")) 
  

   else: 
      user = request.args.get('name') 
      return redirect(url_for('success',name = "Inavlid data")) 
  
if __name__ == '__main__': 
   app.run(debug = True) 
