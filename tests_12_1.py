from unittest import TestCase


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(TestCase):
    def test_walk(self):
        test_w = Runner('walk')
        for _ in range(10):
            test_w.walk()
        self.assertEqual(test_w.distance, 50)

    def test_run(self):
        test_r = Runner('run')
        for _ in range(10):
            test_r.run()
        self.assertEqual(test_r.distance, 100)

    def test_challeng(self):
        runner_r = Runner('run')
      =>
Testing started at 19:06 ...
Launching unittests with arguments python -m unittest D:\proj\pythonProjectUrban\module_12\module_12_1.py in D:\proj\pythonProjectUrban\module_12



Ran 3 tests in 0.006s

OK

Process finished with exit code 0

        runner_w = Runner('walk')
        for _ in range(10):
            runner_r.run()
            runner_w.walk()
        self.assertNotEqual(runner_w.distance,runner_r.distance)
