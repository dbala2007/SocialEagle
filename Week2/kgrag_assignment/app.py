import streamlit as st
from rag_chain import RAGChain
from chat_message import ChatMessage

st.set_page_config(
    page_title="Tamil Nadu Schemes Assistant",
    page_icon="🏛️",
    layout="wide"
)

st.title("🏛️ Tamil Nadu Government Schemes Assistant")

st.caption("Ask questions about Tamil Nadu Government Schemes")

@st.cache_resource
def load_rag():
    return RAGChain()

rag = load_rag()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask about Tamil Nadu Government schemes")

history = [
    ChatMessage(
        role=msg["role"],
        content=msg["content"],
    ) for msg in st.session_state.messages
]

if question:
    st.session_state.messages.append(
        {
            "role":"user",
            "content":question
        }
    )
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Searching schemes"):
            response = rag.invoke(question=question, history=history)
            st.markdown(response.answer)

            with st.expander("📚 Sources"):
                for source in response.sources:
                    st.markdown(f"***{source.scheme_name}***")

                    st.markdown(source.url)

                    st.divider()
            st.session_state.messages.append(
                {
                    "role":"assistant",
                    "content":response.answer
                }
            )