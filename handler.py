import requests

def transfer(event, context):
    urlBank = event['urlBank']
    transfer = event['transfer']
    amount = event['amount']

    # Obtener el token de acceso del servicio de autenticación
    token = get_access_token()
    if token is not None:
        response = make_bank_api_call(urlBank, token, transfer, amount)
        if response.status_code == 200:
            return {
                'statusCode': 200,
                'body': 'Solicitud completada con éxito'
            }
        else:
            return {
                'statusCode': 400,
                'body': 'No se proporcionaron URLs de conexión'
            }
    else:
        return {
            'statusCode': 400,
            'body': 'No se pudo obtener el token de acceso'
        }


def get_access_token():
    auth_endpoint = 'https://auth-service.com/token'
    client_id = 'pichinchabank'
    client_secret = '878****'

    # Realizar la solicitud de token de acceso utilizando OAuth 2.0
    auth_data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    auth_response = requests.post(auth_endpoint, data=auth_data)
    if auth_response.status_code == 200:
        token = auth_response.json().get('access_token')
        return token
    else:
        return None


def make_bank_api_call(url, token, transfer, amount):
    # Realizar la llamada a la API bancaria utilizando el token de acceso, transfer y amount
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'transfer': transfer, 'amount': amount}
    response = requests.post(url, headers=headers, json=payload)
    return response
