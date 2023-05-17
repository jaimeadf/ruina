import sys
import requests
import yaml
import pytz
from argparse import ArgumentParser
from datetime import datetime, timedelta

BASE_URL = 'https://portal.ufsm.br/mobile/webservice'

def read_config() -> dict:
    with open('config.yaml', 'r') as document:
        return yaml.safe_load(document)

def is_weekday(date: datetime, weekday: str) -> bool:
    return date.strftime('%a') == weekday

def resolve_restaurant_id(restaurant: int):
    match restaurant:
        case 2:
            return 41
        case _:
            return restaurant

def login(username: str, password: str) -> str:
    response = requests.post(
        f'{BASE_URL}/generateToken',
        json={
            'appName': config['environment']['app'],
            'deviceId': config['environment']['device-id'],
            'deviceInfo': config['environment']['device-info'],
            'messageToken': config['environment']['message-token'],
            'login': username,
            'senha': password
        }
    )

    data = response.json()

    if data['error']:
        raise Exception(data['mensagem'])
    
    return data['token']

def schedule_meal(token: str, start: datetime, end: datetime, options: dict) -> list:
    payload = {
        'dataInicio': start.strftime('%Y-%m-%d %H:%M:%S'),
        'dataFim': end.strftime('%Y-%m-%d %H:%M:%S'),
        'idRestaurante': resolve_restaurant_id(options['restaurant']),
        'opcaoVegetariana': options['vegetarian'],
        'tiposRefeicoes': []
    }

    if options['coffee']:
        payload['tiposRefeicoes'].append({
            'descricao': 'Café',
            'error': False,
            'item': 1,
            'itemId': 1,
            'selecionado': True
        })

    if options['lunch']:
        payload['tiposRefeicoes'].append({
            'descricao': 'Almoço',
            'error': False,
            'item': 2,
            'itemId': 2,
            'selecionado': True
        })

    if options['dinner']:
        payload['tiposRefeicoes'].append({
            'descricao': 'Janta',
            'error': False,
            'item': 3,
            'itemId': 3,
            'selecionado': True
        })

    response = requests.post(
        f'{BASE_URL}/ru/agendaRefeicoes',
        json=payload,
        headers={
            'X-UFSM-Device-ID': config['environment']['device-id'],
            'X-UFSM-Access-Token': token
        }    
    )

    return response.json()

def find_schedules(date):
    filtered_schedules = filter(
        lambda s : is_weekday(date, s['weekday']),
        config['schedules']
    )

    return list(filtered_schedules)

parser = ArgumentParser(
    prog='agendator',
    description='Agenda automaticamente as refeições do RU da UFSM.'
)

parser.add_argument('-u --username', dest='username', help='Sua matrícula do aplicativo da UFSM.')
parser.add_argument('-p --password', dest='password', help='Sua senha do aplicativo da UFSM.')

args = parser.parse_args()

print('Lendo configuração...')
config = read_config()

try:
    print('Logando no aplicativo...')
    access_token = login(args.username, args.password)
except Exception as exception:
    print(f'Falha ao logar: {str(exception)}')
else:
    print('Procurando refeições para serem agendadas amanhã...')

    now = datetime.now(pytz.timezone('Brazil/East'))
    tomorrow = now + timedelta(1)

    tomorrow_schedules = find_schedules(tomorrow)
    failed = False

    for schedule in tomorrow_schedules:
        if is_weekday(tomorrow, schedule['weekday']):
            print(f"Agendando refeições para o RU {schedule['restaurant']}... ({schedule})")

            data = schedule_meal(access_token, tomorrow, tomorrow, schedule)

            for meal in data:
                date = datetime.strptime(meal['dataRefAgendada'], '%Y-%m-%d %H:%M:%S')
                message = (
                    f"{date.strftime('%d/%m/%Y')} - "
                    f"RU {schedule['restaurant']} ({meal['tipoRefeicao']}): "
                )

                if meal['sucesso']:
                    print(message + 'Agendado com sucesso.')
                else:
                    print('[Erro] ' + message + meal['impedimento'] + '.')
                    failed = True

    if len(tomorrow_schedules) == 0:
        print('Não há nenhuma refeição para ser agendada amanhã.')

    if failed:
        sys.exit(1)
