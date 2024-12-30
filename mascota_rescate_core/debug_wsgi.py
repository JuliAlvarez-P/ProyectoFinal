import os
import sys
from pathlib import Path

# Get the project root directory
BASE_DIR = Path(__file__).resolve().parent

# Add the project directory to the Python path
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mascota_rescate_core.settings')

try:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    print("WSGI application loaded successfully!")
except Exception as e:
    print(f"Error loading WSGI application: {e}")
    print("\nPython path:")
    for path in sys.path:
        print(f"  - {path}")
    print("\nEnvironment variables:")
    for key, value in os.environ.items():
        if 'DJANGO' in key or 'PYTHON' in key:
            print(f"  - {key}: {value}")
