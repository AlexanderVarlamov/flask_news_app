"""
version 
@author varlamov.a
@email varlamov.a@rt.ru
@date 04.07.2023
@time 12:30
"""
import requests

from conf import backend_ip, backend_port, api_name, frontend_port, frontend_ip
from jinja2 import Environment, FileSystemLoader


def get_news_url(title, url):
    return f'<a href="{url}">{title}</a>'


def get_raw_news_json(key: str):
    url = 'http://' + backend_ip + ':' + backend_port + api_name
    news = requests.post(url, json={"sources": [key]})
    raw_json: dict = news.json()['news']
    print(raw_json)
    links_json = {}
    for inner_dict in raw_json:
        for key in inner_dict.keys():
            one_source_news = inner_dict[key]
            links = [get_news_url(title, url) for title, url in one_source_news]
            links_json.update({key: links})

    print(links_json)
    return links_json


def render_webpage(links_json: dict) -> str:
    context = {"sources": links_json, "frontend_ip": frontend_ip, "frontend_port": frontend_port}
    env = Environment(loader=FileSystemLoader("templates/"))
    template = env.get_template("news.template")
    results = template.render(context)
    print(results)
    return results
