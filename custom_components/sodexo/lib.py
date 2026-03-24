"""LIB to Sodexo."""

from html.parser import HTMLParser


def parse_html(html: str) -> str:
    result = html
    index = result.find('<div class="valor_saldo">')
    result = result[index:]
    index = result.find("</div>")
    result = result[0:index]

    parser = HtmlParser()
    parser.feed(result)

    return parser.data


class HtmlParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.data = []
        self.capture = False

    def handle_starttag(self, tag, attrs):
        if tag in ("div"):
            self.capture = True

    def handle_endtag(self, tag):
        if tag in ("div"):
            self.capture = False

    def handle_data(self, data):
        if self.capture:
            self.data.append(data)


class AccountDetails:
    """Represents an Account Details."""

    def __init__(
        self, lunch_pass: float, eco_pass: float, gift_pass: float, updated: str
    ):
        self._lunch_pass = lunch_pass
        self._eco_pass = eco_pass
        self._gift_pass = gift_pass
        self._updated = updated

    @property
    def updated(self) -> str:
        return self._updated

    @property
    def lunch_pass_amount(self) -> float:
        return self._lunch_pass

    @property
    def eco_pass_amount(self) -> float:
        return self._eco_pass

    @property
    def gift_pass_amount(self) -> float:
        return self._gift_pass
