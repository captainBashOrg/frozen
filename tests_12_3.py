print("Простые Юнит-Тесты")
print("Методы Юнит-тестирования. Часть вторая")

import unittest
#import runner
import runner_and_tournament as rt


class TournamentTest(unittest.TestCase):

    is_frozen = True
    is_frozen4 = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

#    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runer_1 = rt.Runner('Усэйн', 10)
        self.runer_2 = rt.Runner('Ан д\'Рей', 9)
        self.runer_3 = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            joined = '{'
            print(f'\nТест: {test_key}')
            for key, value in test_value.items():
                ####print(f'\t{key}: {value.name}')
                joined = joined + str(key)
                joined = joined + (': ')
                joined = joined + value.name
                joined = joined + (', ')
            joined = joined[0:-2]
            joined = joined +  '}'

            print(joined )

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turn1(self):
        # list_test = [[self.runer_1, self.runer_3], [self.runer_2, self.runer_3],
        #              [self.runer_1, self.runer_2, self.runer_3]]
        turn_1 = rt.Tournament(90, self.runer_1, self.runer_3)
        result = turn_1.start()

        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn1'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turn2(self):
        turn_2 = rt.Tournament(90, self.runer_2, self.runer_3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Ник всегда должен быть последним')
        self.all_results['test_turn2'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turn3(self):
        turn_3 = rt.Tournament(90, self.runer_1, self.runer_2, self.runer_3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Ник всегда должен быть последним')
        self.all_results['test_turn3'] = result

    @unittest.skipIf(is_frozen4, 'Тесты в этом кейсе заморожены')
    def test_turn4(self):
        turn_4 = rt.Tournament(5, self.runer_1, self.runer_2, self.runer_3)
        result = turn_4.start()


        #print("Последний ",result[list(result.keys())[-1]]  )
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка!Ник всегда должен быть последним')
        self.all_results['test_turn4'] = result

    if __name__ == '__main__':
        unittest.main()