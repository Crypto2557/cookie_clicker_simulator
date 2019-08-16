#!/usr/bin/env python
import argparse
from tabulate import tabulate

from cookie_clicker.simulator import Simulator
from cookie_clicker.utils import Config
from cookie_clicker import competitions


def run_challenge(building_info: str, run_all_strategies: bool = False, run_all_competitions: bool = True):
    competition_list = competitions.all_competitions if run_all_competitions else competitions.active

    results = {}
    for criterion, duration, _ in competition_list:
        clicker_states = Simulator(building_info=building_info, duration=duration).run_strategies(run_all_strategies, False)
        results[criterion.__name__] = {name: criterion(clicker_state) for name, clicker_state in clicker_states}

    return results


def print_challenge_results(results):
    strategy_names = list(results[list(results.keys())[0]].keys())
    competition_names = list(results.keys())

    header = ['Strategy \\ Competition'] + competition_names
    tablerows = []
    for strategy_name in strategy_names:
        tablerow = [strategy_name]
        for competition_name in competition_names:
            res = results[competition_name][strategy_name]
            if competition_name.startswith('time_to') and res == competitions.FOREVER:
                disp_val = '-'
            else:
                disp_val = '%.3e' % res
            tablerow += [disp_val]
        tablerows += [tablerow]

    print(tabulate(tablerows, headers=tuple(header), tablefmt='fancy_grid', numalign='center'))


def main(args):
    results = run_challenge(args.building_info, args.all_strategies, args.all_competitions)
    print_challenge_results(results)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cookie Clicker Simulation')
    parser.add_argument('--duration',
                        '-d',
                        type=float,
                        help='Duration of the simulation.',
                        default=1e10)

    parser.add_argument('--building_info',
                        '-b',
                        type=str,
                        help='Config file about the buildings.',
                        default=Config.DEFAULT_BUILDING_INFO)

    parser.add_argument('--all_strategies',
                        '-a',
                        action='store_true',
                        help='Do not ignore skipped strategies.')

    parser.add_argument('--all_competitions',
                        '-c',
                        action='store_true',
                        help='Do not ignore skipped competitions.')

    main(parser.parse_args())
