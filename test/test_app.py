import os
import sys
import unittest

sys.path.append(os.getcwd())

from app import app


class AppTests(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_check(self):
        response = self.app.get('/math/check')
        self.assertEqual(response.data, b'Congratulations! Your app works. :)')


    #Add the test_cases for various functionality here
    
    def test_addition_request_format1(self):
        response = self.app.post('/math/add')
        self.assertEqual(response.json['meta']['error'], 'The request must be a JSON of the following format: { data: { param1: <value>, param2: <value> } }')
    
    def test_addition_request_format2(self):
        response = self.app.post('/math/add', json={ "data": { "foo": "bar" } })
        self.assertEqual(response.json['meta']['error'], 'The request must be a JSON of the following format: { data: { param1: <value>, param2: <value> } }')

    def test_addition_request_format3(self):
        response = self.app.post('/math/add', json={ "data": {} })
        self.assertEqual(response.json['meta']['error'], 'The request must contain exactly two operands.')

    def test_addition_operand_format(self):
        response = self.app.post('/math/add', json={ "data": {
            "param1": "foo",
            "param2": "bar"
        } })
        self.assertEqual(response.json['meta']['error'], 'Operands must be integers/floats.')

    def test_addtion_correctness(self):
        response = self.app.post('/math/add', json={ "data": {
            "param1": 7,
            "param2": 3
        } })
        self.assertEqual(response.json['result'], 10)
        
    def test_multiplication_request_format1(self):
        response = self.app.post('/math/multiply')
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { param1: <value>, param2: <value> } }')

    def test_multiplication_request_format2(self):
        response = self.app.post('/math/multiply', json={"data": {"foo": "bar"}})
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { param1: <value>, param2: <value> } }')

    def test_multiplication_request_format3(self):
        response = self.app.post('/math/multiply', json={"data": {}})
        self.assertEqual(response.json['meta']['error'], 'The request must contain exactly two operands.')

    def test_multiplication_operand_format(self):
        response = self.app.post('/math/multiply', json={"data": {
            "param1": "foo",
            "param2": "bar"
        }})
        self.assertEqual(response.json['meta']['error'], 'Operands must be integers/floats.')

    def test_multiplication_correctness(self):
        response = self.app.post('/math/multiply', json={"data": {
            "param1": 4,
            "param2": 5
        }})
        self.assertEqual(response.json['result'], 20)

    def test_division_request_format1(self):
        response = self.app.post('/math/division')
        self.assertEqual(response.json['meta']['error'], 'The request must be a JSON of the following format: { data: { param1: <value>, ... param<n>: <value> } }')
    
    def test_division_request_format2(self):
        response = self.app.post('/math/division', json={ "data": { "foo": "bar" } })
        self.assertEqual(response.json['meta']['error'], 'The request must be a JSON of the following format: { data: { param1: <value>, ... param<n>: <value> } }')

    def test_division_request_format3(self):
        response = self.app.post('/math/division', json={ "data": {"param1":1} })
        self.assertEqual(response.json['meta']['error'], 'Division requires exactly 2 operands')
    
    def test_division_request_format4(self):
        response = self.app.post('/math/division', json={ "data": {"param1":1, "param2":2, "param3":3} })
        self.assertEqual(response.json['meta']['error'], 'Division requires exactly 2 operands')
    
    def test_division_operand_format1(self):
        response = self.app.post('/math/division', json={ "data": {
            "param1": "foo",
            "param2": "bar"
        } })
        self.assertEqual(response.json['meta']['error'], 'Operands should be a real number i.e. integer/float')
    
    def test_division_operand_format2(self):
        response = self.app.post('/math/division', json={ "data": {
            "param1": 1,
            "param2": 0
        } })
        self.assertEqual(response.json['meta']['error'], 'Division by zero is not allowed')
    
    def test_division_correctness(self):
        response = self.app.post('/math/division', json={ "data": {
            "param1": 3,
            "param2": 2,
        } })
        self.assertEqual(response.json['result'], 1.5)

    def test_exponentiation_request_format1(self):
        response = self.app.post('/math/exponentiation')
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { param1: <value>, param2: <value> } }')

    def test_exponentiation_request_format2(self):
        response = self.app.post('/math/exponentiation', json={"data": {"foo": "bar"}})
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { param1: <value>, param2: <value> } }')

    def test_exponentiation_request_format3(self):
        response = self.app.post('/math/exponentiation', json={"data": {}})
        self.assertEqual(response.json['meta']['error'], 'The request must contain exactly two operands.')

    def test_exponentiation_operand_format(self):
        response = self.app.post('/math/matrixaddition', json={"data": {
            "param1": "foo",
            "param2": "bar"
        }})
        self.assertEqual(response.json['meta']['error'], 'Operands must be integers/floats.')

    def test_exponentiation_correctness(self):
        response = self.app.post('/math/matrixaddition', json={"data": {
            "param1": 5,
            "param2": 3
        }})
        self.assertEqual(response.json['result'], 125)

    def test_matrix_addition_request_format1(self):
        response = self.app.post('/math/matrixaddition')
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { param1: <value>, ... param<n>: <value> } }')

    def test_matrix_addition_request_format2(self):
        response = self.app.post('/math/matrixaddition', json={"data": {"foo": "bar"}})
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { param1: <value>, ... param<n>: <value> } }')

    def test_matrix_addition_request_format3(self):
        response = self.app.post('/math/matrixaddition', json={"data": {}})
        self.assertEqual(response.json['meta']['error'], 'Matrix Addition requires atleast 2 operands')

    def test_matrix_addition_operand_format1(self):
        response = self.app.post('/math/matrixaddition', json={"data": {
            "param1": "foo",
            "param2": "bar"
        }})
        self.assertEqual(response.json['meta']['error'],
                         'Operands should be a matrix i.e list of lists of integers/floats')

    def test_matrix_addition_operand_format2(self):
        response = self.app.post('/math/matrixaddition', json={"data": {
            "param1": ["foo"],
            "param2": ["bar"]
        }})
        self.assertEqual(response.json['meta']['error'],
                         'Operands should be a matrix i.e list of lists of integers/floats')

    def test_matrix_addition_operand_format3(self):
        response = self.app.post('/math/matrixaddition', json={"data": {
            "param1": [["foo"]],
            "param2": [["bar"]]
        }})
        self.assertEqual(response.json['meta']['error'],
                         'Operands should be a matrix i.e list of lists of integers/floats')

    def test_matrix_addition_operand_format4(self):
        response = self.app.post('/math/matrixaddition', json={"data": {
            "param1": [[1], [2], [3]],
            "param2": [[1, 2, 3]]
        }})
        self.assertEqual(response.json['meta']['error'], 'Operands of matrix addition should be of same dimensions nxm')

    def test_matrix_addition_correctness(self):
        response = self.app.post('/math/matrixaddition', json={"data": {
            "param1": [
                [1, 1],
                [1, 1]
            ],
            "param2": [
                [2, 2],
                [2, 2]
            ],
            "param3": [
                [3, 3],
                [3, 3]
            ],
        }})
        self.assertEqual(response.json['result'], [
            [6, 6],
            [6, 6]
        ])


    # ----------------------------- Matrix Multiplication ----------------------------------------------
    def test_matrix_multiplication_request_format1(self):
        """
        Test if '/math/matrixmultiplication' request contains data in json format
        """
        response = self.app.post('/math/matrixmultiplication')

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'], 'The request must be a JSON of the following format: { '
                                                         'matrices: [matrix_1, matrix_2, ..., matrix_n] } Here matrix_1'
                                                         ', matrix_2, ..., matrix_n must be list of lists')

    def test_matrix_multiplication_request_format2(self):
        """
        Test if '/math/matrixmultiplication' request contains the correct format for key matrices
        """
        response = self.app.post('/math/matrixmultiplication', json={"matrices": {"foo": "bar"}})

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'], 'The request must be a JSON of the following format: { '
                                                         'matrices: [matrix_1, matrix_2, ..., matrix_n] } Here matrix_1'
                                                         ', matrix_2, ..., matrix_n must be list of lists')

    def test_matrix_multiplication_request_format3(self):
        """
        Test '/math/matrixmultiplication' request body should contain at least two operands in matrices
        """
        response = self.app.post('/math/matrixmultiplication', json={"matrices": []})

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'], 'At least two matrices are required for multiplication')

    def test_matrix_multiplication_operand_format1(self):
        """
        Test '/math/matrixmultiplication' for a matrix should be a list of lists and can't be empty
        """
        response = self.app.post('/math/matrixmultiplication', json={
            "matrices": [
                [],
                "foo"
            ]})

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'], "A matrix can't be empty or a matrix should be a list "
                                                         "of lists of integers/floats")

    def test_matrix_multiplication_operand_format2(self):
        """
        Test '/math/matrixmultiplication' for a matrix should be a list of lists and a matrix row can't be empty
        """
        response = self.app.post('/math/matrixmultiplication', json={
            "matrices": [
                [[1, 3], []],
                [[1, 2], [2, 4]]
            ]
        })

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'], "A matrix row can't be Empty or A matrix row should be a list")

    def test_matrix_multiplication_operand_format3(self):
        """
        Test '/math/matrixmultiplication' for a matrix row should contain either an int or float
        """
        response = self.app.post('/math/matrixmultiplication', json={
            "matrices": [
                [[1, 3], ["a"]],
                [[1, 2], [2, 4]]
            ]
        })

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'], "A matrix row should contain either an int or float")

    def test_matrix_multiplication_operand_format4(self):
        """
        Test '/math/matrixmultiplication' for matrix dimensions for multiplications
        """
        response = self.app.post('/math/matrixmultiplication', json={
            "matrices": [
                [[1, 3]],
                [[1, 2]]
            ]
        })

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'], "Matrix dimensions are not compatible for "
                                                         "multiplication! i.e. The columns of first matrix should"
                                                         " be equal to the rows of 2nd matrix and so on.")

    def test_matrix_multiplication_correctness(self):
        """
        Test '/math/matrixmultiplication' for correct output
        """
        response = self.app.post('/math/matrixmultiplication', json={
            "matrices": [
                [[1, 3]],
                [[1, 2], [3, 4]],
                [[6, 5], [4, 3]]
            ]
        })
        expected_result = [[116, 92]]

        # assert statements
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.json['result'], expected_result)

    # ------------------------------- SOLVE QUADRATIC EQUATION ----------------------------------------
    def test_quadratic_request_format1(self):
        """
        Test if '/math/quadraticequation' request contains data in json format
        """
        response = self.app.post('/math/quadraticequation')

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { a: <value>, b: <value>, '
                         'c: <value>} }')

    def test_quadratic_request_format2(self):
        """
        Test if '/math/quadraticequation' request contains the correct keys in data
        """
        response = self.app.post('/math/quadraticequation', json={"data": {"foo": "bar"}})

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { a: <value>, b: <value>, '
                         'c: <value>} }')

    def test_quadratic_operand_format(self):
        """
        Test if '/math/quadraticequation' request data keys are of correct format
        """
        response = self.app.post('/math/quadraticequation', json={"data": {
            "a": "2",
            "b": "1",
            "c": []
        }})

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'],
                         'Operands (a, b, c) should be either an int or a float')

    def test_quadratic_correctness(self):
        """
        Test if '/math/quadraticequation' request for correct output
        """
        response = self.app.post('/math/quadraticequation', json={"data": {
            "a": 1,
            "b": -3,
            "c": 2
        }})

        # assert statements
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.json['result'], {'x1': 2.0, 'x2': 1.0})
        self.assertEqual(response.json['meta']['detail'], 'Two real and distinct solutions as (b^2 - 4ac) > 0')

    def test_factorial_request_format1(self):
        response = self.app.post('/math/factorial')
        self.assertEqual(response.json['meta']['error'], 'The request must be a JSON of the following format: { data: { param1: <value> } }')
    
    def test_factorial_request_format2(self):
        response = self.app.post('/math/factorial', json={ "data": { "foo": "bar" } })
        self.assertEqual(response.json['meta']['error'], 'The request must be a JSON of the following format: { data: { param1: <value> } }')

    def test_factorial_request_format3(self):
        response = self.app.post('/math/factorial', json={ "data": {} })
        self.assertEqual(response.json['meta']['error'], 'The request must contain exactly one operand.')

    def test_factorial_operand_format(self):
        response = self.app.post('/math/factorial', json={ "data": {
            "param1": "foo"
        } })
        self.assertEqual(response.json['meta']['error'], 'Operand must be integer only.')

    def test_factorial_operand_format(self):
        response = self.app.post('/math/factorial', json={ "data": {
            "param1": -5
        } })
        self.assertEqual(response.json['meta']['error'], 'Operand must be positive integer only.')

    def test_factorial_correctness(self):
        response = self.app.post('/math/factorial', json={ "data": {
            "param1": 5
        } })
        self.assertEqual(response.json['result'], 120)

    def test_test_hcflcm_format1(self):
        """
        Test if '/math/hcflcm' request contains the correct keys in data
        """
        response = self.app.post('/math/hcflcm')

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'], 'The request must be a JSON of the following format: { data: { a: <value>, b: <value>} }')
        
    def test_test_hcflcm_format2(self):
        """
        Test if '/math/hcflcm' request contains the correct keys in data
        """
        response = self.app.post('/math/hcflcm', json={"data": {"foo": "bar"}})

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'], 'The request must be a JSON of the following format: { data: { a: <value>, b: <value>} }')
    
    def test_hcflcm_operand_format(self):
        """
        Test if '/math/hcflcm' request data keys are of correct format
        """
        response = self.app.post('/math/hcflcm', json={"data": {
            "a": "2",
            "b": 9.7
        }})

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'],
                         'Operands a, b should be either an int Only')

    def test_hcflcm_correctness1(self):
        """
        Test if '/math/hcflcm' request for correct output
        """
        response = self.app.post('/math/hcflcm', json={"data": {
            "a": 13,
            "b": 23
        }})

        # assert statements
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.json['result'], {'hcf': 1, 'lcm': 299})
        self.assertEqual(response.json['meta'], {})
    
    def test_hcflcm_correctness2(self):
        """
        Test if '/math/hcflcm' request for correct output
        """
        response = self.app.post('/math/hcflcm', json={"data": {
            "a": 20,
            "b": -8
        }})

        # assert statements
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.json['result'], {"hcf": 4, "lcm": 40})
        self.assertEqual(response.json['meta'], {})    

    def test_hcflcm_correctness2(self):
        """
        Test if '/math/hcflcm' request for correct output
        """
        response = self.app.post('/math/hcflcm', json={"data": {
            "a": -6,
            "b": -8
        }})

        # assert statements
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.json['result'], {"hcf": 2,"lcm": 24})
        self.assertEqual(response.json['meta'], {}) 

if __name__ == '__main__':
    unittest.main()