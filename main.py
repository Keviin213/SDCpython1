import requests
from flask import Flask, render_template
from pprint import pprint 
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

#
#  set the region to use and the url/resource_path for the API nethond
#
#  set the subscription key from Azure Cognitive Services Resource Group
#
  region = 'westcentralus' #Here you enter the region of your subscription
  url = 'https://{}.api.cognitive.microsoft.com/vision/v1.0/analyze'.format(region)
  key = "bsbsbsbsbss"
#
#  picture that will be sent for processing
#  located in the img directory
#   under  static/img 
  pic = "static/img/people.jpg"
  maxNumRetries = 1

#
# read the file from local disc
#
  pathToFileInDisk = pic
  with open( pathToFileInDisk, 'rb' ) as f:
    data = f.read()

# Computer Vision parameters
  params = { 'visualFeatures' : 'categories,tags,description,faces'}

# Computer Vision header fields
  headers = dict()
  headers['Ocp-Apim-Subscription-Key'] = key
  headers['Content-Type'] = 'application/octet-stream'

  json = None
  response = requests.request( 'post', url, json = json, data = data, headers = headers, params = params )

  vreq = response.url 
  vresp = response.text

  return render_template("vision.html", url=vreq, result=vresp, pic=pic)

if __name__ == '__main__':
  app.run()
