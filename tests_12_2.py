import unittest
import runner_and_tournament as run


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.first_runner = run.Runner('Усэйн', 10)
        self.second_runner = run.Runner('Андрей', 9)
        self.third_runner = run.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print(*[{k: v for k, v in dict_.items()} for dict_ in cls.all_results], sep='\n')

    def test_first_tur(self):
        first_tur = run.Tournament(90,self.first_runner, self.third_runner)
        result = first_tur.start()
        self.all_results.append(result)
        self.assertTrue(result[2] == self.third_runner)

    def test_second_tur(self):
        tournament = run.Tournament(90, self.second_runner, self.third_runner)
        result = tournament.start()
        self.all_results.append(result)
        self.assertTrue(result[2] == self.third_runner)

    def test_third_tur(self):
        tournament = run.Tournament(90, self.first_runner, self.second_runner, self.third_runner)
        result = tournament.start()
        self.all_results.append(result)
        self.assertTrue(result[3] == self.third_runner)


if __name__ == "__main__":
    unittest.main()

