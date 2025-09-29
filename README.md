# 🚇 Sistema Inteligente de Rutas en Transporte Masivo

Este proyecto implementa un sistema inteligente en **Python** que, a partir de una **base de conocimiento en reglas lógicas**, calcula la **mejor ruta entre dos estaciones** en un sistema de transporte masivo.  

Incluye:
- 📂 Base de conocimiento en formato Prolog-like (`kb/`).
- ⚙️ Código Python modular (`src/`).
- 🧭 Algoritmo de búsqueda de rutas (Dijkstra con penalización de transbordo).
- 📑 Documentación (`docs/`).
- 🎥 Video explicativo (se agregará en la entrega final).
- 🌐 Repositorio con commits de cada integrante del equipo.

---

## 🚀 Instalación

### Requisitos
- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

### Pasos de instalación
1. Clonar el repositorio:
   ```bash
   git clone <[URL_DEL_REPO](https://github.com/John-fonseca/IA-Ruta-Transporte.git)>
   cd ruta-transporte
   cd /src
   Ejecutar -> python main.py --start A --goal C (example)
   Ejecutar -> python main.py --kb ../kb/estaciones.txt --start "Portal Norte" --goal "Universidades"
   Ejecutar -> python main.py --kb ../kb/kb_example3.txt --start "Estacion Sur" --goal "Estacion Norte"


   
