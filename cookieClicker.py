import argparse
from buildingInfo import BuildingInfo
from simulator import Simulator
from strategies import *


def main(duration):
    """Runs the simulator."""
    simulator = Simulator(building_info=BuildingInfo, duration=duration)
    clicker_states = simulator.run_strategies([strategy_monster, strategy_cheap, strategy_expensive])
    simulator.print_comparison(clicker_states)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cookie Clicker Simulation')
    parser.add_argument('-d',
                        '-duration',
                        type=float,
                        help='Duration of the simulation.',
                        default=1e10)
    args = parser.parse_args()
    main(args.d)
