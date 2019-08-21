#!/usr/bin/env python
import argparse
from tabulate import tabulate
from typing import Dict, List
from decimal import Decimal

from cookie_clicker.utils import Config
from cookie_clicker.challenge import Challenge


def main(args):
    challenge = Challenge(args)
    challenge.run()
    challenge.print_results()


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
