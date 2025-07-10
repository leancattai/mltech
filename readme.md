# M&L Tech 🚀

Sitio web oficial de **M&L Tech**, una startup enfocada en:

- Desarrollo de software a medida
- Automatizaciones con Python
- Integraciones de APIs
- Consultoría tecnológica
- Soluciones web modernas, accesibles y eficientes

---

## 🛠 Tecnologías utilizadas

- **Frontend**: HTML5, Tailwind CSS, Alpine.js, AOS.js, Tabler Icons
- **Backend**: Flask (Python-ready, opcional)
- **Extras**: HTMX, diseño responsive, animaciones suaves, arquitectura modular

---

## 🚀 ¿Cómo levantar el proyecto localmente?

### 1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/ml-tech.git
cd ml-tech
```

### 2. Crear y activar entorno virtual (recomendado)

python -m venv venv

# En Windows:

venv\Scripts\activate

# En Unix/macOS:

source venv/bin/activate

### 3. Instalar dependencias

pip install flask

### 4. Ejecutar la aplicación

py main.py

### 📁 Estructura del proyecto

ml-tech/
├── static/
│ └── assets/
│ └── icons/
├── templates/
│ ├── components/
│ │ ├── servicios-grid.html
│ │ ├── portfolio-grid.html
│ │ ├── float-icons.html
│ │ └── float-icons-style.jinja
│ ├── includes/
│ │ ├── head.html
│ │ ├── navbar.html
│ │ └── footer.html
│ ├── index.html
│ ├── servicios.html
│ ├── portfolio.html
│ ├── quienes-somos.html
│ └── contacto.html
├── main.py
└── README.md

### 📌 Notas

El sitio está optimizado para SEO básico y accesibilidad.

Todas las secciones son responsivas y animadas con AOS.js.

Listo para conectar a backend Flask si se desea.

Favicon SVG personalizado incluido en /static/assets/icons/.
