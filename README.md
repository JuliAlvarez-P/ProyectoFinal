# Mascota Rescate - Plataforma de Adopción de Mascotas

Una aplicación web desarrollada con Django para facilitar la adopción de mascotas y ayudar a animales necesitados a encontrar un hogar amoroso.

## Características

- Registro y autenticación de usuarios
- Perfiles de usuario personalizables
- Listado de mascotas disponibles para adopción
- Detalles completos de cada mascota
- Formulario para agregar nuevas mascotas
- Sección "Cómo Ayudar" con información sobre donaciones y voluntariado
- Interfaz intuitiva y fácil de usar

## Tecnologías Utilizadas

- Python 3.10
- Django 4.2
- SQLite3
- HTML5
- CSS3
- Bootstrap 5

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
source venv/bin/activate  # Linux/Mac
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Realizar migraciones:
```bash
cd project_files/mascota_rescate_core
python manage.py migrate
```

5. Crear superusuario:
```bash
python manage.py createsuperuser
```

6. Iniciar servidor de desarrollo:
```bash
python manage.py runserver
```

## Despliegue en PythonAnywhere

La aplicación está desplegada en PythonAnywhere y puede accederse en:
[http://Juli0406.pythonanywhere.com](http://Juli0406.pythonanywhere.com)

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios que te gustaría realizar.

## Autor

- Julieta Alvarez
- Contacto: julieta2000facultad@gmail.com
