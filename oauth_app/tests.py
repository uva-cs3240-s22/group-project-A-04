from django.test import TestCase

# Create your tests here.

# manage.py test looks for tests in the app
# finds subclass of the TestCase class
# creates special database for testing
# looks for test methods— one whose names begin with test
# runs the functions below, returns results of tests through various asserts

# Good rules-of-thumb include having:
# a separate TestClass for each model or view
# a separate test method for each set of conditions you want to test
# test method names that describe their function from the tutorial

# Remember: no code can be pushed to main without tests!

class SampleTests(TestCase):

    # sample test that always returns true
    def test_true(self):
        """
        This sample test always returns True.
        """
        self.assertTrue(True, "Alright, who changed this assertion to False out of spite?")