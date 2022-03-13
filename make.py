from telegraph import Telegraph
from parser import Parser

from typing import List


def create(title, content) -> str:
    telegraph = Telegraph()
    telegraph.create_account(short_name='1337')

    response = telegraph.create_page(
        title,
        html_content=content
    )

    url = 'http://telegra.ph/{}'.format(response['path'])

    return url

def make(URL) -> str:
    parser: List = Parser(URL).run()

    title: str = parser[0]
    content: str = parser[1]

    article = create(title, content)
    return article


if __name__=='__main__':
    print( make('https://habr.com/ru/company/jugru/blog/649789/') )
