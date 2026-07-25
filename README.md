# 🤖 Challenge Alura - Agente Inteligente de Soporte E-Commerce

¡Bienvenido al repositorio del proyecto **Agente Inteligente de Soporte para TechStore AI**! Desarrollado para el **Challenge Alura / Oracle Next Education (ONE)**.

---

## 📌 1. Descripción General del Proyecto

**TechStore AI Agent** es una solución de Inteligencia Artificial diseñada para responder de forma automatizada, precisa y eficiente las consultas más frecuentes de los clientes de una tienda virtual (E-commerce).

El agente utiliza técnicas de **Retrieval-Augmented Generation (RAG)** e ingesta de documentos en formatos **PDF** y **CSV** para fundamentar sus respuestas en la normativa real de la empresa.

---

## 🏗️ 2. Arquitectura de la Solución

```text
[Usuario] ---> [Interfaz de Usuario (Streamlit)]
                      │
                      ▼
          [Motor del Agente AI (Python)]
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
[PDF Reader / Ingestion]  [CSV Query Engine]
(Base_de_Conocimiento.pdf) (preguntas_frecuentes.csv)
````

Entrada: El cliente realiza una consulta mediante la interfaz de chat interactiva.

Procesamiento e Ingesta: El motor lee y analiza la Base de Conocimiento en PDF y la tabla CSV de preguntas frecuentes.

Búsqueda & Extracción: La consulta es evaluada frente a los documentos fuente para extraer la respuesta contextual exacta.

Respuesta: El agente genera una respuesta precisa, citando la fuente exacta de la información utilizada.

🛠️ 3. Tecnologías Utilizadas
Lenguaje: Python 3.10+

Framework Web & UI: Streamlit

Procesamiento de Documentos: PyPDF, Pandas

Infraestructura (Deploy): Oracle Cloud Infrastructure (OCI) / Compute Instance

Control de Versiones: Git & GitHub

🚀 4. Guía para Replicar el Proyecto
Cualquier evaluador o usuario puede ejecutar este proyecto en su máquina local siguiendo estos pasos:

1. Clonar el repositorio:
````
git clone [https://github.com/TU_USUARIO/desafio-alura-agente-inteligente.git](https://github.com/TU_USUARIO/desafio-alura-agente-inteligente.git)
cd desafio-alura-agente-inteligente
````
2. Instalar dependencias:
````
pip install -r requirements.txt
````
3. Ejecutar la aplicación:
````
streamlit run app.py
````
4. Acceder a la aplicación: Abre tu navegador web en http://localhost:8501.

💬 5. Ejemplos de Preguntas y Respuestas del Agente
Pregunta: "¿Cuánto tarda el envío a provincias y cuál es el costo?"

Respuesta: "El envío a provincias cuesta $10.00 USD o es gratis por compras superiores a $100 USD. Tarda entre 3 a 5 días hábiles. (Fuente: CSV / PDF)"

Pregunta: "¿Cuál es el plazo para solicitar una devolución?"

Respuesta: "Tienes hasta 30 días calendario desde la recepción para solicitar la devolución. (Fuente: Base_de_Conocimiento_Ecommerce.pdf)"

☁️ 6. Evidencia del Deploy en Oracle Cloud Infrastructure (OCI)
🌐 URL Pública de la aplicación: http://<IP_PUBLIC_OCI>:8501
