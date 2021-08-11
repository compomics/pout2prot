<template>
    <v-container fluid style="max-width: 1600px;">
        <v-row>
            <v-col cols="12">
                <h1>
                    Welcome
                </h1>
                <div class="mb-2">
                    This application can be used to perform protein grouping and subgrouping on the
                    proteins recorded in a .pout file. Complete all steps in the wizard below to fulfil the analysis.
                    All conversion steps take place on the client side. This means that none of your files are sent to
                    our web server and that they are only used by the browser itself to perform the requested analysis.
                </div>
                <v-stepper vertical v-model="currentStep">
                    <v-stepper-step :complete="currentStep > 1" step="1" editable>
                        Select all input files
                        <small>This application only accepts .pout-files</small>
                    </v-stepper-step>
                    <v-stepper-content step="1">
                        <v-alert
                            icon="mdi-information"
                            text
                            v-if="this.allFiles.length === 0"
                            type="info"
                        >
                            You can add multiple files to the selection by using the input box below. Please note that
                            it is also possible to add files multiple times (you don't need to select all files at
                            once).
                        </v-alert>
                        <div class="d-flex my-4">
                            <v-file-input v-model="files" multiple dense hide-details></v-file-input>
                            <v-btn color="primary" class="ml-4" @click="addFiles" :disabled="files.length === 0">Add</v-btn>
                        </div>
                        <v-simple-table v-if="this.allFiles.length > 0">
                            <template v-slot:default>
                                <thead>
                                    <tr>
                                        <th class="text-left">File</th>
                                        <th class="text-left">Sample category</th>
                                        <th class="text-left">Sample name</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="(file, idx) in allFiles" :key="file.name">
                                        <td>{{ file.name }}</td>
                                        <td>
                                            <v-text-field v-model="sampleCategories[idx]">
                                            </v-text-field>
                                        </td>
                                        <td>
                                            <v-text-field v-model="sampleNames[idx]">
                                            </v-text-field>
                                        </td>
                                    </tr>
                                </tbody>
                            </template>
                        </v-simple-table>

                        <div class="d-flex mt-2">
                            <v-btn class="ml-auto" color="primary" @click="currentStep = 2" :disabled="allFiles.length === 0">
                                Continue
                            </v-btn>
                        </div>
                    </v-stepper-content>
                    <v-stepper-step :complete="currentStep > 2" step="2" editable>
                        Parameters
                    </v-stepper-step>
                    <v-stepper-content step="2" >
                        <v-container fluid>
                            <v-row>
                                <v-col cols="5">
                                    <div class="settings-title">Occam's razor</div>
                                    <span class="settings-text">
                                        This setting only affects the subgroup analysis. If enabled, all proteins that
                                        not uniquely identify at least one peptide are discarded.
                                    </span>
                                </v-col>
                                <v-col cols="1" class="d-flex justify-center">
                                    <v-switch v-model="occam"></v-switch>
                                </v-col>
                                <v-col cols="5">
                                    <div class="settings-title">FDR threshold</div>
                                    <span class="settings-text">
                                        This setting affects the parsing of the input files. Only entries for which the
                                        FDR is larger than the value given here are retained, all other entries are
                                        not taken into account while performing the protein grouping analysis.
                                    </span>
                                </v-col>
                                <v-col cols="1">
                                    <v-text-field
                                        label="0.05"
                                        step="0.01"
                                        min="0"
                                        max="1"
                                        single-line filled
                                        type="number"
                                        v-model="fdr">
                                    </v-text-field>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col cols="5">
                                    <div class="settings-title">Decoy flag</div>
                                    <span class="settings-text">
                                        Which flag is used to indicate decoy proteins in the input data set? All
                                        proteins that include this substring in their name are discarded from the
                                        analysis. Leave empty if no such flag has been set.
                                    </span>
                                </v-col>
                                <v-col cols="1">
                                    <v-text-field single-line filled v-model="decoyFlag">
                                    </v-text-field>
                                </v-col>
                            </v-row>
                        </v-container>
                        <div class="d-flex mt-2">
                            <v-btn text @click="currentStep = 1">
                                Go back
                            </v-btn>
                            <v-btn class="ml-auto" color="primary" @click="startAnalysis">
                                Continue
                            </v-btn>
                        </div>
                    </v-stepper-content>
                    <v-stepper-step :complete="currentStep > 3" step="3" editable @click="startAnalysis">
                        View results
                    </v-stepper-step>
                    <v-stepper-content step="4">
                        <div class="d-flex align-center flex-column" v-if="analysisInProgress">
                            <v-progress-circular indeterminate color="primary"></v-progress-circular>
                            <span>Performing analysis, please wait...</span>
                        </div>
                        <div class="d-flex align-center flex-column" v-else-if="error">
                            <v-alert
                                border="right"
                                colored-border
                                type="error"
                                outlined>
                                {{ errorMessage }}
                            </v-alert>
                        </div>
                        <div class="d-flex align-center flex-column" v-else>
                            <span>
                                Protein grouping has successfully been performed. Click the button below to download the
                                generated files.
                            </span>
                            <v-btn color="primary" outlined x-large fab class="mt-2" @click="downloadFiles">
                                <v-icon>
                                    mdi-cloud-download-outline
                                </v-icon>
                            </v-btn>
                        </div>
                        <div class="d-flex mt-2">
                            <v-btn class="ml-auto" color="primary" @click="currentStep = 1">
                                Start over
                            </v-btn>
                        </div>
                    </v-stepper-content>
                </v-stepper>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import { protein_grouping_analysis } from "@/business/processing/Analyzer";
import { write_to_file } from "@/business/processing/OutputWriter";
import { set, dict } from '@/business/processing/org.transcrypt.__runtime__.js'
import Parser from "@/business/processing/Parser";

import JSZip from 'jszip';
import FileSaver from 'file-saver';

export default {
    name: 'HomePage',

    data: () => ({
        files: [],
        allFiles: [],
        sampleCategories: [],
        sampleNames: [],
        currentStep: 1,
        occam: false,
        fdr: 0.01,
        decoyFlag: "",
        analysisInProgress: false,
        zipResult: null,
        error: false,
        errorMessage: ""
    }),

    methods: {
        addFiles: function() {
            for (const file of this.files) {
                if (!this.allFiles.find(f => f.name === file.name)) {
                    this.allFiles.push(file);
                    const fileName = file.name.replace(/.pout$/, "");
                    this.sampleNames.push(fileName);
                    this.sampleCategories.push(fileName);
                }
            }
        },
        startAnalysis: async function() {
            this.error = false;

            if (this.allFiles) {
                this.currentStep = 4;

                let psmExp;
                let pepPsm;
                let pepProt;
                let protPept;
                let repCat;

                try {
                    [
                        psmExp, pepPsm, pepProt, protPept, repCat
                    ] = await Parser.parseFiles(
                        this.allFiles,
                        this.sampleNames,
                        this.sampleCategories,
                        this.fdr,
                        this.decoyFlag
                    );

                } catch (error) {
                    console.warn(error);
                    this.error = true;
                    this.errorMessage = `
                        An error occurred while parsing the input files you provided. Please make sure that the files
                        you provided are valid .pout-files produced by Percolator.
                    `;
                    return;
                }

                const peptPsmArray = [];
                for (const entry of pepPsm.entries()) {
                    const newSet = set();
                    for (const item of entry[1]) {
                        newSet.add(item);
                    }
                    peptPsmArray.push([entry[0], newSet]);
                }

                const protPeptArray = [];
                for (const entry of protPept.entries()) {
                    const newSet = set();
                    for (const peptide of entry[1]) {
                        newSet.add(peptide);
                    }
                    protPeptArray.push([entry[0], newSet]);
                }

                const peptProtArray = [];
                for (const entry of pepProt.entries()) {
                    const newSet = set();
                    for (const prot of entry[1]) {
                        newSet.add(prot);
                    }
                    peptProtArray.push([entry[0], newSet]);
                }

                let proteinGroups;
                let proteinSubgroups;

                try {
                    [proteinGroups, proteinSubgroups] = protein_grouping_analysis(
                        this.occam,
                        dict(protPeptArray),
                        dict(peptProtArray)
                    );
                } catch (e) {
                    this.error = true;
                    this.errorMessage = "An error occurred while performing the protein grouping analysis: " + e.message;
                    return;
                }


                try {
                    const groupFile = write_to_file(dict([...repCat]), proteinGroups, dict([...psmExp.entries()]), dict(peptPsmArray), dict(peptProtArray), dict(protPeptArray));
                    const subGroupFile = write_to_file(dict([...repCat]), proteinSubgroups, dict([...psmExp.entries()]), dict(peptPsmArray), dict(peptProtArray), dict(protPeptArray));

                    const zip = new JSZip();
                    zip.file("groups.tsv", groupFile);
                    zip.file("subgroups.tsv", subGroupFile);
                    this.zipResult = zip;
                } catch (e) {
                    this.error = true;
                    this.errorMessage = "An error occurred while trying to write the analysis results to a file."
                }
            }
        },
        downloadFiles: async function() {
            this.zipResult.generateAsync({type: "blob"}).then(function(content) {
                FileSaver.saveAs(content, "pout2prot.zip");
            });
        }
    }
}
</script>

<style>
    .settings-title {
        color: black;
        font-size: 18px;
    }

    .settings-important-text {
        font-style: italic;
        font-weight: bold;
        display: block;
    }
</style>
