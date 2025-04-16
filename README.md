# 📚 Aplicación CRUD de Registro de Estudiantes

Esta aplicación ha sido desarrollada en **Python** y tiene como objetivo principal el **registro de estudiantes**. Utiliza una base de datos gestionada con **MySQL Workbench**, específicamente la tabla denominada `estudiantes` dentro de la base de datos `unap`.

## 🚀 Instalación y Uso

### Requisitos previos
- Python 3.8+
- MySQL Workbench
- Biblioteca `mysql-connector-python`

### Instalación
1. Clona el repositorio:
   ```bash
   git clone [URL_DEL_REPOSITORIO]
   cd nombre-del-repositorio
   ```

2. Instala las dependencias:
   ```bash
   pip install mysql-connector-python
   ```

3. Configura la base de datos:
   - Crea una base de datos llamada `unap` en MySQL
   - Ejecuta el siguiente script SQL:
     ```sql
     CREATE TABLE estudiantes (
         id INT PRIMARY KEY,
         nombre VARCHAR(255),
         sección VARCHAR(255),
         edad INT
     );
     ```

### Ejecución
```bash
python main.py
```

## 🧩 Características Principales

La aplicación implementa un sistema completo de operaciones **CRUD (Crear, Leer, Actualizar, Eliminar)**:

### ✅ Crear
Permite registrar nuevos estudiantes ingresando los datos en los campos correspondientes y presionando el botón `Insertar`.  
Al insertar correctamente, se muestra el mensaje:
```
Éxito, Estudiante insertado correctamente.
```

### 📄 Leer
Muestra todos los estudiantes registrados en la tabla `estudiantes`, utilizando una tabla visual dentro de la interfaz mediante la función `actualizar_treeview`.

### 🔄 Actualizar
Permite modificar la información de un estudiante existente:
1. Seleccionar una fila en la tabla.
2. Modificar los campos necesarios.
3. Presionar el botón `Actualizar`.

### ❌ Eliminar
Facilita la eliminación de registros seleccionando una fila de la tabla y presionando el botón `Eliminar`.  
Internamente utiliza la función `eliminar_estudiante` y la sentencia SQL:
```sql
DELETE FROM estudiantes WHERE id=%s
```

## 🔐 Seguridad contra Inyección SQL
Se ha implementado una función llamada `es_entrada_segura`, que detecta entradas maliciosas basadas en palabras clave como:
```
drop, delete, insert, update, --, ;, /*, */
```
Si se detectan, se lanza el mensaje de error:
```
Datos inválidos o inseguros
```

## 🛠️ Conexión a la Base de Datos
La conexión se realiza mediante la librería `mysql.connector`, utilizando la función `obtener_conexión`, que toma los siguientes parámetros:
- `host`
- `usuario`
- `contraseña`
- `nombre de la base de datos`

## 🗃️ Estructura de la Base de Datos
**Tabla:** `estudiantes`

| Campo    | Tipo          | Descripción                     |
|----------|---------------|---------------------------------|
| id       | INT           | Identificador único del estudiante |
| nombre   | VARCHAR(255)  | Nombre del estudiante           |
| sección  | VARCHAR(255)  | Sección a la que pertenece       |
| edad     | INT           | Edad del estudiante             |

## 📎 Recurso Adicional
- [Video demostrativo](https://youtu.be/57zvgDe1iSQ) de la interfaz CRUD y simulación de inyección SQL

