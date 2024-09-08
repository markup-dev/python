import unittest

import runner


class RunnerTest(unittest.TestCase):
	is_frozen = False

	@unittest.skipIf(is_frozen, 'ok')
	def test_walk(self):
		test_runner = runner.Runner('test')
		for i in range(10):
			test_runner.walk()
		self.assertEqual(test_runner.distance, 50)

	@unittest.skipIf(is_frozen, 'ok')
	def test_run(self):
		test_runner = runner.Runner('test')
		for i in range(10):
			test_runner.run()
		self.assertEqual(test_runner.distance, 100)

	@unittest.skipIf(is_frozen, 'ok')
	def test_challenge(self):
		test_runner = runner.Runner('test')
		test_runner2 = runner.Runner('test2')
		for i in range(10):
			test_runner.run()
			test_runner2.walk()
		self.assertNotEqual(test_runner.distance, test_runner2.distance)


if __name__ == '__main__':
	RunnerTest()
