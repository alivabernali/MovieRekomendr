# MovieRekomendr :movie_camera:
Chirag Gupta `@chiragg4` | Shreyah Prasad `@sprasa20` | Aliva Panigrahi `@alivabp2`
## Overview
MovieRekomendr is a personable movie recomender system based on popular [Letterboxd](https://letterboxd.com/) user reviews. Letterboxd is a social film review website, where users can come together to rank movies and leave short or detailed reviews. Using sentiment analysis on the site's most recent reviews, MovieRekomendr provides users with best and worst ranked lists of the best films that have been reviewed on LetterBoxd. 

## Tools & Technologies
To implement MovieRekomendr, we made use of various libraries. We primarily used [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/), a Python library for pulling data from HTML files. This provided us with a bank of text movie reviews and numerical ratings. To conduct sentiment analysis on the text reviews we used [NLTK](https://www.nltk.org/), a Python suite of libraries to assist in NLP. The NLTK movie review corpus was a useful addition for our implementation. Last but not least, we used [Scikit-Learn](https://scikit-learn.org/stable/) to test different classifiers, including linear support vector machine and random forest. We are also using a bank of [iMDB](https://www.imdb.com/) (a similar film review site) reviews to further train the model.

## Code Design
Our code is divided into two main Python files: </br>
`get_reviews.py`: scrapes all movie reviews and rankings and outputs as a `.csv` </br>
`model.py`: trains model using most optimal classifier AND ranks movies based on sentiment analysis </br>
```mermaid
graph LR
A(get_reviews.py)-->|output| B(test.csv)-->|input| C(model.py)-->|input| D(ranked list: most popular </br>ranked list: most discussed)
```

## Code Installation & Instructions
1. Clone/download this repository, and ensure you have successfully downloaded the following files: </br>
    `get_reviews.py` </br>
    `model.py` </br>
    `finalized_model.sav` </br>
