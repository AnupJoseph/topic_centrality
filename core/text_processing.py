from textacy.preprocessing.replace import replace_urls
import bs4


def processor(text):
    text = replace_urls(text, replace_with='')
    text = bs4.BeautifulSoup(text, 'html.parser').get_text()
    text = str(text)
    return text
