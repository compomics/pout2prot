from Parser import parser
from Analyzer import protein_grouping_analysis

# handling of command line (or config file) arguments

my_path = ".\\data\\*.pout"  # be careful with / (linux) and \\ (windows)
fdr_threshold = 0.01
decoy_flag = "decoy"
occam_flag = False

# Parsing - input: folder, output: dicts
# calls Parser
psm_exp, pep_psm, pep_prot, prot_pep = parser(my_path, fdr_threshold, decoy_flag)

# Running grouping algorithm - input: dicts and parameters (occam, anti-occam), output: new dicts with groups
# calls Analyzer
protein_groups, protein_subgroups = protein_grouping_analysis(occam_flag, prot_pep, pep_prot)

# Output writer - input: all dicts, output: file
# calls OutputWriter
print(protein_groups)
print(protein_subgroups)
