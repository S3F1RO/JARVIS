from tools.exercise_generator import generate_exercise
import json

def main():
    exercise = generate_exercise()
    print("Question: " + exercise['question'])
    print("Answer: " + exercise['expected_answer'])
    print("Difficulty: " + str(exercise['difficulty']))
    print('Exercise: ')
    print(json.dumps(exercise,indent=4))

if __name__ == "__main__":
    main()

































# def configure_mistral_provider() -> None:
#     """Branche le SDK openai-agents sur l'API Mistral (compatible OpenAI). Déjà écrit."""
#     api_key = os.getenv("MISTRAL_API_KEY")
#     if not api_key:
#         raise SystemExit(
#             "MISTRAL_API_KEY manquante. Copie .env.example vers .env puis ajoute ta cle Mistral."
#         )
#     client = AsyncOpenAI(
#         api_key=api_key,
#         base_url=os.getenv("MISTRAL_BASE_URL", DEFAULT_MISTRAL_BASE_URL),
#     )
#     set_default_openai_client(client, use_for_tracing=False)
#     set_default_openai_api("chat_completions")
#     set_tracing_disabled(True)


# def build_agent(mcp_server: MCPServerStreamableHttp) -> Agent:
#     return Agent(
#         name="Jarvis",
#         model=os.getenv("MISTRAL_MODEL", DEFAULT_MISTRAL_MODEL),
#         instructions=(
#             "Tu es un professeur de mathématiques qui utilise une base PostgreSQL exposee via MCP pour la progression. "
#             "Explique chaque étape de ton raisonnement"
#             "Utilise les outils MCP quand la question concerne les etudiants, les cours "
#             "ou les notes. Ne pretends jamais connaitre une donnee sans l'avoir lue "
#             "dans la base via un outil."
#         ),
#         mcp_servers=[mcp_server]
#     )


# def main() -> None:
#     load_dotenv()
#     configure_mistral_provider()
#     print("Agent Deployed")

# if __name__ == "__main__":
#     main()
