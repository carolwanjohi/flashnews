import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test class to test behaviours of the Source class

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        self.news_source = Source('abc-news-au','ABC News (AU)', 'Most trusted source of local, national and world news. Comprehensive, independent, in-depth analysis, the latest business, sport, weather and more.')

    def test_instance(self):
        '''
        Test case to check if self.new_source is an instance of Source
        '''
        self.assertTrue( isinstance(self.news_source,Source))
