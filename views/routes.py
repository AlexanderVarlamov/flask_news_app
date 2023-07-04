"""
version 
@author varlamov.a
@email varlamov.a@rt.ru
@date 03.07.2023
@time 16:31
"""
from flask import render_template, request
from conf import *
import requests

from controllers.req_processors import get_raw_news_json


def main_page():
    html_page = render_template('index.html')
    return html_page


def process_sources():
    key = request.form['list_of_sources']
    return get_raw_news_json(key)
