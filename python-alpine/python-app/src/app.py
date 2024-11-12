import signal
import sys
import time

def handle_sigterm(signum, frame):
    print("Received SIGTERM, shutting down...")
    sys.exit(0)

# Registra el manejador de señales
signal.signal(signal.SIGTERM, handle_sigterm)

while True:
    print("Hello World!!")
    time.sleep(5)