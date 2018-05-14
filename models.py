import os.path

from azure.cognitiveservices.vision.computervision import ComputerVisionAPI

SUBSCRIPTION_KEY_ENV_NAME = "tisss"
COMPUTERVISION_LOCATION = os.environ.get("COMPUTERVISION_LOCATION", "westcentralus")

