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
