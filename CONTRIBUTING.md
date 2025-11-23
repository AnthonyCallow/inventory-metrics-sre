 **Guía de Contribución — Inventory Metrics API (SRE Bootcamp)**

¡Gracias por tu interés en contribuir!  
Este repositorio es parte del proceso de formación del **SRE Bootcamp**, y busca servir como recurso práctico para aprender sobre observabilidad, métricas, automatización y despliegue de aplicaciones en Kubernetes.  
Tus aportes —ya sean ideas, correcciones o mejoras— pueden ayudar a otros estudiantes a aprender más efectivamente.

---

#  **Cómo Contribuir**

## 1. **Haz un Fork del Repositorio**

Utiliza la interfaz de GitHub para crear una copia del proyecto en tu propio perfil.

---

## 2. **Crea una Rama de Trabajo**

Usa un nombre descriptivo para tu rama.  
Ejemplos:

`git checkout -b fix-servicemonitor-labels git checkout -b update-dashboard-metrics git checkout -b improve-ansible-playbook`

---

## 3. **Realiza tus Cambios**

Al hacer tus aportes, por favor:

- Sigue la estructura de carpetas existente (`app/`, `k8s/`, `ansible/`, etc.).
  
- Escribe documentación clara y comentarios de código cuando sea necesario.
  
- Mantén consistencia en formato, estilo y convenciones del proyecto.
  
- Si tu cambio afecta Kubernetes, Ansible o métricas, **prueba el despliegue en Minikube** antes de enviar tu PR.
  
- Si realizas cambios en dashboards, asegúrate de que los paneles muestren datos reales.
  
- No incluyas archivos generados automáticamente ni secretos.
  

---

## 4. **Haz Commit y Push de tus Cambios**

Ejemplo:

`git add . git commit -m "Fix: actualizar labels del ServiceMonitor para Prometheus Operator" git push origin fix-servicemonitor-labels`

---

## 5. **Abre un Pull Request (PR)**

En tu PR:

- Usa un título claro y profesional.
  
- Escribe un resumen breve y directo explicando tu cambio.
  
- Si aplica, referencia issues relacionados.
  
- Explica los pasos para reproducir el cambio (si afecta comportamiento).
  
- Especifica si el PR afecta documentación, comportamiento, métricas o infraestructura.
  

---

#  **Guías y Buenas Prácticas**

###  Escribir en español claro y profesional

(inglés también es aceptado si el contexto lo requiere).

###  Evitar emojis en documentación técnica

(a menos que el contexto sea educativo o motivacional).

###  Asegurar que los ejercicios sean reproducibles

Evita dependencias externas no documentadas.

###  Para Kubernetes y Ansible:

- Mantén indentación de 2 espacios en YAML.
  
- Usa nombres de recursos consistentes con el estándar del proyecto.
  
- No incluyas secretos ni credenciales.
  

###  Si tu cambio despliega recursos persistentes (pods, PVs, namespaces, etc.):

Incluye una sección **“Cleanup”** indicando cómo eliminar los recursos.

Ejemplo:

`kubectl delete ns inventory-monitoring`

---

#  **Revisión de Pull Requests**

Todos los PR serán revisados para garantizar:

- Calidad técnica
  
- Claridad en la documentación
  
- Consistencia con el resto del proyecto
  
- Buenas prácticas SRE y DevOps
  

Se pueden solicitar cambios antes de hacer merge.

---

#  **Gracias por Contribuir**

Tu participación ayuda a mejorar este recurso educativo y fortalece el aprendizaje de otros estudiantes del SRE Bootcamp.  
¡Gracias nuevamente por aportar al proyecto!
