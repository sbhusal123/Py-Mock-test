from some_package.some_module import someClass
import unittest
from unittest import TestCase
from unittest.mock import patch

class TestSomeClass(TestCase):

    # @patch('some_package.some_module.someHelperClass')
    # def test_some_class_behaviour(self,shc):
    #     # shc is the mocked instance of someHelperClass
    #     shc.return_value.some_method.return_value = True
            

    #     # testing behaviour
    #     sc = someClass()
    #     self.assertEqual(sc.call(),"Returned True")

    def test_some_class_behaviour(self):
        # NOTE: always mock the path where the import is made
        # not where the module definition is placed.
        # if some_package.some_module.someHelperClass is imported at
        # mypackege.mymodile.someHelperClass patch the same
        with patch("some_package.some_module.someHelperClass") as mocked_obj:

            # alias.return_value.method_name.return_value = {mocked_value}
            mocked_obj.return_value.some_method.return_value = False
            

            # testing behaviour
            sc = someClass()
            self.assertEqual(sc.call(),"Returned False")


if __name__ == "__main__":
    unittest.main()
