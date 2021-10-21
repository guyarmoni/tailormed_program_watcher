from urllib.request import urlopen
from bs4 import BeautifulSoup as Soup
from assistance_program import AssistanceProgram
from consts import FUND_URLS
import query_utils as q


def fill_table(connection):
    for fund in FUND_URLS:
        program = get_fund_details(FUND_URLS.get(fund))
        # todo - error handling needed for url opening
        q.add_fund_to_db(connection, program)


def update_table(connection):
    for fund in FUND_URLS:
        program = get_fund_details(FUND_URLS.get(fund))
        # todo - error handling needed for url opening
        q.update_fund_in_db(connection, program)


def get_fund_details(fund_url):
    fund_page_soup = get_page_parsed_html(fund_url)

    details = fund_page_soup.find_all("div", {"class": "details"})
    details_separate = details[0].find_all("div", {"class": "row"})

    # extracting relevant information from web page
    program_name = fund_page_soup.h1.text.split()[0]
    status = details_separate[0].div.text.split()[1]
    grant_amount = details_separate[1].text.split()[3]
    eligible_treatments = get_fund_treatments(fund_page_soup)

    # creates an object that represents the assistance program and holds its details
    fund = AssistanceProgram(program_name, status, grant_amount, eligible_treatments)

    return fund


def get_page_parsed_html(url):
    # connecting and getting templates
    url_client = urlopen(url)
    page_html = url_client.read()
    url_client.close()

    # return parsed page
    return Soup(page_html, "html.parser")


# helper function for extracting fund treatments
def get_fund_treatments(fund_page_soup):
    treatments = fund_page_soup.find_all("div", {"class": "treatments"})
    treatments = treatments[0]
    return list(map(lambda li: li.text, treatments.find_all("li")))


