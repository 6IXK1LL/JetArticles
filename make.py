from telegraph import Telegraph
from parser import Parser


def make(URL):
    parser = Parser(URL).run()

    title = parser[0]
    content = parser[1]

    telegraph = Telegraph()
    telegraph.create_account(short_name='1337')

    response = telegraph.create_page(
        title,
        html_content=content
    )

    url = 'http://telegra.ph/{}'.format(response['path'])

    return url