import unittest
import Tests_12_1
import Tests_12_2
import Tests_12_3


#Часть 1. TestSuit.

new_run_tourST = unittest.BaseTestSuite()
new_run_tourST.addTest(unittest.TestLoader().loadTestsFromTestCase(Tests_12_1.RunnerTest))
new_run_tourST.addTest(unittest.TestLoader().loadTestsFromTestCase(Tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(new_run_tourST)

#Часть 2. Пропуск тестов.

all_testsST = unittest.TestSuite()
all_testsST.addTest(unittest.TestLoader().loadTestsFromTestCase(Tests_12_3.RunnerTest))
all_testsST.addTest(unittest.TestLoader().loadTestsFromTestCase(Tests_12_3.TournamentTest))

runner_all = unittest.TextTestRunner(verbosity=2)
runner_all.run(all_testsST)

