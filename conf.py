import configparser

config = configparser.ConfigParser()
config.read('./settings.ini')

backend_port = config['BACKEND']['port']
backend_ip = config['BACKEND']['ip']
frontend_port = int(config['NETWORK']['port'])
api_name = config['BACKEND']['api_name']

