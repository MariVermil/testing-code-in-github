import unittest

import main
import random
import time
import matplotlib.pyplot as plt


class TestFunctionsValues(unittest.TestCase):
    def test_min_max(self):
        self.assertEqual(main._min((1, 2, 3, 4)), 1)
        self.assertEqual(main._max((1, 2, 3, 4)), 4)
        a = random.sample(range(1000), 10)
        self.assertEqual(main._min(a), min(a))
        self.assertEqual(main._max(a), max(a))
        self.assertEqual(main._min([]), None)
        self.assertEqual(main._max([]), None)

    def test_sum_mult(self):
        self.assertEqual(main._sum((1, 2, 3, 4)), 10)
        self.assertEqual(main._mult((1, 2, 3, 4)), 24)
        a = random.sample(range(1000), 10)
        self.assertEqual(main._sum(a), sum(a))
        true_mult = 1
        for i in a:
            true_mult *= i
        self.assertEqual(main._mult(a), true_mult)


class TestFunctionsSpeed(unittest.TestCase):
    def test_speed(self):
        N = 1000000
        A = int(1e2)

        a = [random.randint(0, A) for _ in range(N)]
        true_min = min(a)
        true_max = max(a)
        true_sum = sum(a)
        true_mult = 1
        for i in a:
            true_mult *= i

        start_time = time.time()
        self.assertEqual(main._min(a), true_min)
        self.assertLessEqual(time.time() - start_time, 1)

        start_time = time.time()
        self.assertEqual(main._max(a), true_max)
        self.assertLessEqual(time.time() - start_time, 1)

        start_time = time.time()
        self.assertEqual(main._sum(a), true_sum)
        self.assertLessEqual(time.time() - start_time, 1)

        start_time = time.time()
        self.assertEqual(main._mult(a), true_mult)
        self.assertLessEqual(time.time() - start_time, 1)


class IntegrationTest(unittest.TestCase):
    def test_multiple_functions(self):
        A = 1000
        N = 100

        a = [[random.randint(0, A) for _ in range(N)] for _ in range(3)]
        self.assertEqual(main._mult([main._min(a[0]), main._max(a[1]), main._sum(a[2])]),
                         min(a[0]) * max(a[1]) * sum(a[2]))


class TestDrawGraph(unittest.TestCase):
    def test_speed_graph(self):
        MAX_N = int(1e7)
        STEP = int(1e6)
        N = [x for x in range(STEP, MAX_N + 1, STEP)]
        A = 10000

        execution_times = []
        for n in N:
            a = [random.randint(0, A) for _ in range(n)]
            start_time = time.time()
            main._min(a)
            execution_times.append((time.time() - start_time) * 1000)

        plt.plot(execution_times, N, color='pink')
        plt.xlabel('Размер списка')
        plt.ylabel('Время выполнения, с')
        _ = plt.show()


if __name__ == '__main__':
    unittest.main()
    print("Everything passed")
