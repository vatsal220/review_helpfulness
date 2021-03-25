import numpy as np
import pickle

from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from utils.model_feature_utils import word_count, encode_main_cat

# API definition
app = Flask(__name__)
api = Api(app)

# Import model
model_path = './models/random_forest_clf_model_vg.sav'
rf_clf = pickle.load(open(model_path, 'rb'))

'''
    'price', 'overall', 'verified', 'valid_image', 'review_year', 'time_since_review',
    'review_wc', 'summary_wc', 'title_wc', 'description_count',
    'similar_item_present', 'recommended_item_counts', 'count_also_bought',
    'image_present', 'best_rank'
'''


class HelpfulReviewAPI(object):
    def __init__(
        main_cat,
        price, 
        overall, 
        verified, 
        valid_image,
        review_year, 
        time_since_review,
        review, summary, 
        title,
        description, 
        similar_item_present, 
        recommended_item_counts,
        count_also_bought,
        image_present, 
        best_rank
    ):
        self.main_cat = encode_main_cat(main_cat)
        self.price = [price]
        self.overall = [overall]
        self.verified = [verified]
        self.valid_image = [valid_image]
        self.review_year = [review_year]
        self.time_since_review = [time_since_review]
        self.review_wc = [word_count(review)]
        self.summary_wc = [word_count(summary)]
        self.title_wc = [word_count(title)]
        self.description_wc = [word_count(description)]
        self.similar_item_present = [similar_item_present]
        self.recommended_item_counts = [recommended_item_counts]
        self.count_also_bought = [count_also_bought]
        self.image_present = [image_present]
        self.best_rank = [best_rank]
        
    def get(self):
        features = (self.main_cat + self.price + self.overall + self.verified + 
            self.valid_image + self.review_year + self.time_since_review + self.review_wc + self.summary_wc + self.title_wc +
            self.description_wc + self.similar_item_present + self.recommended_item_counts + self.count_also_bought + 
            self.image_present + self.best_rank
                   )
            
        pred = rf_clf.predict([features])
        
        if pred[0] == 0:
            return "The review was not helpful"
        else:
            return "The review was helpful"
            
# api.add_resource(HelpfulReviewAPI, '/api/')

@app.route('/')
def predict():
    
    return render_template('index.html')




if __name__ == '__main__':
#     price = [100]
#     overall = [5]
#     verified = [1]
#     valid_image = [1]
#     review_year = [2018]
#     time_since_review = [3]
#     review = 'This was an amazing product which I would highly recommend'
#     review_wc = [word_count(review)]
#     summary = 'None Present'
#     summary_wc = [word_count(summary)]
#     title = 'Product of your life'
#     title_wc = [word_count(title)]
#     description = 'Not Available'
#     description_wc = [word_count(description)]
#     similar_item_present = [2]
#     recommended_item_counts = [4]
#     count_also_bought = [4]
#     image_present = [1]
#     best_rank = [3]
    
#     features = encode_main_cat('category_toys  games') + price + overall + verified + valid_image + review_year + time_since_review + review_wc + summary_wc + title_wc + description_wc + similar_item_present + recommended_item_counts + count_also_bought + image_present + best_rank
             
#     pred = rf_clf.predict([features])
#     if pred[0] == 0:
#         print("The review was not helpful")
#     else:
#         print("The review was helpful")
        
    app.run(debug = True)

