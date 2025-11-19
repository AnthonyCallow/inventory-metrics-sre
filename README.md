📦 Inventory Metrics API — Proyecto Final SRE Bootcamp

Este proyecto implementa un sistema completo de observabilidad, métricas, alertas y automatización, utilizando:

Python + Flask

Docker

Kubernetes (Minikube)

Prometheus (via kube-prometheus-stack)

Grafana

Alertmanager

Automatización completa con Ansible

📘 1. Descripción del Proyecto

La Inventory Metrics API es una aplicación sencilla escrita en Flask que expone endpoints básicos y métricas personalizadas compatibles con Prometheus.

Endpoints
Endpoint	Descripción
/	Mensaje de bienvenida
/items	Lista de productos
/health	Healthcheck
/fail	Genera errores 500
/metrics	Exposición de métricas Prometheus
Métricas expuestas

inventory_http_requests_total

inventory_request_duration_seconds_bucket

Histogramas y contadores de latencia

Métricas por método HTTP, endpoint y status code

🧩 2. Arquitectura
                ┌────────────────────┐
                │ Inventory API      │
                │  Flask + Metrics   │
                └─────────┬──────────┘
                          │ /metrics
                ┌─────────▼──────────┐
                │  ServiceMonitor    │
                │ (Prometheus Oper.) │
                └─────────┬──────────┘
                          │
                ┌─────────▼──────────┐
                │    Prometheus      │
                └─────────┬──────────┘
                          │
             ┌────────────▼────────────┐
             │        Grafana          │
             │ Dashboards de métricas │
             └────────────┬────────────┘
                          │
              ┌───────────▼────────────┐
              │     Alertmanager       │
              └─────────────────────────┘

⚙️ 3. Requisitos Previos

Solo es obligatorio:

Docker Desktop instalado en Windows con soporte WSL2

Todo lo demás (kubectl, helm, minikube, dependencias apt) será instalado automáticamente por Ansible.

🤖 4. Automatización con Ansible

El proyecto incluye un playbook que:

✔ Instala herramientas necesarias
✔ Inicia Minikube
✔ Construye imagen Docker
✔ Carga imagen en Minikube
✔ Aplica manifiestos Kubernetes
✔ Instala kube-prometheus-stack
✔ Aplica ServiceMonitor y alertas
✔ Muestra estado final del cluster

Estructura:
ansible/
 ├─ inventory.ini
 └─ deploy.yml

🚀 5. Despliegue Automático

Ejecuta en WSL2:

cd ~/inventory-metrics-sre
ansible-playbook -i ansible/inventory.ini ansible/deploy.yml --ask-become-pass


Si todo funciona correctamente, verás:

PLAY RECAP
localhost : ok=21   changed=11   failed=0

🐍 6. Build Manual (Opcional)
docker build -t inventory-metrics-api:latest .
minikube image load inventory-metrics-api:latest

☸️ 7. Despliegue Manual (Opcional)
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/servicemonitor.yaml
kubectl apply -f k8s/alert-rules.yaml

📡 8. Acceso a los Servicios
🔹 8.1 API
kubectl port-forward -n inventory-monitoring svc/inventory-api 8000:8000


http://localhost:8000

http://localhost:8000/items

http://localhost:8000/fail

http://localhost:8000/metrics

🔹 8.2 Prometheus
kubectl port-forward -n monitoring svc/prometheus-stack-kube-prom-prometheus 9090:9090


Visita:

👉 http://localhost:9090

🔹 8.3 Grafana
kubectl port-forward -n monitoring svc/prometheus-stack-grafana 3000:80


Visita:

👉 http://localhost:3000

Usuario: admin
Contraseña:

kubectl get secret -n monitoring prometheus-stack-grafana \
  -o jsonpath="{.data.admin-password}" | base64 --decode && echo


Importa el dashboard desde:

monitoring/grafana-dashboard.json

🔹 8.4 Alertmanager
kubectl port-forward -n monitoring svc/prometheus-stack-kube-prom-alertmanager 9093:9093


👉 http://localhost:9093

🧪 9. Pruebas de Alertas

Generar errores 500:

for i in {1..30}; do curl -s http://localhost:8000/fail; done


Luego:

Prometheus → Alerts

Alertmanager → muestra alerta activa

📁 10. Estructura del Proyecto
inventory-metrics-sre/
├── ansible/
│   ├── deploy.yml
│   └── inventory.ini
│
├── app/
│   ├── main.py
│   └── requirements.txt
│
├── k8s/
│   ├── namespace.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── servicemonitor.yaml
│   └── alert-rules.yaml
│
├── monitoring/
│   └── grafana-dashboard.json
│
├── docs/
│   └── img/
│
├── Dockerfile
├── LICENSE
├── .gitignore
└── README.md

📸 11. Evidencia del Proyecto

Guarda capturas en:

docs/img/


Se recomienda incluir:

Pods en Kubernetes

Targets en Prometheus

Dashboard en Grafana

Alertmanager activo

👤 12. Autor

Anthony Richard Callow Monge
Proyecto Final — SRE Bootcamp

📜 13. Licencia

MIT License — ver archivo LICENSE.


