import requests
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html") 

@app.route("/about")
def about():
  req = requests.get('https://github.com/timeline.json')
  treq = req.url 
  resp = req.json()
  return render_template("about.html", url=treq, result=resp)

@app.route("/vision")
def vision():

  region = 'westcentralus' #Here you enter the region of your subscription
  url = 'https://{}.api.cognitive.microsoft.com/vision/v1.0/analyze'.format(region)
  key = "3b290a5c45cf4f76aa61e5fb77347a07"
  maxNumRetries = 1

#  vreq = req.url 
#  vresp = req.json()
  vreq = "test.url"
  vresp = "{test response}"
  return render_template("vision.html", url=vreq, result=vresp)

if __name__ == '__main__':
  app.run()
