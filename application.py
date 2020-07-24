import requests
from flask import Flask, render_template, request
from pprint import pprint 
import os, uuid, sys
from azure.storage.blob import BlobClient
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials


# Instantiate a new ContainerClient


app = Flask(__name__)

#
#  set some variables
#
local_path="upload"
container = "upload"
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
computervision_key = os.getenv("COMPUTERVISION_SUBSCRIPTION_KEY")
COMPUTERVISION_LOCATION = os.environ.get("COMPUTERVISION_LOCATION", "eastus")

#  set the region to use and the url/resource_path for the API nethond
#


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

  print("in vision , filename is " + current_file)
 

#  with open()
# Computer Vision parameters
  params = { 'visualFeatures' : 'categories,brands,description,objects,faces'}

# Computer Vision header fields

 

  return render_template("vision.html", url=endpoint, result=curent_file, pic=local_file_name)
  
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
     blob_client = BlobClient.from_connection_string(conn_str=connection_string, container_name="upload", blob_name=local_file_name)
     with open(upfile, "rb") as data:
                blob_client.upload_blob(data, blob_type="BlockBlob")

# Now we send it of for analysis
     credentials = CognitiveServicesCredentials(computervision_key)
     computervision_endpoint = "https://eastus.api.cognitive.microsoft.com"
     client = ComputerVisionClient( endpoint=computervision_endpoint,credentials=credentials)
     print("endpoint " + computervision_endpoint)

 #    results = client.describe_image("https://homepages.cae.wisc.edu/~ece533/images/zelda.png")

#     with open("upload/cut.jpg", "rb") as image_stream:
#         image_analysis = client.analyze_image_in_stream(
#            image=image_stream,
#            visual_features=[
#                VisualFeatureTypes.image_type,  # Could use simple str "ImageType"
#                VisualFeatureTypes.faces,      # Could use simple str "Faces"
#                VisualFeatureTypes.categories,  # Could use simple str "Categories"
#                VisualFeatureTypes.color,      # Could use simple str "Color"
#                VisualFeatureTypes.tags,       # Could use simple str "Tags"
#                VisualFeatureTypes.description  # Could use simple str "Description"
#            ]
#         )
    
     os.remove(os.path.join(local_path, local_file_name))
 
  return render_template("upload.html",file=local_file_name, container=container)
  
@app.route('/listcont')
def listcont():

  block_blob_service = BlockBlobService(account_name=storage_account, account_key=account_key)
  list = block_blob_service.list_blobs(container_name)
  return render_template("listcont.html",container=container_name,list=list,account=storage_account)   

if __name__ == '__main__':
  app.run()
