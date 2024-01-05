def individual_serializer(todo) -> dict:
    return {
        "id": str(todo['_id']),
        "name": todo['name'],
        "description": todo['description'],
        "complete": todo['complete']
    }

def list_serializer(todo_list) -> list:
    return[individual_serializer(item) for item in todo_list]