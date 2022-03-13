from bs4 import BeautifulSoup
import requests

from typing import List


class Parser:
    def __init__(self, url) -> None:
        self.url = url
        self.page = requests.get(url)
        self.html_code = self.page.text
        self.soup = BeautifulSoup(self.html_code, 'lxml')
    
        self.getArticle()
        self.getText()
    
    def getArticle(self) -> List[str]:
        self.post = self.soup.find("article",
            class_="tm-article-presenter__content tm-article-presenter__content_narrow")
        self.title = self.post.find("h1", class_="tm-article-snippet__title tm-article-snippet__title_h1").text
        self.text = self.post.find_all(['p', 'li', 'b','h3', 'h4'])

        return [self.text, self.title]

    def getText(self) -> str:
        self.article_text = ''
        for i in self.getArticle()[0]:
            self.article_text += f'{i.text}\n'

        return self.article_text

    def run(self) -> List[str]:
        return [self.getArticle()[1], self.getText()]


if __name__=='__main__':
    URL = "https://habr.com/ru/company/jugru/blog/649789/"

    parser = Parser(URL).run()
    
    title = parser[0]
    content = parser[1]
    
    print(title + '\n\n' + content)