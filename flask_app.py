"""
version 
@author varlamov.a
@email varlamov.a@rt.ru
@date 03.07.2023
@time 16:28
"""
from flask import Flask

from views.routes import main_page, process_sources


def get_app() -> Flask:
    app = Flask("Get_latest_news")
    app.add_url_rule('/', view_func=main_page)
    app.add_url_rule('/process_sources', view_func=process_sources, methods=['POST'])
    return app
