import newrunner
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = newrunner.Runner("Усейн", 10)
        self.runner2 = newrunner.Runner("Андрей", 9)
        self.runner3 = newrunner.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        result = {}
        for test_key, test_value in cls.all_results.items():
            print(f'Тест! {test_key}')
            for key, value in test_value.items():
                result[key] = str(value.name)
            print(result)

    def test_run1(self):
        run_1 = newrunner.Tournament(90, self.runner1, self.runner3)
        finish = run_1.start()
        self.all_results[f'Результат забега бегунов: {self.runner1} и {self.runner3}'] = finish
        self.assertTrue(list(finish.values())[-1].name == str(self.runner3))

    def test_run2(self):
        run_2 = newrunner.Tournament(90, self.runner2, self.runner3)
        finish = run_2.start()
        self.all_results[f'Результат забега бегунов: {self.runner2} и {self.runner3}'] = finish
        self.assertTrue(list(finish.values())[-1].name == str(self.runner3))

    def test_run3(self):
        run_3 = newrunner.Tournament(90, self.runner1, self.runner2, self.runner3)
        finish = run_3.start()
        self.all_results[f'Результат забега бегунов: {self.runner1}, {self.runner2}, {self.runner3}'] = finish
        self.assertTrue(list(finish.values())[-1].name == str(self.runner3))


if __name__ == '__main__':
        unittest.main()