from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/scrape_mars"
mongo = PyMongo(app)

data={}

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

# Set route
@app.route('/')
def index():
    # Store the database in a list
    mars = mongo.db.mars.find_one()


    # Return the template with the teams list passed in
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scraper():
    db.dropdatabase()    
    mars = mongo.db.mars
    data = scrape_mars.scrape()
    mars.update({}, data, upsert=True)
   
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)