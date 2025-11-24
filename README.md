# Proyecto Final SRE Bootcamp
**Autor:** Anthony Richard Callow Monge / **Correo:** anthony.callow@outlook.com

Este proyecto implementa un sistema completo de observabilidad, métricas, alertas y automatización, utilizando:

- Python + Flask
- Docker
- Kubernetes (Minikube)
- Prometheus (via kube-prometheus-stack)
- Grafana
- Alertmanager
- Automatización completa con Ansible


## Tabla de Contenido

- [Descripción](#1-descripción)
- [Arquitectura](#2-arquitectura)
- [Estructura del proyecto](#3-estructura)
- [Requisitos previos](#4-requisitos-previos)
- [Build y despliegue automático con Ansible](#5-build-y-despliegue-automático-con-ansible)
- [Build y despliegue manual](#6-build-y-despliegue-manual)
- [Acceder a los servicios](#7-acceder-a-los-servicios)
  - [API](#api)
  - [Prometheus](prometheus)
  - [Grafana](grafana)
  - [Alertmanager](alertmanager)
- [Pruebas de alertas](#9-pruebas-de-alertas)
- [Evidencia del proyecto](#10-evidencia-del-proyecto)


##  1. Descripción

La Inventory Metrics API es una aplicación sencilla escrita en Flask que expone endpoints básicos y métricas personalizadas compatibles con Prometheus.

### Metricas expuestas

| Endpoint   | Descripción                       |
| ---------- | --------------------------------- |
| `/`        | Mensaje de bienvenida             |
| `/items`   | Lista de productos                |
| `/health`  | Healthcheck                       |
| `/fail`    | Genera errores 500                |
| `/metrics` | Exposición de métricas Prometheus |

##  2. Arquitectura
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

## 3. Estructura
```bash
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
```


##  4. Requisitos Previos

Antes de ejecutar el proyecto es obligatorio tener:

- Docker Desktop instalado en Windows con soporte WSL2
- Todo lo demás (kubectl, helm, minikube, dependencias apt) será instalado automáticamente por Ansible.

## 5. Build y Despliegue automático con Ansible

El proyecto incluye un playbook que:

- Instala herramientas necesarias
- Inicia Minikube
- Construye imagen Docker
- Carga imagen en Minikube
- Aplica manifiestos Kubernetes
- Instala kube-prometheus-stack
- Aplica ServiceMonitor y alertas
- Muestra estado final del cluster

### Ubicación de los archivos:

```bash
ansible/
├─ inventory.ini
└─ deploy.yml
```


### Pasos para ejecutar el playbook

Ejecute en WSL2:

```bash
cd ~/inventory-metrics-sre
ansible-playbook -i ansible/inventory.ini ansible/deploy.yml --ask-become-pass

```

Si todo funciona correctamente, se verá:

```bash
PLAY RECAP
localhost : ok=21   changed=11   failed=0

```

##  6. Build y Despliegue Manual 

En caso de que querer ejecutar el proyecto manualmente, ejecute los siguientes comandos:


- Build: 
```bash
docker build -t inventory-metrics-api:latest .
minikube image load inventory-metrics-api:latest


```
- Despliegue:
```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/servicemonitor.yaml
kubectl apply -f k8s/alert-rules.yaml


```

##  7. Acceder a los Servicios

Una vez desplegueda la aplicación se pueden acceder los siguientes servicios:

**- API**
```bash
kubectl port-forward -n inventory-monitoring svc/inventory-api 8000:8000

```

-  	http://localhost:8000
-	 http://localhost:8000/items
- 	http://localhost:8000/fail
-	 http://localhost:8000/metrics

**- Prometheus**
```bash
kubectl port-forward -n monitoring svc/prometheus-stack-kube-prom-prometheus 9090:9090

```
Visita: http://localhost:9090

**- Grafana**
```bash
kubectl port-forward -n monitoring svc/prometheus-stack-grafana 3000:80


```
Visita: http://localhost:3000

Usuario: admin
Contraseña:

```bash
kubectl get secret -n monitoring prometheus-stack-grafana \
  -o jsonpath="{.data.admin-password}" | base64 --decode && echo
```

Importa el dashboard desde:

```bash
monitoring/grafana-dashboard.json

```

**- Alertmanager**
```bash
kubectl port-forward -n monitoring svc/prometheus-stack-kube-prom-alertmanager 9093:9093


```

http://localhost:9093

## 9. Pruebas de Alertas

Generar errores 500:

```bash
for i in {1..30}; do curl -s http://localhost:8000/fail; done


```

Luego:

Prometheus → Alerts

Alertmanager → muestra alerta activa



##  10. Evidencia del Proyecto
<img width="921" height="623" alt="image" src="https://github.com/user-attachments/assets/06a483a7-7d72-4d4f-aec0-4ccb321bac8b" />

<img width="921" height="900" alt="image" src="https://github.com/user-attachments/assets/5c12531f-4224-4afc-be25-2d02bc2a8c9e" />

<img width="921" height="205" alt="image" src="https://github.com/user-attachments/assets/51049df2-c05b-4abb-aacc-6eb08617f7af" />

<img width="921" height="174" alt="image" src="https://github.com/user-attachments/assets/ece35e05-7beb-4406-874e-b97c901a14bb" />

<img width="921" height="888" alt="image" src="https://github.com/user-attachments/assets/5fbc259a-4e56-409f-973b-da3c56394d5d" />

<img width="921" height="191" alt="image" src="https://github.com/user-attachments/assets/bfd30315-e9e2-4b44-b7e1-b3eaf5fae01b" />

<img width="921" height="505" alt="image" src="https://github.com/user-attachments/assets/de0ea6e2-92fb-4a12-bcd3-97d9e8bf759f" />

<img width="921" height="991" alt="image" src="https://github.com/user-attachments/assets/60025f73-fba6-4d3e-9ba6-19424d72a207" />

<img width="921" height="549" alt="image" src="https://github.com/user-attachments/assets/542e50af-b56f-4a6b-bff7-874f73c844da" />

<img width="921" height="250" alt="image" src="https://github.com/user-attachments/assets/2d0bd507-779d-4702-9014-cf13b0efe767" />



