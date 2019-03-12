from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "You've reached the home page. Congrats!"

@app.route('/about')
def about():
    return "Welcome to the About page! Here you'll learn more about our mission."

if __name__=="__main__":
    app.run(debug=True)