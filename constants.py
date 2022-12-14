from decouple import config

AZURE_IMAGE_DESCRIBE_URL = config('AZURE_IMAGE_DESCRIBE_URL')
AZURE_IMAGE_DETECT_URL = config('AZURE_IMAGE_DETECT_URL')
AZURE_READ_TEXT_URL = config('AZURE_READ_TEXT_URL')
SUBSCRIPTION_KEY = config('SUBSCRIPTION_KEY')
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'