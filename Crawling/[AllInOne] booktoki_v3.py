# coding: utf8
# title: Add Booktoki.com
# author: github.com/STR-HK/hdl-stubs
# comment: Created at 2023/10/23

from io import BytesIO
from utils import Soup, LazyUrl, Downloader, clean_title
import clf2


class Image(object):

    def __init__(self, src, name):
        ext = ".{}".format(src.split(".")[-1])
        if ext.lower()[1:] not in ["jpg", "jpeg", "bmp", "png", "gif", "webm", "webp"]:
            ext = ".jpg"
        self.filename = f"{name}{ext}"
        self.url = LazyUrl(src, lambda _: src, self)


@Downloader.register
class Downloader_Booktoki(Downloader):
    type = "booktoki"
    URLS = [r"regex:booktoki[0-9]*\.com"]
    MAX_CORE = 4
    icon = "https://manatoki.net/img/book/favicon-32x32.png"

    def read(self):
        soup = get_soup(self.url)
        artist = self.get_artist(soup)
        base_title = f"[{artist}] {self.get_title(soup)}"
        self.artist = artist

        img_candidate = soup.find("div", class_="view-img").find("img")
        if img_candidate:
            src = img_candidate["src"]
            img = Image(src, "cover")
            self.urls.append(img.url)

        pages = get_pages_list(soup)
        self.print_(pages)
        
        # 각 소설 하나 당 파일 생성
        for n, page in enumerate(pages):
            # 각 소설의 제목을 정의
            self.title = f"{base_title} ({n+1}/{len(pages)})"
            self.print_(f"Reading: {n+1}/{len(pages)}")
            pagesoup = get_soup(page)
            
            # 콘텐츠 및 제목 가져오기
            @try_n(4)
            def content_getter():
                try:
                    return get_content(pagesoup)
                except:
                    return get_content(get_soup(page))
            
            @try_n(4)
            def title_getter():
                try:
                    return f"{n+1}화 | {get_page_title(pagesoup)}"
                except:
                    return f"{n+1}화 | {get_page_title(get_soup(page))}"

            # 개별 소설의 제목과 내용을 결합
            content_title = title_getter()
            content = content_getter().replace("&nbsp;", "\n")
            
            full_content = ""
            full_content += content_title
            full_content += "\n\n"
            full_content += content
            full_content += "\n\n\n終"

            # 개별 파일로 저장
            f = BytesIO()
            f.write(full_content.encode("UTF-8"))
            f.seek(0)

            # 각 소설에 대한 파일명 설정
            novel_title = clean_title(content_title)  # 파일명에 적합한 형식으로 정리
            self.filenames[f] = f"{novel_title}.txt"
            self.urls.append(f)

    def get_info_list(self, soup: Soup) -> list:
        """-> [title, [platform, tags, artist], summary]"""
        infobox = soup.find("div", class_="col-sm-8")
        contents = infobox.find_all("div", class_="view-content")
        details = contents[1].get_text().split("\xa0")
        for n, detail in enumerate(details):
            details[n] = detail.strip()
        return [
            contents[0].get_text().strip(),
            details,
            contents[2].get_text().strip(),
        ]

    def get_title(self, soup: Soup):
        return clean_title(self.get_info_list(soup)[0])

    def get_artist(self, soup: Soup):
        return clean_title(self.get_info_list(soup)[1][2])


def get_soup(url: str):
    return Soup(clf2.solve(url)["html"])


def get_pages_list(soup: Soup):
    pages_list = []
    list_body = soup.find("ul", class_="list-body")
    list_items = list_body.find_all("li", class_="list-item")
    for list_item in list_items:
        page = list_item.find("a")["href"]
        pages_list.append(page)
    pages_list.reverse()
    return pages_list


def get_content(soup: Soup):
    novel = soup.find("div", {"id": "novel_content"})
    ps = novel.find_all("p")
    if len(novel.find_all("p")) != 0:
        text = ""
        for n, p in enumerate(ps):
            if p.get_text() != "":
                text += p.get_text()
            else:
                text += "\n"
            text += "\n"
    else:
        text = novel.get_text()
    return text


def get_page_title(soup: Soup):
    full = soup.find("div", class_="toon-title")
    span = full.find("span").get_text()
    title = full.get_text().replace(span, "").strip()
    return clean_title(title)


log(f"Site Added: Booktoki")
