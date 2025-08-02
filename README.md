# Informe Final del Proyecto: Módulo de Gestión de Tareas
# Actividad Autónoma 1

**Autor:** Pablo Guber Camacho Bravo
**Fecha:** 1 de agosto del 2025
**NRC:** 23267

---

## Índice

1. [Definición del módulo: Sistema de Registro de Usuarios](#1-definición-del-módulo-sistema-de-registro-de-usuarios)
2. [Planificación ágil](#2-planificación-ágil)
3. [Prácticas de XP](#3-prácticas-de-xp)
4. [Implementación](#4-implementación)
5. [Conclusión](#5-conclusión)

---

## 1. Definición del módulo: Sistema de Registro de Usuarios

El **Sistema de Registro de Usuarios** es un módulo funcional que permite a nuevos usuarios crear una cuenta dentro de una aplicación web. Su objetivo principal es facilitar el ingreso de usuarios legítimos mediante la recopilación de información básica como nombre completo, correo electrónico y contraseña, garantizando al mismo tiempo la validación adecuada de datos y el almacenamiento seguro de credenciales.

Este módulo constituye una pieza fundamental en el ciclo de vida de aplicaciones modernas que requieren autenticación, al proporcionar la base sobre la cual se gestionará el acceso seguro a funcionalidades protegidas. Su desarrollo se realizará aplicando las metodologías ágiles SCRUM y XP, incluyendo prácticas de programación por parejas, desarrollo guiado por pruebas (TDD) y la gestión colaborativa de artefactos como Product Backlog y Sprint Backlog.

### Requisitos funcionales

| Código | Requisito Funcional | Descripción |
|--------|-------------------|-------------|
| RF1 | Registro de usuario | El sistema debe permitir que los usuarios se registren ingresando su nombre completo, correo electrónico, contraseña y confirmación de contraseña. |
| RF2 | Validación de campos | El sistema debe validar que todos los campos estén completos y que el correo tenga un formato válido. |
| RF3 | Coincidencia de contraseñas | El sistema debe verificar que la contraseña y su confirmación coincidan. |
| RF4 | Evitar registros duplicados | El sistema debe verificar que el correo electrónico ingresado no esté previamente registrado. |
| RF5 | Hash de contraseñas | Las contraseñas deben almacenarse de forma segura utilizando algoritmos de hash (como bcrypt o equivalente). |
| RF6 | Mensaje de confirmación | Tras un registro exitoso, el sistema debe mostrar un mensaje que indique al usuario que su cuenta ha sido creada correctamente. |
| RF7 | Mensajes de error claros | En caso de errores, el sistema debe mostrar mensajes informativos que indiquen qué campo requiere corrección. |

---

## 2. Planificación ágil

### Product Backlog (Historias de Usuario)

Usaremos el formato:
**Como [tipo de usuario], quiero [acción] para [beneficio].**

| ID | Historia de Usuario | Prioridad | Criterios de Aceptación |
|----|-------------------|-----------|------------------------|
| HU1 | Como usuario, quiero ver un formulario de registro para crear una cuenta nueva. | Alta | Se muestra un formulario con los campos: nombre, correo, contraseña y confirmación de contraseña. |
| HU2 | Como usuario, quiero que se validen mis datos para evitar errores en el registro. | Alta | El sistema muestra errores si algún campo está vacío o el correo no es válido. |
| HU3 | Como usuario, quiero que el sistema me avise si ya estoy registrado con mi correo. | Alta | El sistema muestra un mensaje de "correo ya registrado" si el email ya existe. |
| HU4 | Como usuario, quiero que mi contraseña se guarde de forma segura. | Media | Las contraseñas se almacenan en la base de datos usando hash seguro (bcrypt u otro). |
| HU5 | Como usuario, quiero recibir un mensaje de éxito al registrarme correctamente. | Media | El sistema muestra "Registro exitoso" al completar el formulario sin errores. |
| HU6 | Como desarrollador, quiero asegurar que el código esté cubierto por pruebas unitarias. | Alta | Cada funcionalidad está cubierta por al menos una prueba automatizada que verifica su correcto funcionamiento. |

### Sprint Backlog

Para el desarrollo se plantearon dos sprints simulados, cada uno con historias específicas que pueden completarse en un periodo de trabajo iterativo.

#### Sprint 1: Estructura base y validación
**Duración estimada:** 1 semana  
**Objetivo:** Mostrar formulario y validar entradas del usuario.

| ID | Historia de Usuario | Tareas técnicas |
|----|-------------------|----------------|
| HU1 | Formulario de registro | Crear interfaz del formulario con los campos requeridos |
| HU2 | Validación de campos | Implementar validaciones de campos vacíos y formato de correo |
| HU3 | Verificar correo duplicado | Programar verificación contra base de datos (o archivo simulado) |

#### Sprint 2: Seguridad y experiencia de usuario
**Duración estimada:** 1 semana  
**Objetivo:** Agregar seguridad, retroalimentación al usuario y pruebas unitarias.

| ID | Historia de Usuario | Tareas técnicas |
|----|-------------------|----------------|
| HU4 | Guardado seguro de contraseña | Implementar almacenamiento usando hashing (bcrypt u otro) |
| HU5 | Confirmación visual | Mostrar mensajes visuales de éxito o error al usuario |
| HU6 | Pruebas unitarias (TDD) | Escribir pruebas antes de codificar, validar funcionalidades |

### Link hacia el Tablero de Planificación en Trello:
[https://trello.com/invite/b/688ccc09c4e76549238fca4a/ATTIce7367911d99de40159277ab485d0747E9EFA358/sistema-de-registro-de-usuarios](https://trello.com/invite/b/688ccc09c4e76549238fca4a/ATTIce7367911d99de40159277ab485d0747E9EFA358/sistema-de-registro-de-usuarios)

---

## 3. Prácticas de XP

Durante el desarrollo del módulo "Sistema de Registro de Usuarios", se aplicaron dos prácticas fundamentales de XP: la **programación por parejas** y el **Desarrollo Guiado por Pruebas (TDD)**. Estas prácticas permitieron mejorar la calidad del código, fomentar el trabajo colaborativo y asegurar que las funcionalidades cumplieran con los requisitos definidos desde el inicio.

### Programación por parejas

La programación por parejas consistió en trabajar de forma conjunta en una misma máquina (o entorno compartido), alternando los roles de:

- **Driver (conductor):** Persona encargada de escribir el código directamente.
- **Observer/Navigator (observador):** Persona que analiza la lógica, identifica errores, sugiere mejoras y revisa que el código cumpla con los criterios establecidos.

Durante cada sprint, se realizaron sesiones planificadas de codificación en pareja. Al final de cada sesión, los roles se intercambiaron para garantizar la participación activa de ambos miembros y promover la retroalimentación constante.

#### Beneficios observados:
- Reducción de errores gracias a la revisión continua.
- Mayor claridad en la lógica del código.
- Mejora en la comunicación técnica entre los miembros del equipo.

### Desarrollo Guiado por Pruebas (TDD)

Se adoptó el enfoque de **Test-Driven Development (TDD)** para el desarrollo de las funcionalidades principales del módulo. Este enfoque se implementó siguiendo el ciclo:

1. **Red:** Escribir una prueba fallida que represente un comportamiento esperado.
2. **Green:** Escribir el código mínimo necesario para pasar la prueba.
3. **Refactor:** Refactorizar el código para mejorar su calidad sin alterar su funcionalidad.

#### Pruebas implementadas:
- Validación de campos vacíos (nombre, correo, contraseña).
- Verificación de coincidencia entre contraseña y su confirmación.
- Formato válido de correo electrónico.
- Prevención de registros duplicados por correo.
- Confirmación de mensaje de éxito tras registro válido.

---

## 4. Implementación

### Enfoque TDD (Test-Driven Development)

#### Paso 1: Escribir la prueba primero (test fallido)

Creamos un archivo llamado `test_validaciones.py` con una prueba inicial:

```python
# test_validaciones.py
from validaciones import validar_correo

def test_correo_valido():
    assert validar_correo("usuario@dominio.com") == True

def test_correo_vacio():
    assert validar_correo("") == False

def test_correo_invalido():
    assert validar_correo("usuario.com") == False
```

#### Paso 2: Implementar solo lo necesario para que pase el test

Creamos el archivo `validaciones.py` con la función mínima viable:

```python
# validaciones.py
import re

def validar_correo(correo):
    if not correo:
        return False
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, correo) is not None
```

### Código final

```python
# validaciones.py
import re

def validar_correo(correo):
    if not correo:
        return False
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, correo) is not None

def test_correo_valido():
    assert validar_correo("usuario@dominio.com") == True

def test_correo_vacio():
    assert validar_correo("") == False

def test_correo_invalido():
    assert validar_correo("usuario.com") == False
```

### Mantener el código en un repositorio GitHub con historial de commits

#### Proceso seguido:

1. **Crear un repositorio en GitHub**

2. **Clonar el repositorio en el ordenador:**
   ```bash
   git clone https://github.com/P4Bl0-Camacho/registro-usuarios-scrum-xp.git
   ```

3. **Entrar a la carpeta del repositorio:**
   ```bash
   cd registro-usuarios-scrum-xp
   ```

4. **Inicializar Git:**
   ```bash
   git init
   ```

5. **Colocar los archivos Python en la carpeta**

6. **Añadir los archivos al repositorio:**
   ```bash
   git add .
   ```

7. **Realizar el primer commit:**
   ```bash
   git commit -m "Primer commit: agregar archivos iniciales"
   ```

8. **Subir los cambios al repositorio GitHub:**
   ```bash
   git push
   ```

---

## 5. Conclusión

El desarrollo del módulo "Sistema de Registro de Usuarios" permitió aplicar de manera efectiva los principios de las metodologías ágiles SCRUM y Extreme Programming (XP) en un entorno académico simulado. A través de la definición clara del Product Backlog, la organización en sprints y el uso de tableros colaborativos como Trello, se logró estructurar el trabajo de forma iterativa y enfocada en la entrega de valor continuo.

La práctica de programación por parejas fortaleció la comunicación y la revisión constante del código, mientras que el uso de Desarrollo Guiado por Pruebas (TDD) aseguró la calidad y el correcto funcionamiento del módulo desde sus primeras etapas. Además, el uso de herramientas como GitHub permitió evidenciar el progreso mediante un historial de commits claro y ordenado.

### Lecciones aprendidas:

#### Lo que funcionó bien (Continue):
- La programación por parejas mejoró significativamente la calidad del código
- TDD nos ayudó a mantener el foco en los requisitos desde el inicio
- El uso de Trello facilitó la organización y seguimiento del progreso
- Los sprints cortos permitieron entregas incrementales de valor

#### Lo que podríamos mejorar (Start):
- Implementar Daily Scrums más estructurados
- Agregar más automatización en el proceso de testing
- Mejorar la documentación técnica del código

#### Lo que deberíamos evitar (Stop):
- Commits muy grandes que dificultan el seguimiento
- Procrastinar la escritura de pruebas

La aplicación de estas metodologías ágiles no solo mejoró la calidad del producto final, sino que también proporcionó valiosa experiencia en prácticas de desarrollo colaborativo que son fundamentales en la industria del software moderno.
