print("Простые Юнит-Тесты")
import unittest
import runner

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk (self):
        walk_man = runner.Runner(name="Johnny First")
        for  _ in range ( 10):
            walk_man.walk()

        self.assertEqual(walk_man.distance, 50)
        #print("Ходьба", walk_man.distance , self.assertEqual (walk_man.distance , 50 ))

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run (self):
        run_man = runner.Runner (name="Bille Secon")

        for _  in range (10):
            run_man.run()
        self.assertEqual(run_man.distance, 100)
        #print("Бег ",  run_man.distance ,  self.assertEqual ( run_man.distance , 100 ) )

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        r1= runner.Runner (name="Uno")
        r2 = runner.Runner(name="Due")

        for _ in range (10):
            r1.walk()
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)
        #print("Бегун vs пешеход", r1.distance, r2.distance, self.assertNotEqual (r1.distance,r2.distance) )

if __name__ == '__main__':
    unittest.main()

