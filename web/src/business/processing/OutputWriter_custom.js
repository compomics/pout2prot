export default class OutputWriter_custom {
    writeContentToString(repCat, groups, psmExp, pepPsm, proteinPeptideMap) {
        let output = "sample category\tsample name\tprotein accessions\tspectrum count\n";

        // To calculate the spectrum count properly we need to map each peptide to all its protein groups. This will
        // be the divisor we use to adjust for a psm that belongs to multiple groups.
        const peptideToGroups = new Map();

        for (let [group, proteins] of Object.entries(groups)) {
            for (let i = 0; i < proteins.length; i++) {
                const protein = proteins[i];
                for (const peptide of proteinPeptideMap[protein]) {
                    if (!peptideToGroups.has(peptide)) {
                        peptideToGroups.set(peptide, new Set());
                    }
                    peptideToGroups.get(peptide).add(group);
                }
            }
        }

        // Group names are ignored for the output file, can only loop using values
        for (const proteins of Object.values(groups)) {
            // There will be a separate line written for each experiment.
            // Here we find all experiments for this group and calculate the adjusted spectrum count for each.
            const experiments = new Set();
            const experimentToCount = new Map();

            const usedPeptides = new Set();
            for (const protein of proteins) {
                for (const peptide of proteinPeptideMap[protein]) {
                    if (!usedPeptides.has(peptide)) {
                        for (const psm of pepPsm[peptide]) {
                            const divideBy = peptideToGroups.get(peptide).size;
                            const experiment = psmExp[psm];

                            if (experimentToCount.has(experiment)) {
                                experimentToCount.set(experiment, experimentToCount.get(experiment) + 1 / divideBy);
                            } else {
                                experimentToCount.set(experiment, 1 / divideBy);
                                experiment.add(experiment);
                            }
                        }
                    }
                    usedPeptides.add(peptide);
                }
            }

            // Write a line in output file for each experiment
            for (const experiment of experiments) {
                const category = repCat[experiment];
                const categoryStrings = category.split("\\");
                const categoryString = categoryStrings[categoryStrings.length - 2];
                const experimentStrings = experiment.split("\\");
                const experimentString = experimentStrings[experimentStrings.length - 1].split(".")[0];
                output += `${categoryString}\t${experimentString}\t${proteins.join(',')}\t${experimentToCount[experiment]}\n`
            }
        }

        return output;
    }
}
