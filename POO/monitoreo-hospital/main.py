import paho.mqtt.client as mqtt # pip install paho-mqtt
import time

# Configuración del broker
BROKER = "lica.ingenieria.uner.edu.ar"     # dirección del broker
PORT = 1883   
USERNAME = "estudiante"
PASSWORD = "fiuner"
TOPIC_ROOT = "appsestudiantes/monitoreohospital/"
# Lista de tópicos a suscribirse
TOPICS = [(TOPIC_ROOT + "quirófano/temperatura", 0)] #, ("salacirugia01/humedad", 0), ("salacirugia01/presion", 0)]

# --- Callbacks ---
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Conectado al broker")
        # Suscribirse a todos los tópicos definidos
        for topic, qos in TOPICS:
            client.subscribe(topic, qos)
            print(f"📡 Suscrito a: {topic} (QoS={qos})")
    else:
        print(f"❌ Error al conectar. Código: {rc}")

def on_message(client, userdata, msg):
    print(f"📥 Mensaje recibido en {msg.topic}: {msg.payload.decode('utf-8')}")

def on_disconnect(client, userdata, rc):
    print("⚠️ Desconectado del broker. Intentando reconectar...")
    reconnect(client)

def reconnect(client):
    """Reintenta reconectar con backoff exponencial"""
    delay = 1
    while True:
        try:
            client.reconnect()
            print("🔄 Reconectado al broker")
            return
        except Exception as e:
            print(f"⏳ Reintento en {delay}s - {e}")
            time.sleep(delay)
            delay = min(delay * 2, 60)  # máx 60 segundos


# --- Cliente MQTT ---
client = mqtt.Client()

client.username_pw_set(USERNAME, PASSWORD)

# Asignar callbacks
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

# Conectar y mantener loop
try:
    client.connect(BROKER, PORT, keepalive=60)
    client.loop_forever()
except KeyboardInterrupt:
    print("🛑 Programa detenido por el usuario")
