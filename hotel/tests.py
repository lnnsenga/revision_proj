from django.test import TestCase

# Create your tests here.


# create a test 
# run locally
# create file :.github file in workflow folder. write action code in the github file to run the test.

class HotelTest(TestCase):

    def setUp(self):
        pass

    def test_app_pass(self):
        response = 2+2
        self.assertEqual(response,4)

    def test_app_fail(self):
        response = 2+1
        self.assertNotEqual(response,4)
        

        
