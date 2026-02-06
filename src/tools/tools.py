from langchain.tools import BaseTool

from .calculator import multiply, add, subtract, divide
from .valida_cpf import validar_cpf
from .google_calendar import list_calendar_events, create_calendar_event, delete_calendar_event


TOOLS: list[BaseTool] = [
    multiply,
    add,
    subtract,
    divide,
    validar_cpf,
    list_calendar_events, 
    create_calendar_event,
    delete_calendar_event
]
TOOLS_BY_NAME = {tool.name: tool for tool in TOOLS}
