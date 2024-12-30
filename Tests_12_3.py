import runner
import unittest
import newrunner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipUnless(is_frozen, "Тест пройден")
    def test_walk(self):
        RW = runner.Runner("Human")
        for i in range(10):
            RW.walk()
        self.assertEqual(RW.distance, 50)

    @unittest.skipUnless(is_frozen, "Тест пройден")
    def test_run(self):
        RR = runner.Runner("guepard")
        for i in range(10):
            RR.run()
        self.assertEqual(RR.distance, 100)

    @unittest.skipUnless(is_frozen, "Тест пройден")
    def test_challenge(self):
        RW_ = runner.Runner("scooter")
        RR_ = runner.Runner("bike")
        for i in range(10):
            RR_.run()
            RW_.walk()
        self.assertNotEqual(RW_.distance, RR_.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

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

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run1(self):
        run_1 = newrunner.Tournament(90, self.runner1, self.runner3)
        finish = run_1.start()
        self.all_results[f'Результат забега бегунов: {self.runner1} и {self.runner3}'] = finish
        self.assertTrue(list(finish.values())[-1].name == str(self.runner3))

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run2(self):
        run_2 = newrunner.Tournament(90, self.runner2, self.runner3)
        finish = run_2.start()
        self.all_results[f'Результат забега бегунов: {self.runner2} и {self.runner3}'] = finish
        self.assertTrue(list(finish.values())[-1].name == str(self.runner3))

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run3(self):
        run_3 = newrunner.Tournament(90, self.runner1, self.runner2, self.runner3)
        finish = run_3.start()
        self.all_results[f'Результат забега бегунов: {self.runner1}, {self.runner2}, {self.runner3}'] = finish
        self.assertTrue(list(finish.values())[-1].name == str(self.runner3))


if __name__ == '__main__':
        unittest.main()