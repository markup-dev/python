import unittest
from RunnerTest import RunnerTest
from TournamentTest import TournamentTest


test = unittest.TestSuite()
test.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
test.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test)
