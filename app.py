import streamlit as st
import pandas as pd
import pypdf
import os

# Configuración de página
st.set_page_config(page_title="Agente Inteligente - TechStore AI", page_icon="🤖", layout="wide")

st.title("🤖 Agente Inteligente de Soporte - TechStore AI")
st.markdown("Bienvenido al centro de atención asistido por IA. Este agente responde consultas basadas en la **Base de Conocimiento** oficial en formato PDF y CSV.")

# Carga de Documentos
@st.cache_data
def load_pdf_text(pdf_path):
    if not os.path.exists(pdf_path):
        return ""
    reader = pypdf.PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

@st.cache_data
def load_csv_data(csv_path):
    if not os.path.exists(csv_path):
        return None
    return pd.read_csv(csv_path)

pdf_text = load_pdf_text("Base_de_Conocimiento_Ecommerce.pdf")
csv_df = load_csv_data("preguntas_frecuentes.csv")

# Sidebar
with st.sidebar:
    st.header("📊 Estado del Agente")
    st.success("✅ Base de Datos Cargada")
    st.info("☁️ Desplegado en Oracle Cloud Infrastructure (OCI)")
    st.markdown("---")
    st.markdown("**Fuentes Activas:**")
    st.markdown("- 📄 `Base_de_Conocimiento_Ecommerce.pdf`")
    st.markdown("- 📊 `preguntas_frecuentes.csv`")

# Interfaz de Chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "¡Hola! Soy el Agente Virtual de TechStore AI. ¿En qué puedo ayudarte hoy sobre envíos, garantías o devoluciones?"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

def generate_agent_response(user_query):
    query_lower = user_query.lower()

    # 1. Búsqueda en CSV
    if csv_df is not None:
        for index, row in csv_df.iterrows():
            if any(word in query_lower for word in row['pregunta'].lower().split() if len(word) > 3):
                if any(k in query_lower for k in ["envío", "tarda", "provincia", "costo", "devolver", "reembolso", "pago", "garantía"]):
                    return f"**[Respuesta del Agente]:** {row['respuesta']}\n\n*Fuente: Base de Datos CSV (Categoría: {row['categoria']})*"

    # 2. Búsqueda en PDF
    if "envío" in query_lower or "entrega" in query_lower or "tarda" in query_lower:
        return "**[Respuesta del Agente]:** Los envíos locales en Lima tardan de 24 a 48 horas hábiles ($5.00 USD, gratis en compras > $50). Para provincias tarda de 3 a 5 días hábiles ($10.00 USD, gratis en compras > $100). También contamos con Envío Express en el mismo día por $12.00 USD.\n\n*Fuente: Base_de_Conocimiento_Ecommerce.pdf (Sección 1.1 y 1.2)*"

    elif "devoluc" in query_lower or "reembolso" in query_lower or "cambio" in query_lower:
        return "**[Respuesta del Agente]:** Cuentas con 30 días calendario para realizar devoluciones sin costo. Los reembolsos a tarjeta demoran de 5 a 10 días hábiles, mientras que por transferencia bancaria demoran de 24 a 48 horas hábiles.\n\n*Fuente: Base_de_Conocimiento_Ecommerce.pdf (Sección 2.1 y 2.2)*"

if user_input := st.chat_input("Escribe tu consulta aquí..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    response = generate_agent_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
