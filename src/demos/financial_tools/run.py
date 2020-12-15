import sys
from app import app

port = int(sys.argv[1])

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=port)