import unittest
from app import app

def direct_new_comment(self, comment):
    return self.app.post('/', comment = comment, follow_redirects=True)



class TestInvalidInputs(unittest.TestCase):
    def test_new_comment(self):
        comment = 'ipsum fore culpa quorum noster ipsum multos cillum eram nulla sint multos quae sint ipsum minim aliqua amet nulla aliqua magna sunt duis ipsum malis cillum dolor tamen nisi minim quae fore esse irure aute quis sint quis illum eram illum export irure eram quorum esse labore culpa magna legam illum quorum fore quis  quis illum aliqua illum illum fore malis illum tempor culpa noster fugiat export  multos aliqua dolore duis esse veniam elit esse nulla multos labore illum tempor'
        rv = self.direct_new_comment(comment)
        assert b'Error' in rv.data


if __name__ == '__main__':
    unittest.main()
