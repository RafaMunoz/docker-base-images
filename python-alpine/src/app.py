import signal
import sys
from fastapi import FastAPI

app = FastAPI()

def handle_sigterm(signum, frame):
    print("Received SIGTERM, shutting down...")
    sys.exit(0)

# Registra el manejador de señales
signal.signal(signal.SIGTERM, handle_sigterm)

@app.get("/")
def read_root():
    return {"Hello": "World"}

