from datetime import datetime

from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langgraph.graph.state import RunnableConfig
from rich import print
from rich.markdown import Markdown
from rich.prompt import Prompt

from src.graph import build_graph
from src.prompts.prompts import SYSTEM_PROMPT


def main() -> None:
    graph = build_graph()
    config = RunnableConfig(configurable={"thread_id": 1})
    all_messages: list[BaseMessage] = []

    prompt = Prompt()
    Prompt.prompt_suffix = ""
    
    # Obter data e ano atual para o prompt
    now = datetime.now()
    current_date = now.strftime("%d de %B de %Y")
    current_year = now.year
    
    # Formatar o prompt com data atual
    formatted_prompt = SYSTEM_PROMPT.format(
        current_date=current_date,
        current_year=current_year
    )

    while True:
        user_input = prompt.ask("[bold cyan]Você: \n")
        print(Markdown("\n\n  ---  \n\n"))

        if user_input.lower() in ["q", "quit", "exit"]:
            break

        human_message = HumanMessage(user_input)
        current_loop_messages = [human_message]

        if len(all_messages) == 0:
            current_loop_messages = [SystemMessage(formatted_prompt), human_message]

        result = graph.invoke({"messages": current_loop_messages}, config=config)

        print("[bold cyan]RESPOSTA: \n")
        print(Markdown(result["messages"][-1].content))
        print(Markdown("\n\n  ---  \n\n"))

        all_messages = result["messages"]

    print(all_messages)


if __name__ == "__main__":
    main()