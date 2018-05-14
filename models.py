import os.path

from azure.cognitiveservices.vision.computervision import ComputerVisionAPI

SUBSCRIPTION_KEY_ENV_NAME = "3af0e70b4f3641689f254019214efeda"
COMPUTERVISION_LOCATION = os.environ.get("COMPUTERVISION_LOCATION", "westcentralus")

