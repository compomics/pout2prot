from .pd2pout import pd_to_pout2prot

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="A folder containing all PD-files that should be converted to pout files.")
    parser.add_argument("output", help="The folder to which the converted pout-files should be stored.")
    return parser.parse_args()


def main():
    args = parse_args()
    pd_to_pout2prot(args.input, args.output)
