
import os
from app.server import app

PORT = int(os.getenv('PORT', 5000))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
