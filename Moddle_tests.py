import unittest
import Moodle_locators as locators
import Moodle_methods as methods

class MoodleAppTestPositiveTestCase(unittest.TestCase):
      @staticmethod
      def test_create_new_user():
          methods.setUp()
          methods.log_in(locators.admin_username, locators.admin_password)  # LOGIN AS ADMIN
          methods.create_new_user()
          methods.log_out()
          methods.log_in(locators.new_username, locators.new_password)
          methods.check_new_user_can_login()
          methods.logger('created')
          methods.log_out()
          methods.log_in(locators.admin_username, locators.admin_password)
          methods.delete_newuser()
          methods.log_out()
          methods.tearDown()