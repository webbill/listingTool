import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '28_(poj9@hd%%rj(cvorc2264gu1ye&=oj5#po^to5e38i-c0g'
# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


#STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, 'listingtool',STATIC_URL.replace("/", ""))

STATICFILES_DIRS = (
    MEDIA_ROOT,
)

BeforeRangeNum = 9
AfterRangeNum = 11

#from listingtool.ebayPythonApi import *
#from listingtool.initSys import *

