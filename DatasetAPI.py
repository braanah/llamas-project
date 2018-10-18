import ijson
import json
import time


class Dataset():

    def __init__(self):
        '''
        Expects a dataset directory with yelp_business_new.json and yelp_review_new.json
        '''
        BUSINESS_DATASET_NEW = "dataset/yelp_business_new.json"
        REVIEW_DATASET_NEW = "dataset/yelp_review_minified.json"
        self.BUSINESS_DATASET = "./dataset/yelp_academic_dataset_business.json"
        self.business_file = open(self.BUSINESS_DATASET)
        self.review_file = open(REVIEW_DATASET_NEW)

    def get_business_ids(self):
        return (json.loads(business)['business_id'] for business in self.business_file)
        # return (business['business_id'] for business in ijson.items(self.business_file, 'item'))

    def get_business(self, id):
        # i = json.load(self.business_file)
        # i = ijson.items(self.business_file, 'item')
        # for b in i:
        #     print(b)
        #     input()

        for js in open(self.BUSINESS_DATASET):
            business = json.loads(js)
            if business['business_id'] == id:
                return business
        # for business in ijson.items(self.business_file, 'item'):
        #     print(business)
        #     if business['business_id'] == id:
        #         return business

    def get_reviews(self, business_id):
        '''
        Returns generator
        Slower in traversal
        '''
        return (review for review in ijson.items(self.review_file, 'item') if review['business_id'] == business_id)

    def get_reviews_std(self, business_id):
        '''
        Returns a list
        Uses standard json module
        Big overhead to load data
        '''

        print("Loading")
        reviews = json.load(self.review_file)
        out = [review for review in reviews if review['business_id'] == business_id]
        print("Loaded")
        return out


if __name__ == '__main__':
    '''
    Testing the two functions in Dataset
    '''
    i = Dataset()

    j = i.get_business_ids().__next__()

    start = time.time()
    end = None
    for review in i.get_reviews_std(j):
        end = time.time()
        print(review)
        print("Time = " + str(end - start) + " seconds")
        input()
        start = time.time()
