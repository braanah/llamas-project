import ijson
import time


class Dataset():

    def __init__(self):
        '''
        Expects a dataset directory with yelp_business_new.json and yelp_review_new.json
        '''
        BUSINESS_DATASET_NEW = "dataset/yelp_business_new.json"
        REVIEW_DATASET_NEW = "dataset/yelp_review_new.json"
        self.business_file = open(BUSINESS_DATASET_NEW)
        self.review_file = open(REVIEW_DATASET_NEW)

    def get_business_ids(self):
        return (business['business_id'] for business in ijson.items(self.business_file, 'item'))

    def get_reviews(self, business_id):
        return (review for review in ijson.items(self.review_file, 'item') if review['business_id'] == business_id)


if __name__ == '__main__':
    '''
    Testing the two functions in Dataset
    '''
    i = Dataset()

    j = i.get_business_ids().__next__()

    start = time.time()
    end = None
    for review in i.get_reviews(j):
        end = time.time()
        print(review)
        print("Time = " + str(end - start) + " seconds")
        input()
        start = time.time()
