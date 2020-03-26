import multiprocessing
from typing import Callable, Tuple
import numpy as np
import json
import time
import os
import importlib

INPUTS_PATH = f'{os.getcwd()}\\inputs'


def get_input(problem_name: str, idx: int) -> Tuple:
    path = f'{INPUTS_PATH}\\{problem_name}\\test_{idx}.json'
    if f'test_{idx}.json' not in os.listdir(f'{INPUTS_PATH}\\{problem_name}'):
        raise FileNotFoundError('Test index does not exist')
    with open(path, 'r') as f:
        arguments = json.load(f)
    if not arguments['visible']:
        raise PermissionError('The requested test is not visible')
    return arguments['arguments']


def wrapper(func, desired_output, idx, *args, **kwargs):
    initial_time = time.time()
    output = func(*args, **kwargs)
    end_time = time.time()
    if desired_output == output:
        print(f'Well done! test #{idx} had been passed sucessfully.')
        print(f'Time required: {np.round(end_time - initial_time, 5)} seconds.')
    else:
        print('Solution is incorrect.')


def get_official_and_user_solutions(problem_name: str) -> Tuple[Callable, Callable]:
    path = f'problems.{problem_name.replace(" ", "_")}'
    user_file = '.' + problem_name.title().replace(" ", "")
    official_file = '.' + problem_name.title().replace(" ", "") + 'Solved'
    user_sol = importlib.import_module(user_file, path)
    official_sol = importlib.import_module(official_file, path)

    module = problem_name.replace(" ", "_") + '_solution'
    return getattr(official_sol, module), getattr(user_sol, module)


def get_test(problem_name: str, test_num: int):
    try:
        path = f'{INPUTS_PATH}\\{problem_name}\\test_{test_num}.json'
        with open(path, 'r') as f:
            data = json.load(f)
            arguments = data['arguments'].values()
            desired_output = data['desired_output']
            return arguments, desired_output
    except:
        raise FileNotFoundError('Test index does not exist')


def run_test(time_limit: int, *args):
    p = multiprocessing.Process(target=wrapper, args=args)
    start = time.time()
    p.start()

    # give the solution the given time to run
    if time_limit == 0:
        p.join()
        time_limit = time.time() - start
    else:
        p.join(time_limit)

    # If thread is still active, terminate
    if p.is_alive():
        print('Time limit exceeded. You can do better than that!')
        p.terminate()
        p.join()
    return time_limit


def test(problem_name: str, idx: int) -> None:
    arguments, desired_output = get_test(problem_name, idx)
    official_sol, user_sol = get_official_and_user_solutions(problem_name)
    print('First running official')
    time_limit = run_test(0, official_sol, desired_output, idx, *arguments)
    print('Now running yours')
    run_test(time_limit, user_sol, desired_output, idx, *arguments)
