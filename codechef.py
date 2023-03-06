from bs4 import BeautifulSoup
import requests
import re

def codechef_ratings(username):
    try:
        url = f"https://www.codechef.com/users/{username}"
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html5lib")

    # to find rating
        rating = soup.find("div", attrs={'class': "rating-number"}).contents[0]

    # find name
        name = soup.find("h1", attrs={"class": "h2-style"}).contents[0]

    # to find correct section
        section_class = soup.find("section", attrs={'class': "rating-data-section problems-solved"})

    # to find correct division
        div = section_class.findChildren("div", recursive=False)[0]

    # to find correct element
        h5 = div.findChild("h5", recursive=False).contents[0]

        problems_solved = re.findall("\d+", h5)[0]

        ans = [name,rating,problems_solved]
        print("Name:",name)
        print("Rating:", rating)
        print("Problems Solved:", problems_solved)
        return ans
    except:
        print("Invalid Username")
        return []