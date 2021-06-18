<template>
    <v-container>
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
                    <v-stepper-step :complete="currentStep > 1" step="1">
                        Select all input files
                        <small>This application only accepts .pout-files</small>
                    </v-stepper-step>
                    <v-stepper-content step="1">
                        <v-file-input v-model="files" multiple></v-file-input>
                        <div class="d-flex mt-2">
                            <v-btn class="ml-auto" color="primary" @click="currentStep = 2">
                                Continue
                            </v-btn>
                        </div>
                    </v-stepper-content>
                    <v-stepper-step :complete="currentStep > 2" step="2">
                        Configure experiment names
                    </v-stepper-step>
                    <v-stepper-content step="2">
                        <v-simple-table>
                            <template v-slot:default>
                                <thead>
                                    <tr>
                                        <th class="text-left">File</th>
                                        <th class="text-left">Experiment name</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="(file, idx) in files" :key="file.name">
                                        <td>{{ file.name }}</td>
                                        <td>
                                            <v-text-field v-model="experimentNames[idx]">
                                            </v-text-field>
                                        </td>
                                    </tr>
                                </tbody>
                            </template>
                        </v-simple-table>

                        <div class="d-flex mt-2">
                            <v-btn text @click="currentStep = 1">
                                Go back
                            </v-btn>
                            <v-btn class="ml-auto" color="primary" @click="currentStep = 3">
                                Start analysis
                            </v-btn>
                        </div>
                    </v-stepper-content>
                    <v-stepper-step :complete="currentStep > 3" step="3">
                        View results
                    </v-stepper-step>
                    <v-stepper-content step="3">
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
import { set, dict } from '@/business/processing/org.transcrypt.__runtime__.js'
import Parser from "@/business/processing/Parser";

export default {
    name: 'HomePage',

    data: () => ({
        files: [],
        experimentNames: [],
        currentStep: 1
    }),

    watch: {
        // Process newly uploaded file and start the parser.
        files: function(newValue) {
            // const fileReader = new FileReader();
            this.experimentNames.splice(0, this.experimentNames.length);
            for (const file of this.files) {
                this.experimentNames.push(file.name);
            }


            // console.log(newValue.name);

            // fileReader.onload = function(stats) {
            //     console.log(stats);
            //     console.log(fileReader.result);
            //
            //     protein_grouping_analysis(false, [], []);
            // }

            // fileReader.readAsText(newValue, "utf-8");
        }
    },

    methods: {
        startAnalysis: async function() {
            if (this.files) {
                const [
                    psmExp, pepPsm, pepProt, protPept, repCat
                ] = await Parser.parseFiles(this.files, ["a", "b"], 0.05, "False");

                const protPeptArray = [];
                for (const entry of protPept.entries()) {
                    protPeptArray.push([entry[0], set(entry[1])]);
                }

                const peptProtArray = [];
                for (const entry of peptProtArray.entries()) {
                    peptProtArray.push([entry[0], set(entry[1])]);
                }

                const [proteinGroups, proteinSubgroups] = protein_grouping_analysis(false, dict(protPeptArray), dict(peptProtArray));
                console.log(proteinGroups.py_values());
            }
        }
    }
}
</script>
