### Inicializar el proyecto

- Crear entorno virtual (Primero se debe instalar venv si no se tiene)
``` bash
  python -m venv .env
```
- Encender entorno virtual
```bash
  .env\Scripts\activate
```
- Instalar las dependecias
```bash
  pip install -r requirements.txt
```
- Crear el archivo .envvars según .envvarsexample
- Para DATABASE_NAME ejecutar en mysql CREATE DATABASE \<ed-db\> y usar ese nombre
- RUN
```bash
  python src/utils/creartablas.py
```
- Ejecutar el proyecto
```bash
  python src/run.py
```
- Para salir desactivar el entorno virtual
```bash
  deactivate
```
