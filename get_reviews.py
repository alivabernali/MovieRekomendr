import requests
from bs4 import BeautifulSoup

# Gets reviews from a particular url into csv
def get_Reviews(url, csv):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    boxes = soup.find_all("div", {"class" : "film-detail-content"})
    f = open(csv, "a")
    for i in range(len(boxes)):
        rating = boxes[i].find_all("span")
        review = boxes[i].find_all("div", {"class" : "body-text -prose collapsible-text"})
        name = boxes[i].find_all("h2", {"class" : "headline-2 prettify"})
        if len(rating) == 4:
            continue
        else:
            rating = 2 * len(rating[0].text.strip())
        f.write(name[0].text.replace(";", ",") + ";" + str(rating) + ";" + review[0].text.replace(";", ",") + "\n")

# Driver code where csv_filepath is the url of file
if __name__ == "__main__":
    num_pages = 25
    csv_filepath = "data/test.csv"
    for i in range(1, num_pages + 1):
        get_Reviews(f"https://letterboxd.com/reviews/popular/this/week/page/{i}/", csv_filepath)