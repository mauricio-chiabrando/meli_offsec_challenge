import os
import sys

os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GRPC_TRACE"] = ""
sys.stderr = open(os.devnull, "w")

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, Tool
from ldap_tools import get_current_user_info, get_user_groups, list_all_users, list_all_groups, search_privileged_accounts

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

tools = [
    Tool(
        name="get_current_user_info",
        func=lambda _: str(get_current_user_info()),
        description="Devuelve la información del usuario actualmente autenticado en LDAP."
    ),
    Tool(
        name="get_user_groups",
        func=lambda username_str=None: str(get_user_groups(username_str)),
        description="Devuelve los grupos a los que pertenece un usuario específico de LDAP. Se usa pasando el nombre del usuario."
    ),
    Tool(
        name="list_all_users",
        func=lambda _: str(list_all_users()),
        description="Enumera todos los usuarios visibles en el dominio LDAP."
    ),
    Tool(
        name="list_all_groups",
        func=lambda _: str(list_all_groups()),
        description="Lista todos los grupos disponibles en LDAP."
    ),
    Tool(
        name="search_privileged_accounts",
        func=lambda _: str(search_privileged_accounts()),
        description="Busca cuentas sensibles, privilegiadas, con altos permisos o de servicio comunes."
    )
]

agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=False,
    handle_parsing_errors=True
)

def run_agent():
    print("Agente de consulta LDAP con LLM iniciado. Podés escribir en lenguaje natural (exit para salir).\n")
    while True:
        query = input(">> ")
        if query.lower() in ("exit", "quit"):
            print("Cerrando agente...")
            break
        try:
            response = agent.invoke(query)
            print(response["output"])
        except Exception as e:
            print(f"Error ejecutando la consulta: {e}")

if __name__ == "__main__":
    run_agent()
