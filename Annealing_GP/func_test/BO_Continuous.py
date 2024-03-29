import time
from math import *
from bayes_opt import BayesianOptimization
from bayes_opt import UtilityFunction
from bayes_opt.logger import JSONLogger
from bayes_opt.event import Events

# pbounds={'x1': (-1+88, 1+88), 'x2': (-1+0.1324, 1+0.1324), 'x3': (-1-0.4233, 1-0.4233), 'x4': (-1+0.8023, 1+0.8023), 'x5': (-1-0.6352, 1-0.6352)},
x1_low = -1.5+88
x1_high = 1.5+88
x2_low = -1.5+0.1324
x2_high = 1.5+0.1324
x3_low = -1.5-0.4233
x3_high = 1.5-0.4233
x4_low = -1.5+0.8023
x4_high = 1.5+0.8023
x5_low = -1.5-0.6352
x5_high = 1.5-0.6352

# x1_low = -2+88
# x1_high = 2+88
# x2_low = -2+0.1324
# x2_high = 2+0.1324
# x3_low = -2-0.4233
# x3_high = 2-0.4233
# x4_low = -2+0.8023
# x4_high = 2+0.8023
# x5_low = -2-0.6352
# x5_high = 2-0.6352


# def black_box_function(x1, x2):
def black_box_function(x1, x2, x3, x4, x5):
    # E11
    return E12_func(x1, x2, x3, x4, x5)


def E11_func(x1, x2, x3, x4, x5):
    # E11: Shifted Happy Cat Function (5-D)
    # Expected optimum: 100 at `(88, 0.1324, -0.4233, 0.8012, -0.6352)`

    # Dimension 5
    d = 5

    # Shift the parameters
    x1 = x1 - 1 - 88
    x2 = x2 - 1 - 0.1324
    x3 = x3 - 1 + 0.4233
    x4 = x4 - 1 - 0.8012
    x5 = x5 - 1 + 0.6352

    alpha = 1/8

    xx = x1*x1 + x2*x2 + x3*x3 + x4*x4 + x5*x5

    fx = ((xx-d)**2)**alpha + 1/d * (1/2 * xx + x1 + x2 + x3 + x4 + x5) + 1/2
    fx = -fx
    fx = fx * 10 + 100

    return fx


def E12_func(x1, x2, x3, x4, x5):
    # E12: Xin-She Yang N. 3 Function (5-D)
    # Expected optimum: 100 at `(88, 0.1324, -0.4233, 0.8012, -0.6352)`
    # Shift the parameters
    x1 = x1 - 0 - 88
    x2 = x2 - 0 - 0.1324
    x3 = x3 - 0 + 0.4233
    x4 = x4 - 0 - 0.8012
    x5 = x5 - 0 + 0.6352

    m = 5
    beta = 15

    fx = exp(-((x1/beta)**(2*m) +(x2/beta)**(2*m) + (x3/beta)**(2*m) + (x4/beta)**(2*m) +  (x5/beta)**(2*m))) - 2 * exp(-(x1**2+x2**2+x3**2+x4**2+x5**2)) * (cos(x1))**2 * (cos(x2))**2 * (cos(x3))**2 * (cos(x4))**2 * (cos(x5))**2
    fx = -fx
    fx = fx * 100

    return fx


if __name__ == "__main__":
    optimizer = BayesianOptimization(
        f=None,
        # pbounds={'x1': (-10, 10), 'x2': (-10, 10)},
        # pbounds={'x1': (-500, 500), 'x2': (-500, 500), 'x3': (-500, 500), 'x4': (-500, 500), 'x5': (-500, 500)},
        # pbounds={'x1': (-2+1+88, 2+1+88), 'x2': (-2+1+0.1324, 2+1+0.1324), 'x3': (-2+1-0.4233, 2+1-0.4233), 'x4': (-2+1+0.8023, 2+1+0.8023), 'x5': (-2+1-0.6352, 2+1-0.6352)},
        # pbounds={'x1': (-2*pi+88, 2*pi+88), 'x2': (-2*pi+0.1324, 2*pi+0.1324), 'x3': (-2*pi-0.4233, 2*pi-0.4233), 'x4': (-2*pi+0.8023, 2*pi+0.8023), 'x5': (-2*pi-0.6352, 2*pi-0.6352)},
        pbounds={'x1': (x1_low, x1_high), 'x2': (x2_low, x2_high), 'x3': (x3_low, x3_high), 'x4': (x4_low, x4_high), 'x5': (x5_low, x5_high)},
        verbose=2,
        random_state=1,
    )
    
    utility = UtilityFunction(kind="ucb", kappa=2.5, xi=0.0)
    
    file_name = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # file_name = "Continuous"
    logger = JSONLogger(path="./Continuous/Continuous_%s.json"%file_name)
    optimizer.subscribe(Events.OPTIMIZATION_STEP, logger)
    
    num_iter = 3 + 100; # First 20 iterations as random search in the continuous space
    for i in range(num_iter):
        print("%dth iteration: " % i, end='')

        # Get back a suggestion for the next parameter combination the optimizer wants to probe.
        next_point_to_probe = optimizer.suggest(utility)
        print("next point to probe (continuous) is: ", next_point_to_probe)

        # Evaluate your function at the suggested point however/whenever you like.
        target = black_box_function(**next_point_to_probe)
        print("target = ", target)

        # Tell the optimizer what target value was observed.
        optimizer.register(
            params=next_point_to_probe,
            target=target,
        )
    
    print("\nBest target and parameters: ")
    print(optimizer.max)