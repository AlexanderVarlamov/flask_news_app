import configparser

config = configparser.ConfigParser()
config.read('./settings.ini')

backend_port = config['BACKEND']['port']
backend_ip = config['BACKEND']['ip']
frontend_port = int(config['FRONTEND']['port'])
frontend_ip = config['FRONTEND']['ip']
api_name = config['BACKEND']['api_name']

