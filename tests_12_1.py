from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        self.runner_1 = Runner('1')
        for _ in range(10):
            self.runner_1.walk()

        self.assertEqual(self.runner_1.distance, 50)

    def test_run(self):
        self.runner_2 = Runner('2')
        for _ in range(10):
            self.runner_2.run()
        self.assertEqual(self.runner_2.distance, 100)

    def test_challenge(self):
        self.runner_3 = Runner('3')
        self.runner_4 = Runner('4')
        for _ in range(10):
            self.runner_3.run()
            self.runner_4.walk()
        self.assertNotEqual(self.runner_3.distance, self.runner_4.distance)


if __name__ == "__main__":
    unittest.main()
