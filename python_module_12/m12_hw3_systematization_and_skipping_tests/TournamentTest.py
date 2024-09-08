import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
	is_frozen = True

	@classmethod
	def setUpClass(cls):
		cls.all_results = {}

	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
	def setUp(self):
		self.usain = Runner("Усэйн", 10)
		self.andrey = Runner("Андрей", 9)
		self.nik = Runner("Ник", 3)

	@classmethod
	def tearDownClass(cls):
		print(*[value for value in cls.all_results.values()], sep='\n')

	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
	def test_usain_and_nik(self):
		tournament = Tournament(90, self.usain, self.nik)
		result = tournament.start()
		self.all_results[0] = {key: value.name for key, value in result.items()}
		self.assertTrue(result[max(result.keys())].name == 'Ник')

	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
	def test_andrey_and_nik(self):
		tournament = Tournament(90, self.andrey, self.nik)
		result = tournament.start()
		self.all_results[1] = {key: value.name for key, value in result.items()}
		self.assertTrue(result[max(result.keys())].name == 'Ник')

	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
	def test_usain_andrey_and_nik(self):
		tournament = Tournament(90, self.usain, self.andrey, self.nik)
		result = tournament.start()
		self.all_results[2] = {key: value.name for key, value in result.items()}
		self.assertTrue(result[max(result.keys())].name == 'Ник')


if __name__ == '__main__':
	TournamentTest()
