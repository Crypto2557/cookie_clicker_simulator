#!/usr/bin/env python
"""
Cookie Clicker Competitions
"""
import argparse

from cookie_clicker.utils import Config
from cookie_clicker.challenge import Challenge


def main(args):
    """Creates a challenge and runs all competitions"""
    challenge = Challenge(args)
    challenge.run()
    challenge.print_results()


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(description='Cookie Clicker Simulation')
    PARSER.add_argument('--duration',
                        '-d',
                        type=float,
                        help='Duration of the simulation.',
                        default=1e10)

    PARSER.add_argument('--building_info',
                        '-b',
                        type=str,
                        help='Config file about the buildings.',
                        default=Config.Defaults.BUILDING_INFO)

    PARSER.add_argument('--all_strategies',
                        '-a',
                        action='store_true',
                        help='Do not ignore skipped strategies.')

    PARSER.add_argument('--strategy',
                        '-s',
                        type=str,
                        help='Execute only this one strategy.')

    PARSER.add_argument('--all_competitions',
                        '-c',
                        action='store_true',
                        help='Do not ignore skipped competitions.')

    main(PARSER.parse_args())
