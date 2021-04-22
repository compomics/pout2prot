# protein groups
# start with list of proteins, take 1 and add it to a new group
# recursion
# // 1. for all proteins in the group, collect the shared peptide set
# // 2.a for all peptides in the set collect protein set
# // 2.b collect the proteins in our current group for comparison
# // 3. if protein set equals the set of the current protein group -> group creation finished, return proteingroup
# // 4. if protein set not equals set of the current protein group -> continue with 1
