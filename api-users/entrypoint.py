import os
from app import create_app
settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)

port = int(os.environ.get("PORT", 4000))
app.run(host='0.0.0.0', port=port)