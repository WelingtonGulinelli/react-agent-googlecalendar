import os.path
import datetime
from typing import Optional, Any

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from langchain.tools import tool

SCOPES = ["https://www.googleapis.com/auth/calendar"]


def get_calendar_service() -> Any:
    """Autentica e retorna o serviço do Google Calendar"""
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json")
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "src/tools/credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w", encoding="utf-8") as token:
            token.write(creds.to_json())
    
    return build("calendar", "v3", credentials=creds)  # type: ignore


@tool
def list_calendar_events(max_results: int = 10) -> str:
    """Lista os próximos eventos do Google Calendar do usuário.
    
    Args:
        max_results: Número máximo de eventos a retornar (padrão: 10)
        
    Returns:
        String formatada com a lista de eventos ou mensagem se não houver eventos
    """
    try:
        service = get_calendar_service()
        now = datetime.datetime.now().isoformat() + "Z"
        
        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=max_results,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])

        if not events:
            return "Nenhum evento próximo encontrado no calendário."
        
        result = []
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            summary = event.get("summary", "Sem título")
            result.append(f"📅 {start}: {summary}")
        
        return "\n".join(result)

    except HttpError as error:
        return f"Erro ao acessar o Google Calendar: {error}"


@tool
def create_calendar_event(
    summary: str,
    start_time: str,
    end_time: str,
    description: Optional[str] = None,
    location: Optional[str] = None
) -> str:
    """Cria um novo evento no Google Calendar.
    
    Args:
        summary: Título do evento
        start_time: Data/hora de início (formato ISO: YYYY-MM-DDTHH:MM:SS)
        end_time: Data/hora de término (formato ISO: YYYY-MM-DDTHH:MM:SS)
        description: Descrição opcional do evento
        location: Local opcional do evento
        
    Returns:
        Mensagem de confirmação com link do evento ou mensagem de erro
    """
    try:
        service = get_calendar_service()
        
        event = {
            'summary': summary,
            'start': {
                'dateTime': start_time,
                'timeZone': 'America/Sao_Paulo',
            },
            'end': {
                'dateTime': end_time,
                'timeZone': 'America/Sao_Paulo',
            },
        }
        
        if description:
            event['description'] = description
        if location:
            event['location'] = location
        
        created_event = service.events().insert(calendarId='primary', body=event).execute()
        return f"✅ Evento criado com sucesso: {created_event.get('htmlLink')}"
    
    except HttpError as error:
        return f"Erro ao criar evento: {error}"




def main():
    print(list_calendar_events())
