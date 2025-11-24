# Cómo Contribuir

## 1. **Realice un Fork del Repositorio**

Utilice la interfaz de GitHub para crear una copia del proyecto en su propio perfil.

---

## 2. **Cree una Rama de Trabajo**

Asigne un nombre descriptivo.  
Ejemplos:

```bash
git checkout -b fix-servicemonitor-labels 
git checkout -b update-dashboard-metrics 
git checkout -b improve-ansible-playbook


```

---

## 3. **Realice Sus Cambios**

Por favor asegúrese de:

- Mantener la estructura existente (`app/`, `k8s/`, `ansible/`, etc.).
  
- Documentar y comentar el código cuando corresponda.
  
- Conservar el estilo y las convenciones establecidas.
  
- Probar despliegues en Minikube si su cambio afecta Kubernetes, Ansible o métricas.
  
- Validar que los dashboards muestren datos reales.
  
- No incluir archivos generados automáticamente ni información sensible.
  

---

## 4. **Haga Commit y Push**

Ejemplo:



```bash
git add .
git commit -m "Fix: actualizar labels del ServiceMonitor"
git push origin fix-servicemonitor-labels`


```
---

## 5. **Abra un Pull Request**

En su PR:

- Use un título claro y profesional.
  
- Incluya un breve resumen de los cambios.
  
- Referencie issues si aplica.
  
- Indique pasos de reproducción si modifica comportamiento.
  
- Señale si el PR afecta documentación, métricas o infraestructura.
  

---

# **Guías y Buenas Prácticas**

- Escriba en español claro y profesional (inglés si el contexto lo requiere).
  
- Evite emojis en documentación técnica.
  
- Asegure que los ejercicios y despliegues sean reproducibles.
  
- En Kubernetes y Ansible:
  
  - Utilice indentación de 2 espacios en YAML.
    
  - Mantenga nombres coherentes con el estándar del proyecto.
    
  - No incluya secretos ni credenciales.
    
- Si su cambio crea recursos persistentes, incluya una sección **Cleanup**.  
  Ejemplo:

```bash
  kubectl delete ns inventory-monitoring


```
  

  

---

# **Revisión de Pull Requests**

Los PR serán evaluados considerando:

- Calidad técnica
  
- Claridad y completitud de la documentación
  
- Consistencia con el proyecto
  
- Buenas prácticas SRE y DevOps
  

Podrían solicitarse ajustes antes de aprobarse.

