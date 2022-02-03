import unittest
import config
import json
from AzureSearch import az_search

class TestSearchMethods(unittest.TestCase):
    def setUp(self):
        self.az_client = az_search.AzSearchQuery(config.AZURE_SEARCH_SERVICE_NAME, config.AZURE_SEARCH_INDEX_NAME, config.AZURE_SEARCH_API_KEY)

    # Boolean searches
    # Uses AND OR NOT
    def test_boolean_queries(self):
        results = self.az_client.client.search(
            '(atlanta AND collecting) NOT lastName:ali NOT lastName:anderson', 
            order_by='lastName', 
            query_type='full', 
            search_mode='all', 
            include_total_count=True, 
            filter='',
            top=100, 
            facets=['lastName', 'city'], 
            select=['firstName', 'lastName', 'city', 'hobbies'])

        self.write_results(results)

    # Wildcard searches
    # Uses term* to find begins with or /.*term/ to find ends with
    def test_wildcard_queries(self):
        results = self.az_client.client.search(
            'city:/.*vil*./', 
            order_by='lastName', 
            query_type='full', 
            search_mode='all', 
            include_total_count=True, 
            filter="",
            top=100, 
            facets=['lastName', 'city'], 
            select=['firstName', 'lastName', 'city', 'hobbies'])

        self.write_results(results)

    # Fuzzy searches
    # Uses term~ to find a fuzzy match
    def test_fuzzy_queries(self):
        results = self.az_client.client.search(
            'firstName:dominek~ AND hobbies:gardening', 
            order_by='city', 
            query_type='full', 
            search_mode='all', 
            include_total_count=True, 
            filter="",
            top=100, 
            facets=['lastName', 'city'], 
            select=['firstName', 'lastName', 'city', 'hobbies'])
        self.write_results(results)

    def write_results(self, results):
        print('Total Result Count: {}'.format(results.get_count()))
        for result in results:
            print('First Name: {}; Last Name: {}; City: {}, Hobbies: {}'.format(result['firstName'], result['lastName'], result['city'], result['hobbies']))

if __name__ == '__main__':
    unittest.main()