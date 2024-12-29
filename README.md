# Mascota Rescate

Una aplicación web para la adopción de mascotas, desarrollada con Django.

## Características

- Registro y autenticación de usuarios
- Listado de mascotas disponibles para adopción
- Panel de administración para gestionar mascotas
- Carga y gestión de imágenes de mascotas
- Interfaz responsive y moderna

## Requisitos

- Python 3.8 o superior
- PostgreSQL (producción)
- Pip (gestor de paquetes de Python)

## Instalación Local

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/JuliAlvarez-P/ProyectoFinal.git
   cd ProyectoFinal
   ```

2. Crear y activar entorno virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configurar variables de entorno:
   - Crear archivo `.env` en la raíz del proyecto
   - Copiar contenido de `.env.example`
   - Actualizar valores según necesidad

5. Aplicar migraciones:
   ```bash
   python manage.py migrate
   ```

6. Crear superusuario:
   ```bash
   python manage.py createsuperuser
   ```

7. Ejecutar servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

## Despliegue en Heroku

1. Crear nueva aplicación en Heroku

2. Configurar variables de entorno en Heroku:
   - DJANGO_SECRET_KEY
   - DJANGO_DEBUG
   - DJANGO_ALLOWED_HOSTS
   - DATABASE_URL

3. Conectar repositorio y desplegar:
   ```bash
   heroku git:remote -a nombre-de-tu-app
   git push heroku main
   ```

4. Aplicar migraciones:
   ```bash
   heroku run python manage.py migrate
   ```

5. Crear superusuario:
   ```bash
   heroku run python manage.py createsuperuser
   ```

## Mantenimiento

- Actualizar dependencias:
  ```bash
  pip install -r requirements.txt
  ```

- Aplicar migraciones pendientes:
  ```bash
  python manage.py migrate
  ```

- Recolectar archivos estáticos:
  ```bash
  python manage.py collectstatic
  ```

## Contribuir

1. Fork el repositorio
2. Crear rama para nueva característica
3. Commit cambios
4. Push a la rama
5. Crear Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT.
