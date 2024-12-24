import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        RW = runner.Runner("Human")
        for i in range(10):
            RW.walk()
        self.assertEqual(RW.distance, 50)

    def test_run(self):
        RR = runner.Runner("guepard")
        for i in range(10):
            RR.run()
        self.assertEqual(RR.distance, 100)

    def test_challenge(self):
        RW_ = runner.Runner("scooter")
        RR_ = runner.Runner("bike")
        for i in range(10):
            RR_.run()
            RW_.walk()
        self.assertNotEqual(RW_.distance, RR_.distance)

if __name__ == "__main__":
    unittest.main()

