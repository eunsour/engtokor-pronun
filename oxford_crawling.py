import requests

from scrapy import Selector

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}

def oxford_crawling(word):
    base_url = (
        f"https://www.oxfordlearnersdictionaries.com/definition/english/{word}?q={word}"
    )
    resp = requests.get(base_url, headers=headers)
    sel = Selector(resp)

    us = None
    container_list = sel.xpath('//div[@class="webtop"]/span[@class="phonetics"]')

    for container in container_list:
        """
        uk = (
            container.xpath('div[@class="phons_br"]/span[@class="phon"]/text()')
            .get()
            .replace("/", "")
        )
        """
        us = (
            container.xpath('div[@class="phons_n_am"]/span[@class="phon"]/text()')
            .get()
            .replace("/", "")
        )

    return us


if __name__ == "__main__":
    word = "transformer"
    print(oxford_crawling(word=word))
