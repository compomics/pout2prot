def create_protein_groups(protein_peptide_dict, peptide_protein_dict):
    """creates protein groups, calls recursion_check_for_more_linked_proteins"""
    # create dictionary to be returned, will map protein_group_id to list of protein_id
    protein_groups = dict()
    # protein_group_id is a simple integer
    protein_group_id = 0
    # create list of protein_id from proteins-dict which we will exhaust
    remaining_proteins = set(protein_peptide_dict.keys())
    # continue until no proteins remaining for processing
    while len(remaining_proteins) > 0:
        # take another protein
        protein = remaining_proteins.pop()
        # create new protein_group from current protein (i.e. entry in dict)
        protein_group_id += 1
        protein_groups[protein_group_id] = {protein}
        # check for more linked proteins with recursive call
        recursion_check_for_more_linked_proteins(protein_group_id, remaining_proteins, protein_peptide_dict,
                                                 protein_groups, peptide_protein_dict)

    # return the map protein_group_id -> list(protein_id)
    return protein_groups


def recursion_check_for_more_linked_proteins(protein_group_id, remaining_proteins, protein_peptide_dict,
                                             protein_groups, peptide_protein_dict):
    """recursive call, handles most of the grouping logic"""
    # 1. create a set of proteins that are currently in the group
    current_protein_set = set()
    # 2. And collect all the peptides of these proteins into a set
    peptide_set = set()

    for protein in protein_groups[protein_group_id]:
        # go through list of peptides in the protein_peptide_dict and add them to set
        current_protein_set.add(protein)
        peptide_set.update(protein_peptide_dict[protein])

    # 3. for all peptides in the peptide_set collect a new protein set, possibly catching new ones
    new_protein_set = set()
    for peptide in peptide_set:
        new_protein_set.update(peptide_protein_dict[peptide])
    # update the protein_groups-entry with the new list
    protein_groups[protein_group_id].update(new_protein_set)
    # update the remaining_proteins-list by removing the newly added proteins
    for protein in new_protein_set:
        if protein in remaining_proteins:
            remaining_proteins.remove(protein)
    # 4a. if current_protein_set is not equal to new_protein_set call recursion_check_for_more_linked_proteins again
    if (len(current_protein_set.difference(new_protein_set)) != 0
            or len(new_protein_set.difference(current_protein_set)) != 0):
        # make recursive call
        recursion_check_for_more_linked_proteins(protein_group_id, remaining_proteins, protein_peptide_dict,
                                                 protein_groups, peptide_protein_dict)
    # 4b. if current_protein_set is equal to new_protein_set, the group creation is finished
