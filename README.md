# 🧠 Agente LDAP con LLM (Gemini + LangChain)

Este proyecto implementa un **agente conversacional** capaz de consultar un servidor **LDAP** utilizando un **modelo de lenguaje Gemini** a través de **LangChain**.
Permite obtener información de usuarios y los grupos a los que pertenecen mediante consultas en lenguaje natural.

---

## 🚀 Características

* Conexión a **OpenLDAP** usando la librería `ldap3`.
* Consultas dinámicas sobre:

  * Información del usuario actual.
  * Grupos a los que pertenece un usuario específico.
* Integración con **Google Gemini** a través de `langchain-google-genai`.
* Interfaz interactiva desde consola.

---

## 🧬 Estructura del proyecto

```
.
├── ldap_tools.py        # Funciones para interactuar con el servidor LDAP
├── main.py              # Inicializa el agente y maneja el loop de conversación
├── pyproject.toml       # Dependencias del proyecto (Poetry)
└── README.md            # Este archivo
```

---

## ⚙️ Requisitos

* Python **3.12+**
* [Poetry](https://python-poetry.org/docs/#installation)
* Clave API de **Google Gemini**

---

## 🔧 Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/mauricio-chiabrando/meli_offsec_challenge.git
   cd meli_offsec_challenge
   ```

2. Instalar dependencias con **Poetry**:

   ```bash
   poetry install
   poetry shell
   ```

3. Exportar tu clave de **Gemini**:

   ```bash
   export GOOGLE_API_KEY="TU_API_KEY_DE_GEMINI"
   ```

---

## ▶️ Uso

Debido a que el usuario que ejecuta el agente no está en el servidor LDAP provisto, el usuario por el cual se consulta se deberá definir directamente en el archivo ldap_tools.py:

```bash
conn.search(BASE_DN_USERS, "(cn=USUARIO_DE_LDAP)", SUBTREE, attributes=["cn","uid","mail"]) 
```

Ejecutar el agente desde la terminal:

```bash
python3 main.py
```

Luego podés escribir consultas naturales como:

```
>> ¿Quién soy?
>> ¿A qué grupos pertenezco?
>> ¿Qué grupos tiene el usuario john.doe?
```

Para salir:

```
exit
```

---

## 🧠 Funcionamiento interno

El agente utiliza **LangChain** con un modelo **Gemini 2.5 Flash**.
Se le asignan dos herramientas principales:

| Herramienta             | Descripción                                                   |
| ----------------------- | ------------------------------------------------------------- |
| `get_current_user_info` | Devuelve la información del usuario autenticado en LDAP       |
| `get_user_groups`       | Devuelve los grupos a los que pertenece un usuario específico |

Ejemplo de configuración del modelo:

```python
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)
```

---

## 🧪 Ejemplo de salida

```
Agente de consulta LDAP con LLM iniciado. Podés escribir en lenguaje natural (exit para salir).

>> ¿Quién soy?
Eres el usuario con cn 'test.user', uid 'test.user', y tu correo es 'test.user@meli.com'.

>> ¿A qué grupos pertenezco?
Perteneces a los grupos: qa, all_users.
```

---

## 👨‍💻 Autor

**Mauricio Chiabrando**

💼 Challenge Técnico Offensive Security - Mercado Libre

📧 Contacto: [[mauricio.chiabrando@gmail.com](mailto:mauricio.chiabrando@gmail.com)]

---
