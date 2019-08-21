from typing import Dict, List
from decimal import Decimal
from argparse import Namespace
from tabulate import tabulate

from cookie_clicker.simulator import Simulator
from cookie_clicker.utils import Registry


class Challenge(object):

    def __init__(self, opts: Namespace) -> None:
        super(Challenge, self).__init__()

        self._competitions = Registry.competitions(
            active_only=not opts.all_competitions)

        if opts.strategy is not None:
            self._strategies = Registry.get_strategies(opts.strategy)
        else:
            self._strategies = Registry.strategies(
                active_only=not opts.all_strategies)

        self.building_info = opts.building_info
        self.results: Dict[str, Dict[str, Decimal]] = {}

        self.comp_names = [c.name for c in self._competitions]
        self.strat_names = [s.name for s in self._strategies]

    def run(self) -> None:
        self.results.clear()

        for comp in self._competitions:
            self.results[comp.name] = {}

            simulator = Simulator(building_info=self.building_info,
                                  duration=comp.duration)

            for strat in self._strategies:
                clicker_state = simulator.run_strategy(strat,
                                                       print_results=False)
                self.results[comp.name][strat.name] = comp(clicker_state)

    def print_results(self,
                      tablefmt: str = 'fancy_grid',
                      numalign: str = 'center',
                      stralign: str = 'center') -> None:

        headers = ['Strategy \\ Competition'] + self.comp_names
        tablerows: List[List[str]] = []

        for strategy_name in self.strat_names:
            tablerow: List[str] = [strategy_name]
            for competition_name, comp in zip(self.comp_names,
                                              self._competitions):
                comp_res = self.results[competition_name]
                compare_func = max if comp.bigger_is_better else min
                best_result = compare_func(comp_res.values())

                res = comp_res[strategy_name]

                is_best_result = res == best_result

                if competition_name.startswith(
                        'time_to') and res == comp.FOREVER:
                    disp_val = '-'
                else:
                    disp_val = f'{res:.3e}'

                if is_best_result:
                    disp_val = f'** {disp_val} **'

                tablerow += [disp_val]
            tablerows += [tablerow]

        print(
            tabulate(tablerows,
                     headers=tuple(headers),
                     tablefmt=tablefmt,
                     numalign=numalign,
                     stralign=stralign))
