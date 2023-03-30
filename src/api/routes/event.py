from datetime import datetime
from flask import abort, make_response

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H;%M:%S"))

EVENT = {
    "1000": {
        "event_title": "Anivesário da Vovó",
        "event_date": "2023-04-13",
        "event_description": "Aniversário muito legal!",
        "event_status": "0",
        "user_id": "1000",
        "timestamp": get_timestamp(),
    },
    "2000": {
        "event_title": "Prova",
        "event_date": "2022-01-10",
        "event_description": "Prova de Matemática",
        "event_status": "1",
        "user_id": "1000",
        "timestamp": get_timestamp(),
    },
    "3000": {
        "event_title": "Anivesário da Vovó",
        "event_date": "2020-12-22",
        "event_description": "Aula de Geografia",
        "event_status": "1",
        "user_id": "2000",
        "timestamp": get_timestamp(),
    },
    "4000": {
        "event_title": "Festa na piscina",
        "event_date": "2024-01-01",
        "event_description": "Festa na piscina na casa do Caio",
        "event_status": "0",
        "user_id": "4000",
        "timestamp": get_timestamp(),
    },
}

def read_all(user_id):
    events = []
    for event in EVENT.values():
        if event["user_id"] == user_id:
            events.append(event)

    return events

def create(event, user_id):
    event_id = event.get("event_id")
    event_title = event.get("event_title", "")
    event_date = event.get("event_date")
    event_description = event.get("event_description")

    if event_id and event_id not in EVENT:
        EVENT[event_id] = {
            "event_id": event_id,
            "event_title": event_title,
            "event_date": event_date,
            "event_description": event_description,
            "event_status": 0,
            "user_id": user_id,
            "timestamp": get_timestamp(),
        }
        return EVENT[event_id], 201
    else:
        abort(
            406,
            f"Event with title {event_id} already exists",
        )

def update(event_id, event):
    if event_id in EVENT:
        EVENT[event_id]["event_title"] = event.get("user_title", EVENT[event_id]["event_title"])
        EVENT[event_id]["event_date"] = event.get("user_date", EVENT[event_id]["user_date"])
        EVENT[event_id]["event_description"] = event.get("user_title", EVENT[event_id]["event_title"])
        EVENT[event_id]["event_status"] = event.get("user_title", EVENT[event_id]["event_title"])
        EVENT[event_id]["user_id"] = event.get("user_id", EVENT[event_id]["event_title"])
        EVENT[event_id]["timestamp"] = get_timestamp()
        return EVENT[event_id]
    else:
        abort(
            404,
            f"Person with ID {event_id} not found"
        )

def read_one( event_id):
    if event_id in EVENT:
        return EVENT[event_id]
    else:
        abort(
            404,
            f"Event with ID {event_id} not found",
        )

def delete(user_id, event_id):
    if event_id in EVENT:
        del EVENT[event_id]
        return make_response(
            f"{event_id} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Person with ID {event_id} not found"
        )