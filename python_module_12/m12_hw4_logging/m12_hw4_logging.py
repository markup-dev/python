import logging
from unittest import TestCase
import runner

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_test.log', encoding='UTF-8',
										format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(TestCase):
	def test_walk(self):
		try:
			test_runner = runner.Runner('test', -1)
			for i in range(10):
				test_runner.walk()
			self.assertEqual(test_runner.distance, 50)
			logging.info('"test_walk" выполнен успешно')
		except ValueError:
			logging.warning('Неверная скорость для Runner', exc_info=True)

	def test_run(self):
		try:
			test_runner = runner.Runner([1, 2, 3])
			for i in range(10):
				test_runner.run()
			self.assertEqual(test_runner.distance, 100)
			logging.info('"test_run" выполнен успешно')
		except TypeError:
			logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

	def test_challenge(self):
		test_runner = runner.Runner('test')
		test_runner2 = runner.Runner('test2')
		for i in range(10):
			test_runner.run()
			test_runner2.walk()
		self.assertNotEqual(test_runner.distance, test_runner2.distance)


if __name__ == '__main__':
	RunnerTest()

