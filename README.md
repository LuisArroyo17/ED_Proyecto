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
- Ejecutar en mysql CREATE DATABASE 'ed-db';
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
-----------------Para el front------------------
- Verificar si Node.js está instalado
```bash
  node -v
```
- 1 Ingresa al directorio del proyecto
```bash
  cd ed-front
```
- 2 Instala las dependencias
```bash
  npm install
```
- 3 Inicia el servidor de desarrollo
```bash
  npm run dev
```
