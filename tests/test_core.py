import pickle

import osqp

"""Test using pytest
    run in parallel (all test should be able to be run on parallel), without --runbig
    pytest -n auto --lf -rA --cov-report term --cov=miosqp tests/
"""


def test_run_maxiter_problem():
    prob_file = '76'

    # Load one problem
    with open('./max_iter_examples/%s.pickle' % prob_file, 'rb') as f:
        problem = pickle.load(f)

    problem['settings']['verbose'] = True
    problem['settings']['rho'] = 0.01

    # Solve with OSQP
    model = osqp.OSQP()
    model.setup(problem['P'], problem['q'], problem['A'],
                problem['l'], problem['u'], **problem['settings'])
    model.solve()
