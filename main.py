import uvicorn
from fastapi import FastAPI, Body
from typing import Dict

from schemas import Person

app = FastAPI()


@app.get(
        '/me',
        tags=['special methods'],
        summary='Приветствие автора',
        response_description='Возврат приветствия'
)
def hello_author():
    return {"Hello": 'Anton'}


@app.post('/hello')
def greetings(person: Person = Body(...)) -> Dict[str, str]:
    if isinstance(person.surname, list):
        surnames = ' '.join(person.surname)
    else:
        surnames = person.surname
    result = ' '.join([person.name, surnames])
    result = result.title()
    if person.age is not None:
        result += ', ' + str(person.age)
    if person.education_level is not None:
        result += ', ' + person.education_level.lower()
    if person.is_staff:
        result += ', сотрудник'
    return {'Hello': result}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
