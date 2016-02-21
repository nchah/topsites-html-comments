#!/usr/bin/env python
""" Project Topsites HTML Comments - Collecting comments in HTML code for the Top 500 Sites
as ranked by Alexa.com """

from bs4 import BeautifulSoup, Comment
import click
import json
import requests


@click.command()
@click.option('--site', help='The HTTP web address')
def get_html_comments(site):
    """
    Used as a CLI tool. Usage in command line:
    $ python3 topsites-comments.py --site=http://facebook.com
    """
    try:
        r = requests.get(site)
        click.echo("Request Sent.")
        soup = BeautifulSoup(r.text, "html.parser")
        click.echo("Getting HTML comments.\n")
        comments = soup.find_all(text=lambda text: isinstance(text, Comment))
        comment_counter = 1
        total_comments = len(comments)
        for comment in comments:
            click.echo("COMMENT #{}/{}".format(comment_counter, total_comments) + ": " + comment + "\n")
            comment_counter += 1
    except:
        click.echo("Request Failed.")


def scrape_topsites(start_page=0, end_page=20):
    """
    Create a list of top websites ranked by Alexa.com
    :param start_page: int, set at 0 for the first page
    :param end_page: int, set at 20 for the last page
    :return site_list: list, contains top site URLs
    """
    alexa_url = "http://www.alexa.com/topsites/global;"  # Alexa Top 500 Sites
    site_list = []

    # Create list of all top sites
    for page in range(start_page, end_page):
        alexa_url_full = alexa_url + str(page)  # Each page has 25 results, values 0-19
        r = requests.get(alexa_url_full)
        soup = BeautifulSoup(r.text, "html.parser")
        sites = soup.find_all(class_="desc-paragraph")  # Get sites filtered by class

        for site in sites:
            site_url = site.get_text().strip()
            site_list.append(site_url)

    # Write site_list to file
    for site in site_list:
        with open("topsites.txt", "a") as write_file:
            write_file.write(site + "\n")

    return site_list


def scrape_html_comments(start=0, end=500):
    """
    Get all HTML comments on a top site
    :param start: int, start loop here
    :param end: int, end loop here
    :return comments_json: json, of top site and its HTML comments
    """
    with open("topsites.txt", "r") as read_file:
        site_list = read_file.readlines()
    site_list = site_list[start:end]
    site_num = start + 1  # Increment index by 1

    # Create JSON
    comments_json = {}

    # Sending requests
    for site in site_list:
        site = site.strip()

        # Create JSON file
        try:  # Exception handling in case file is not existing
            with open("topsites-comments.json", "r") as read_file:
                comments_json = json.load(read_file)
        except FileNotFoundError:
            with open("topsites-comments.json", "w") as write_file:
                json.dump(comments_json, write_file, ensure_ascii=False, indent=2)

        try:  # Exception handling in case site is unavailable
            r = requests.get("http://" + site)
            soup = BeautifulSoup(r.text, "html.parser")

            # Reference: crummy.com/software/BeautifulSoup/bs3/documentation.html#Removing elements
            comments = soup.find_all(text=lambda text: isinstance(text, Comment))
            comments_count = len(comments)
        except:
            comments = []
            comments_count = 0

        # Numbering adjustment so that JSON sort_keys is ordered properly, set at 4 digits
        site_num = str(site_num)
        num_len = 4
        if len(site_num) < num_len:
            site_num = "0" * (num_len - len(site_num)) + site_num

        # Create JSON object for each site
        comments_json[site_num] = {
            "site_rank": site_num,
            "site_url": site,
            "comments_count": comments_count,
            "comments": comments
        }

        print(site_num)
        site_num = int(site_num)
        site_num += 1  # Increment site number each iteration

        # Write comments_json to JSON file
        with open("topsites-comments.json", "w") as write_file:
            json.dump(comments_json, write_file, ensure_ascii=False, indent=2, sort_keys=True)

        comments_json = {}  # Empty the JSON object


def analyze_comments():
    """ Output txt file with all comments from JSON file formatted to be readable. """
    with open("topsites-comments.json", "r") as read_file:
        comments = json.load(read_file)

    num = 0

    for obj in comments:
        comment_counter = 1  # Set comment counter at 1 not 0

        site = comments[obj]["site_url"]
        with open("topsites-comments-extracted.txt", "a") as write_file:
            write_file.write("=====SITE: " + site + " START=====\n\n")

        for comment in comments[obj]["comments"]:
            extract = "SITE: " + site + ", COMMENT #" + str(comment_counter) + "\n" + comment + "\n\n"
            comment_counter += 1

            with open("topsites-comments-extracted.txt", "a") as write_file:
                write_file.write(extract)

        with open("topsites-comments-extracted.txt", "a") as write_file:
            write_file.write("=====SITE: " + site + " END=====\n\n")

        num += 1


if __name__ == '__main__':
    get_html_comments()
