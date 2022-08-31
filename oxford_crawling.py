import requests

from scrapy import Selector


def get_resp(eng_word):
    base_url = f"https://www.oxfordlearnersdictionaries.com/definition/english/{eng_word}?q={eng_word}"
    payload = {}
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }

    response = requests.request("GET", base_url, headers=headers, data=payload)

    return response


def oxford_crawling(word):
    us_pronun = None
    resp = get_resp(word)
    sel = Selector(resp)

    container_list = sel.xpath('//div[@class="webtop"]/span[@class="phonetics"]')

    for container in container_list:
        """
        uk = (
            container.xpath('div[@class="phons_br"]/span[@class="phon"]/text()')
            .get()
            .replace("/", "")
        )
        """
        us_pronun = (
            container.xpath('div[@class="phons_n_am"]/span[@class="phon"]/text()')
            .get()
            .replace("/", "")
        )

    return us_pronun


if __name__ == "__main__":
    word = "transformer"

    print(oxford_crawling(word))
