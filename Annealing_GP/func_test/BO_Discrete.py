import time
from math import *
from bayes_opt import BayesianOptimization
from bayes_opt import UtilityFunction
from bayes_opt.logger import JSONLogger
from bayes_opt.event import Events
import numpy as np

def black_box_function(x1, x2, x3, x4, x5):
    """Function with unknown internals we wish to maximize.

    This is just serving as an example, for all intents and
    purposes think of the internals of this function, i.e.: the process
    which generates its output values, as unknown.
    """
    
    return function_discrete(x1, x2, x3, x4, x5)


def function_discrete(x1, x2, x3, x4, x5):
    # Get the discrete Parameters 
    # Divide the parameter space into 1000 discrete values 
    para_space = list(np.arange(-100, 101, 200/1000))
        
    # Find the closest value of x1 and x2 in the parameter space
    x1 = min(para_space, key=lambda x:abs(x-x1))
    x2 = min(para_space, key=lambda x:abs(x-x2))

    next_point_to_probe['x1'] = x1
    next_point_to_probe['x2'] = x2

    # E1: Rastrigin's function (shifted)
    # return -(20 + x1**2 + x2**2 - 10 * (cos(2*pi*x1) + cos(2*pi*x2)))

    # E2: Rastrigin's function (shifted)
    # return -(20 + (x1-2)**2 + (x2+2)**2 - 10 * (cos(2*pi*(x1-2)) + cos(2*pi*(x2+2))))
    
    # E3: SCHAFFER FUNCTION
    # return 0.5 - (sin(x1**2-x2**2)**2-0.5)/(1+0.001*(x1**2+x2**2))**2
    
    # E4: SCHAFFER FUNCTION (shifted)
    # return 0.5 - (sin((x1-2)**2-(x2+2)**2)**2-0.5)/(1+0.001*((x1-2)**2+(x2+2)**2))**2

    # E5: Ackley function (5-D)
    result = -20*exp(-0.2*sqrt((1/5)*(x1**2+x2**2+x3**2+x4**2+x5**2)))-exp((1/5)*(cos(2*pi*x1)+cos(2*pi*x2)+cos(2*pi*x3)+cos(2*pi*x4)+cos(2*pi*x5)))+exp(1)+20
    return -result
    

if __name__ == "__main__":
    optimizer = BayesianOptimization(
        f=None,
        pbounds={'x1': (-10, 10), 'x2': (-10, 10), 'x3': (-10, 10), 'x4': (-10, 10), 'x5': (-10, 10)},
        verbose=2,
        random_state=1,
    )

    utility = UtilityFunction(kind="ucb", kappa=2.5, xi=0.0)


    # file_name = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    file_name = "Discrete"
    logger = JSONLogger(path="./Discrete/%s.json"%file_name)
    optimizer.subscribe(Events.OPTIMIZATION_STEP, logger)
        
    num_iter = 60;
    for i in range(num_iter):
        print("%dth iteration: " % i, end='')

        # Get back a suggestion for the next parameter combination the optimizer wants to probe.
        next_point_to_probe = optimizer.suggest(utility)
        print("next point to probe (continuous) is: ", next_point_to_probe)

        # Evaluate your function at the suggested point however/whenever you like.
        target = black_box_function(**next_point_to_probe)
        print("next_point_to_probe (discrete) is: ", next_point_to_probe)
        print("target = ", target)

        # Tell the optimizer what target value was observed.
        optimizer.register(
            params=next_point_to_probe,
            target=target,
        )
        
    print("\nBest target and parameters: ")
    print(optimizer.max)

