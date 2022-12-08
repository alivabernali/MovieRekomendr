import nltk
import ssl
import string
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.ensemble import RandomForestClassifier
import sklearn
from sklearn.svm import SVC
from sklearn import model_selection
import pickle

# Maps feature vector as a dictionary
def find_feature(word_list, feature_vector):
    # Initialization
    feature = {}
    for x in feature_vector:
        feature[x] = x in word_list
    return feature

# Trains the model and store it at filepath
def train_model_default(filepath):
    print("Training Model...", flush = True)
    review_file = "data/IMDB Dataset.csv"
    file = open(review_file, "r")
    revs = file.readlines()[:2000]
    words = []
    reviews = []
    categories = []
    for review in revs:
        r = review.split(",")
        cat = r[len(r) - 1].strip()
        review_temp = ""
        for i in range(len(r) - 1):
            review_temp += r[i]
        review_temp = review_temp.translate(str.maketrans('', '', string.punctuation)).lower()
        reviews.append(review_temp)
        categories.append(cat)
        for word in review_temp.split(" "):
            words.append(word)
    all_words = nltk.FreqDist(words)
    print("Got Frequency Distribution...", flush = True)
    feature_vector = list(all_words)
    print("Making Feature sets...", flush = True)
    all_tr = [(find_feature(set(reviews[i].split(" ")), feature_vector),categories[i]) for i in range(len(reviews))]
    print("Splitting into Train and Test...", flush = True)
    train_set,test_set = model_selection.train_test_split(all_tr,test_size = 0.25)
    # Linear Classifier
    print("Initializing Model...", flush = True)
    model = SklearnClassifier(SVC(kernel = "linear"))
    # # Random Forest Classifier
    # # model = SklearnClassifier(RandomForestClassifier(n_estimators=200, random_state=0))
    model.train(train_set)
    print("Classifying...", flush = True)
    accuracy = nltk.classify.accuracy(model, test_set)
    print('SVC Accuracy : {}'.format(accuracy))
    filename = filepath
    pickle.dump(model, open(filename, 'wb'))

# classifies a given review using a model
def classify_review(review, model, feature_vector):
    review = review.translate(str.maketrans('', '', string.punctuation)).lower()
    words = review.split(" ")
    result = model.classify(find_feature(words, feature_vector))
    return result

# Gives recommendations based on the output of the classifier
def show_recommendations(output):
    recs = []
    popular = []
    for movie in output:
        revs = output[movie]
        t = revs[0] + revs[1]
        if t > 5:
            recs.append((movie, revs[0] / t))
            popular.append((movie, t))
    sorted_recs = sorted(recs, key=lambda t: t[1], reverse = True) 
    sorted_pop = sorted(popular, key=lambda t: t[1], reverse = True)
    print("The Highly recommended movies are as follows: ")
    for m in sorted_recs:
        print(m[0])
    print("The Highly talked about movies are as follows: ")
    for m in sorted_pop:
        print(m[0])


# The driver code
# Change the value of model_path to None if you want to retrain the model, otherwise finalized_model_imdb.sav
if __name__ == "__main__":
    model_path = "finalized_model_imdb.sav"

    if model_path == None:
        model_path = "finalized_model_imdb.sav"
        train_model_default(model_path)
        
    model = pickle.load(open(model_path, 'rb'))
    review_file = "data/IMDB Dataset.csv"
    file = open(review_file, "r")
    revs = file.readlines()[:2000]
    words = []
    reviews = []
    categories = []
    for review in revs:
        r = review.split(",")
        cat = r[len(r) - 1].strip()
        review_temp = ""
        for i in range(len(r) - 1):
            review_temp += r[i]
        review_temp = review_temp.translate(str.maketrans('', '', string.punctuation)).lower()
        reviews.append(review_temp)
        categories.append(cat)
        for word in review_temp.split(" "):
            words.append(word)
    all_words = nltk.FreqDist(words)
    feature_vector = list(all_words)
    print("Classifying Reviews", flush = True)
    results = {}
    review_file = "data/test.csv"
    file = open(review_file, "r")
    reviews = file.readlines()
    for review in reviews:
        rev = review.strip().split(";")
        movie = rev[0]
        if movie not in results:
            results[movie] = [0,0]
        res = classify_review(rev[2], model, feature_vector)
        if res == "positive":
            results[movie][0] += 1
        else:
            results[movie][1] += 1
    show_recommendations(results)