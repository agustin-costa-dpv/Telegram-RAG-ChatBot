# Importing module
# === SERVIDOR FALSO PARA RENDER ===
import os
from flask import Flask
from threading import Thread

app_flask = Flask('')

@app_flask.route('/')
def home():
    return "Bot de Auditoría funcionando correctamente."

def run():
    port = int(os.environ.get('PORT', 5000))
    app_flask.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()
# === FIN DEL SERVIDOR FALSO ===

from utils import logger
import core.setup as setup

log = logger.get_logger(__name__)

if __name__ == "__main__":
    # Iniciar servidor falso para Render
    keep_alive()
    
    # Starting the Bot
    log.info(f"Starting the bot...")
    app = setup.setup_bot()
    # Polling rate
    log.info(f"Polling...")
    app.run_polling(poll_interval=3)
