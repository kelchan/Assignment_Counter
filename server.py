from flask import Flask, render_template, request, redirect, session 
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes


count = 0


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def counter():
    print( request.form )
    global count
    count += 1
    return render_template( "index.html", count = count )

@app.route('/addTwo', methods = ['POST'])
def addTwo():
    print( "GLOBAL COUNT = ")
    global count
    count += 1
    print( count )
    return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
    global count
    count = 0
    print( count )
    return redirect('/')























if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.



