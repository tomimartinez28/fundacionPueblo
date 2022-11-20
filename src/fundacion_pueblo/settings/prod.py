from .base import *

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static"),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', 
        'NAME': 'd98p22rne2r3ib',
        'USER': 'nwcqrkzhlvenfq',
        'PASSWORD': 'db33e57799534ad7d3736d339783f7efada0baf7de882d8092dc00e23534a39b',
        'HOST': 'ec2-52-54-212-232.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}