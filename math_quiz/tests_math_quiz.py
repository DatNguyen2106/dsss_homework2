import unittest
from math_quiz import generateRandomNumbers, generateOperator, calculation

class TestMathGame(unittest.TestCase):

    def test_generateRandomNumbers(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generateRandomNumbers(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generateOperator(self):
        operators = {'+', '-', '*'}
        for _ in range(1000):  # Test a large number of random values
            random_operator = generateOperator()
            random_operator = function_B()
            # used in unit testing to check whether a string is contained in other or not
            self.assertIn(random_operator, operators)

    def test_calculation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 2, '+', '5 + 2', 7),
                (6, 2, '-', '6 - 2', 3),
                (5, 2, '*', '5 * 2', 10),
                (8, 4, '-', '8 - 4', 4),
                (3, 5, '*', '3 * 5', 15),
                (6, 4, '+', '6 + 4', 10),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                with self.subTest(num1=num1, num2=num2, operator=operator, expected_problem=expected_problem,
                    expected_answer=expected_answer):
                    result = calculation(num1, num2, operator)
                    # check function for operator '+' , '-', '*'
                    if operator in ['+', '-', '*']:
                        # check if the result from function C is correct or not by comparing with the expected_problem and expected_answer
                        self.assertEqual(result, (expected_problem, expected_answer),
                                        f"Expected: {expected_problem} = {expected_answer}, Got: {result[0]} = {result[1]}")
                    else:
                        # Handle unsupported operators
                        self.fail(f"Unsupported operator: {operator} in {expected_problem}")
                pass    

if __name__ == "__main__":
    unittest.main()


