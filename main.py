#!/usr/bin/env python
import argparse

from cookie_clicker.building_info import BuildingInfo
from cookie_clicker.simulator import Simulator

def main(args):
    """Runs the simulator."""
    simulator = Simulator(building_info=BuildingInfo, duration=args.duration)
    clicker_states = simulator.run_strategies(args.all_strategies)
    simulator.print_comparison(clicker_states)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cookie Clicker Simulation')
    parser.add_argument('--duration',
                        '-d',
                        type=float,
                        help='Duration of the simulation.',
                        default=1e10)

    parser.add_argument('--all_strategies',
                        '-a',
                        action='store_true',
                        help='Do not ignore skipped strategies.')

    args = parser.parse_args()
    main(args)
