import Assert from "@/business/utils/Assert";

export default class Parser {
    static async parseFiles(files, fileNames, sampleCategories, fdrThreshold, decoyFlag) {
        const psmExp = new Map();
        const repCat = new Map();
        const pepPsm = new Map();
        const pepProt = new Map();
        const protPept = new Map();

        for (const [idx, fileName] of Object.entries(fileNames)) {
            repCat.set(fileName, sampleCategories[idx]);
        }

        for (const [fileIdx, file] of Object.entries(files)) {
            const fileContents = await Parser.readFile(file);

            const lines = fileContents.rstrip().split(/\r?\n/);
            const header = lines[0].split("\t");

            const peptideIndex = header.indexOf("peptide");
            const proteinsIndex = header.indexOf("proteinIds");
            const psmIdIndex = header.indexOf("PSMId");

            for (const line of lines.splice(1)) {
                const items = line.rstrip().split("\t");
                const peptide = items[peptideIndex].replace(/\[.*\]/g, "").split(".")[1];
                const proteins = items.splice(proteinsIndex);

                const psmId = items[psmIdIndex];

                for (const [i, protein] of Object.entries(proteins)) {
                    const splitProtein = protein.split("|", 3);
                    if (
                        splitProtein.length > 1 &&
                        splitProtein[1] !== "" &&
                        splitProtein[1] !== "sp" &&
                        splitProtein[1] !== "tr"
                    ) {
                        proteins[i] = splitProtein[1];
                    }
                }

                Assert.assert(decoyFlag === "" || !proteins.every((p) => p.includes(decoyFlag)), `${psmId} is only contained in decoy proteins!`);

                Assert.assert(!psmExp.has(psmId), "Only one experiment should be mapped to a PSM.");
                psmExp.set(psmId, fileNames[fileIdx]);

                if (!pepPsm.has(peptide)) {
                    pepPsm.set(peptide, new Set());
                }
                pepPsm.get(peptide).add(psmId);

                for (const protein of proteins) {
                    if (decoyFlag === "" || !protein.includes(decoyFlag)) {
                        if (!pepProt.has(peptide)) {
                            pepProt.set(peptide, new Set());
                        }
                        pepProt.get(peptide).add(protein);

                        if (!protPept.has(protein)) {
                            protPept.set(protein, new Set());
                        }
                        protPept.get(protein).add(peptide);
                    }
                }
            }
        }

        return [psmExp, pepPsm, pepProt, protPept, repCat];
    }

    static async readFile(file) {
        const fileReader = new FileReader();

        return new Promise((resolve) => {
            fileReader.onload = function(stats) {
                resolve(fileReader.result);
            }

            fileReader.readAsText(file);
        });
    }
}
