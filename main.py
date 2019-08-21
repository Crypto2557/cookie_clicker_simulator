#!/usr/bin/env python
import argparse
from tabulate import tabulate
from typing import Dict, List
from decimal import Decimal

from cookie_clicker.simulator import Simulator
from cookie_clicker.utils import Config, Registry
from cookie_clicker import competitions


def run_challenge(building_info: str,
                  strategy: str = None,
                  run_all_strategies: bool = False,
                  run_all_competitions: bool = True):

    results = {}
    for comp in Registry.competitions(run_all_competitions):
        simulator = Simulator(building_info=building_info,
                              duration=comp.duration)
        clicker_states = simulator.run_strategies(strategy, run_all_strategies,
                                                  False)
        results[comp.name] = {
            name: comp(clicker_state) for name, clicker_state in clicker_states
        }

    return results


def print_challenge_results(results: Dict[str, Dict[str, Decimal]]):
    strategy_names = list(results[list(results.keys())[0]].keys())
    competition_names = list(results.keys())

    header = ['Strategy \\ Competition'] + competition_names
    tablerows: List[List[str]] = []
    for strategy_name in strategy_names:
        tablerow: List[str] = [strategy_name]
        for competition_name in competition_names:

            res = results[competition_name][strategy_name]

            # Check if this result is the best result
            comp = Registry.get_competition(competition_name)

            is_best_result = True
            for comp_strategy_name in strategy_names:
                comp_res = results[competition_name][comp_strategy_name]

                if comp_res > res and comp.bigger_is_better:
                    is_best_result = False
                    break

                if comp_res < res and not comp.bigger_is_better:
                    is_best_result = False
                    break

            if competition_name.startswith('time_to') and res == comp.FOREVER:
                disp_val = '-'
            else:
                disp_val = f'{res:.3e}'

            if is_best_result:
                disp_val = f'** {disp_val} **'

            tablerow += [disp_val]
        tablerows += [tablerow]

    print(
        tabulate(tablerows,
                 headers=tuple(header),
                 tablefmt='fancy_grid',
                 numalign='center',
                 stralign='center'))


def main(args):
    results = run_challenge(args.building_info, args.strategy,
                            args.all_strategies, args.all_competitions)
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
                        default=Config.Defaults.BUILDING_INFO)

    parser.add_argument('--all_strategies',
                        '-a',
                        action='store_true',
                        help='Do not ignore skipped strategies.')

    parser.add_argument('--strategy',
                        '-s',
                        type=str,
                        help='Execute only this one strategy.')

    parser.add_argument('--all_competitions',
                        '-c',
                        action='store_true',
                        help='Do not ignore skipped competitions.')

    main(parser.parse_args())
