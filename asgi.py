import os
import django
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'A2SL.settings')
django.setup()  # Optional, if you are using Django's models directly

application = get_asgi_application()
