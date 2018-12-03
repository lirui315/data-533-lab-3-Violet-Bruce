
# coding: utf-8

# In[5]:


import unittest
import testsuite.unittests.TestBirthdateMonth
import testsuite.unittests.TestBirthdateYear


# In[6]:


def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestBirthdateMonth))
    suite.addTest(unittest.makeSuite(TestBirthdateYear))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()

