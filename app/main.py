from flask import Flask, jsonify, request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
from functools import wraps

app = Flask(__name__)


#  MÉTRICAS PROMETHEUS


# Contador de todas las peticiones HTTP
REQUEST_COUNT = Counter(
    "inventory_http_requests_total",
    "Total de peticiones HTTP a la API de inventario",
    ["method", "endpoint", "http_status"]
)

# Histograma de duración de las peticiones
REQUEST_LATENCY = Histogram(
    "inventory_request_duration_seconds",
    "Duración de las peticiones HTTP en segundos",
    ["endpoint"]
)

# Datos de del inventario
ITEMS = [
    {"id": 1, "name": "Absolute Batman", "stock": 5},
    {"id": 2, "name": "Absolute Wonder Woman", "stock": 7},
    {"id": 3, "name": "Absolute Absolute Superman", "stock": 4},
    {"id": 4, "name": "Absolute Flash", "stock": 6},
    {"id": 5, "name": "Absolute Green Lanter", "stock": 9},
]


def track_metrics(endpoint: str):
    """
    Decorador para medir la duración de la petición
    y aumentar los contadores de métricas.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            try:
                # Ejecuta la función de la ruta
                response = func(*args, **kwargs)

                status_code = 200
                if isinstance(response, tuple):
                    if len(response) >= 2:
                        status_code = response[1]
                else:
                    status_code = 200

                return response

            except Exception:
                duration = time.time() - start
                REQUEST_LATENCY.labels(endpoint=endpoint).observe(duration)
                REQUEST_COUNT.labels(
                    method=request.method,
                    endpoint=endpoint,
                    http_status=500
                ).inc()
                # Volvemos a lanzar la excepción para que Flask la maneje
                raise

            finally:
                # Si no hubo excepción, se mide aquí
                duration = time.time() - start
                if request:
                    # Solo registramos si hay request activo
                    REQUEST_LATENCY.labels(endpoint=endpoint).observe(duration)
                    pass

        return wrapper
    return decorator


#        RUTAS API

@app.route("/")
@track_metrics(endpoint="/")
def home():
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint="/",
        http_status=200
    ).inc()
    return jsonify({"message": "Inventory API con métricas Prometheus"}), 200


@app.route("/items")
@track_metrics(endpoint="/items")
def get_items():
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint="/items",
        http_status=200
    ).inc()
    return jsonify(ITEMS), 200


@app.route("/health")
@track_metrics(endpoint="/health")
def health():
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint="/health",
        http_status=200
    ).inc()
    return jsonify({"status": "ok"}), 200


@app.route("/fail")
@track_metrics(endpoint="/fail")
def fail():
    # Endpoint que siempre responde 500 a propósito
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint="/fail",
        http_status=500
    ).inc()
    return jsonify({"error": "Fallo intencional para pruebas de alerta"}), 500



#     ENDPOINT MÉTRICAS

@app.route("/metrics")
def metrics():
    """
    Endpoint estándar para Prometheus.
    Aquí se exponen todas las métricas en formato de texto.
    """
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}


if __name__ == "__main__":
    # Modo desarrollo local (no para producción)
    app.run(host="0.0.0.0", port=8000, debug=True)

