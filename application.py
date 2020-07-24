import requests
from flask import Flask, render_template, request
from pprint import pprint 
import os, uuid, sys
from azure.storage.blob import BlobClient


# Instantiate a new ContainerClient


app = Flask(__name__)

#
#  set some variables
#. local path is the directory int the app directory
#. connection_string is from the storage account
#. container_name is the upload destinarion container 
#. in the storage account
#
local_path="upload"
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = "upload"
#
#  set the region to use and the url/resource_path for the API nethond
#
region = 'westcentralus' #Here you enter the region of your subscription
url = 'https://{}.api.cognitive.microsoft.com/vision/v1.0/analyze'.format(region)
key = "4287cca65e4446d0a360841265095710"
pic = "static/img/person.jpg"

#storage_account = 'inststorageaccount'
#account_key =  'EdUwI34WmY0zlbmYXlvoG6+wqAsJ68j/b6sSpb8EIOIAl/2Bh3g4VTgJzI5PZTzksg0iScymQeAURiefv94MsA=='



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

  maxNumRetries = 1

  pathToFileInDisk = pic
  with open( pathToFileInDisk, 'rb' ) as f:
    data = f.read()

# Computer Vision parameters
  params = { 'visualFeatures' : 'categories,tags,description,faces'}

# Computer Vision header fields
  headers = dict()
  headers['Ocp-Apim-Subscription-Key'] = key
  headers['Content-Type'] = 'application/octet-stream'

  json = true 
  response = requests.request( 'post', url, json = json, data = data, headers = headers, params = params )

  vreq = response.url 
  vresp = response.text

  return render_template("vision.html", url=vreq, result=vresp, pic=pic)
  
@app.route('/selcvfile')
def selcvfile():
  return render_template("selcvfile.html") 
  
@app.route("/upload", methods = {'GET', 'POST'})
def upload():
  
  if request.method == 'POST':
     
     req_file = request.files['file']
     print("in POST , filename is " + req_file.filename)
     local_file_name = req_file.filename
     req_file.save(os.path.join(local_path, local_file_name))
     upfile = os.path.join(local_path, local_file_name)
     print("Path " + os.path.join(local_path, local_file_name))
     print("upfile " + upfile)
     blob_client = BlobClient.from_connection_string(conn_str=connection_string, container_name=container_name, blob_name=local_file_name)
     with open(upfile, "rb") as data:
                blob_client.upload_blob(data, blob_type="BlockBlob")

     os.remove(os.path.join(local_path, local_file_name))
 
  return render_template("upload.html", file=local_file_name, container=container_name)
  
@app.route('/listcont')
def listcont():

  block_blob_service = BlockBlobService(account_name=storage_account, account_key=account_key)
  list = block_blob_service.list_blobs(container_name)
  return render_template("listcont.html",container=container_name,list=list,account=storage_account)   

if __name__ == '__main__':
  app.run()
