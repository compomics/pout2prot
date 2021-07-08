from .Parser import parser
from .Analyzer import protein_grouping_analysis
from .OutputWriter import write_to_file

import argparse


# handling of command line (or config file) arguments
def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_folder", help="Folder containing all input files that should be processed.")
    parser.add_argument("groups_output_file", help="File to which the found protein groups should be written to.")
    parser.add_argument("subgroups_output_file", help="File to which the found protein subgroups should be written to.")
    parser.add_argument("--occam", action="store_true", help="Use Occam's razor during the computation of the grouping process.", default=False)
    parser.add_argument("--decoy_flag", default="decoy", help="Flag that should be used to filter out decoy proteins.", type=str)
    parser.add_argument("--fdr_threshold", default=0.01, help="Maximum FDR rate.", type=float)
    return parser.parse_args()


def main():
    args = parse_args()
    my_path = args.input_folder  # be careful with / (linux) and \\ (windows)
    fdr_threshold = args.fdr_threshold
    decoy_flag = args.decoy_flag
    occam_flag = args.occam
    #
    # my_path = '../data/large_input'
    # fdr_threshold = 0.01
    # decoy_flag = "False"
    # occam_flag = True

    # Parsing - input: folder, output: dicts
    # calls Parser
    psm_exp, pep_psm, pep_prot, prot_pep, rep_cat = parser(my_path, fdr_threshold, decoy_flag)

    # Running grouping algorithm - input: dicts and parameters (occam, anti-occam), output: new dicts with groups
    # calls Analyzer
    protein_groups, protein_subgroups = protein_grouping_analysis(occam_flag, prot_pep, pep_prot)

    # Output writer - input: all dicts, output: file
    # calls OutputWriter
    write_to_file(rep_cat, protein_groups, psm_exp, pep_psm, pep_prot, prot_pep, args.groups_output_file)
    write_to_file(rep_cat, protein_subgroups, psm_exp, pep_psm, pep_prot, prot_pep, args.subgroups_output_file)
    # write_to_file(rep_cat, protein_groups, psm_exp, pep_psm, pep_prot, prot_pep, '../../output/groups.out')
    # write_to_file(rep_cat, protein_subgroups, psm_exp, pep_psm, pep_prot, prot_pep, '../../output/subgroups.out')
