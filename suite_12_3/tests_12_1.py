import runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        name_1 = runner.Runner(self)
        for i in range(10):
            self.distance = runner.Runner.walk(name_1)
        self.assertEqual(self.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        name_2 = runner.Runner(self)
        for i in range(10):
            self.distance = runner.Runner.run(name_2)
        self.assertEqual(self.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_name = ['name_1', 'name_2']
        for _ in test_name:
            names = runner.Runner(self)
            for i in range(10):
                self.distancew = runner.Runner.walk(names)
            names = runner.Runner(self)
            for i in range(10):
                self.distancer = runner.Runner.run(names)
            self.assertNotEqual(self.distancew, self.distancer)


if __name__ == "__main__":
    unittest.main()

