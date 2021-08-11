# only for Occams razor (PAPSSO): go through proteins and remove those that have no unique peptides
# Remove all proteins that don't contain unique peptides

# Input
# 1) Peptide -> Set<Protein>
# 2) Protein -> Set<Peptide>

# We need to check whether some of these proteins do not contain unique peptides. We can check this by iterating over
# all proteins, for each protein extract all associated peptides and check if these peptides are all associated to
# another at least one other protein. If that's the case, we remove the current protein.


def occam_filter(peptides_to_proteins, proteins_to_peptides):
    """ Perform filtering on the proteins, based on Occam's razor decisions.

    :param peptides_to_proteins: A dictionary that maps every peptide onto a set of all proteins (that are associated
    with ths peptide).
    :param proteins_to_peptides: A dictionary that maps every protein onto a set of all peptides (which are associated
    with this protein).
    :return: Both set's given are updated in-place. This means that no explicit value is returned, but rather that the
    arguments passed will be changed.
    """

    # peptides that only have a single protein are unique
    unique_peps = set()
    # proteins that have are
    unique_proteins = set()
    # peptides that belong to a unique protein are explained
    explained_peps = set()
    for [pep1, prots1] in peptides_to_proteins.items():
        if len(prots1) == 1:
            # get first and only element of set as protein
            for protein in prots1:
                break
            # update unique sets
            unique_proteins.add(protein)
            unique_peps.add(pep1)
            # add the peptides of this unique protein to explained proteins
            for pep in proteins_to_peptides[protein]:
                explained_peps.add(pep)

    # now that we tracked unique proteins we can check which ones should be removed
    # we use 2 tests: 1. explained by unique proteins, 2. explained by being a subset of another protein
    remove_proteins = set()
    for [prot2, peps2] in proteins_to_peptides.items():
        # only check non-unique proteins here
        if not (prot2 in unique_proteins):
            # starting with True, in the first test maybe set to False, in the second test may be set back to False
            is_explained = True
            # the FIRST TEST checks if the peptides of this protein are fully explained by unique proteins
            for pep_test in peps2:
                if not (pep_test in explained_peps):
                    is_explained = False
            # the SECOND TEST checks if the peptides of this protein are a subset of another non-unique protein
            # collect all other proteins that share any of this proteins peptides
            sharing_proteins = set()
            for pep_group in peps2:
                for protein_share in peptides_to_proteins[pep_group]:
                    sharing_proteins.add(protein_share)
            # here comes the actual subset-test
            for protein_test in sharing_proteins:
                # the < operator tests for strict subset relation
                if peps2 < proteins_to_peptides[protein_test]:
                    is_explained = True
            # finally add this protein to be removed if its peptides are explained by other proteins
            if is_explained:
                remove_proteins.add(prot2)

    # Removing step
    peptides_marked_for_update = set()
    for prot_remove in remove_proteins:
        for pep in proteins_to_peptides[prot_remove]:
            peptides_marked_for_update.add(pep)
        del proteins_to_peptides[prot_remove]

    for pept_marked in peptides_marked_for_update:
        peptides_to_proteins[pept_marked] = peptides_to_proteins[pept_marked].difference(remove_proteins)
