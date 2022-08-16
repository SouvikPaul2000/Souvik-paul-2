from flask import Flask

app = Flask(__name__)

'''@app.route("/")
def hello_world():
    return render_template('index.html')'''

@app.route("/")
def hello_world():
    return "Hello"
    
@app.route("/<string:n>")
def Pal(n):
        l=n[::-1]
        if n==l:
            return "Yes its a palindrome"
        
           
        else:
            return "No its not a palindrome"

if __name__== "__main__":
    app.run(debug=True)