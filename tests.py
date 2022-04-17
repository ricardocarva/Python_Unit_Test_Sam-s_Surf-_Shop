# Write your code below:
import unittest
import surfshop

class test_whatever(unittest.TestCase):
  def setUp(self):
    self.cart = surfshop.ShoppingCart()

  def test_add_one_surfboards(self):
    self.assertEqual(self.cart.add_surfboards(1), 'Successfully added 1 surfboard to cart!')

  def test_add_more_surfboards(self):
    #Creates the loop
    for num in range(2,5):
      #Uses the context to create parametized subtests
      with self.subTest(num):
        #instanciates the tested class in a variable
        message = self.cart.add_surfboards(num)
        #Get the expected result
        suffix = '' if num == 1 else 's'
        expected_result = f'Successfully added {num} surfboard{suffix} to cart!'
        #Assert if it is equal
        self.assertEqual(message, expected_result)
        #Instanciate the class for the next test. The setUp class will only run before the test is run, but for each subTest, we need a new instance
        self.cart = surfshop.ShoppingCart()

  @unittest.skip
  def test_add_surfboards_error(self):
    self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)
  # @unittest.expectedFailure
  def test_apply_discounts(self):
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)

unittest.main()