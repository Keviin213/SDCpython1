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
  key = "bsbsbs"
  maxNumRetries = 1

  pathToFileInDisk = r'static/img/cut.jpg'
  with open( pathToFileInDisk, 'rb' ) as f:
    data = f.read()

# Computer Vision parameters
  params = { 'visualFeatures' : 'categories,tags,description,faces'}

  headers = dict()
  headers['Ocp-Apim-Subscription-Key'] = key
  headers['Content-Type'] = 'application/octet-stream'

  json = None
  response = requests.request( 'post', url, json = json, data = data, headers = headers, params = params )

  vreq = response.url 
  vresp = response.json()
#  vreq = "test.url"
#  vresp = "{test response}"
  return render_template("vision.html", url=vreq, result=vresp)

if __name__ == '__main__':
  app.run()
