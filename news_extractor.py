#!/usr/bin/env python3

import requests
import re
from readability import Document

class NewsArticle:
    def __init__(self, title, body, raw):
        self.title = title
        self.body = body
        self.raw = raw

def get_webpage_data(url):
    response = requests.get(url)
    doc = Document(response.text)
    return doc

def remove_html_artifacts(text):
    removed_tags_text = re.sub(r"<(.*?>)", "", text)
    removed_extraneous_html_entities = re.sub(r"&#(.*?;)", "", removed_tags_text)
    return removed_extraneous_html_entities

def remove_repeated_whitespace(text):
    removed_extra_tabs = re.sub("\t\t+", "\t", text)
    removed_empty_lines = "".join([line.strip() + "\n" for line in removed_extra_tabs.split("\n") if line.strip() != ''])
    return removed_empty_lines

def clean_up_document_body(doc):
    initial_text = doc.summary()
    removed_html_text = remove_html_artifacts(initial_text)
    removed_extra_whitespace_text = remove_repeated_whitespace(removed_html_text)
    return removed_extra_whitespace_text

def article_from_url(url):
    try:
        raw = get_webpage_data(url)
        body = clean_up_document_body(raw)
        return NewsArticle(raw.title(), body, raw.input)
    except Exception as e:
        print("Could not extract news data from url! Probably a bad URL!")
        print(e)
        return None

