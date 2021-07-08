<template>
    <v-app>
        <v-app-bar
            app
            color="primary"
            dark
        >
            <div class="d-flex align-center">
                <span class="font-weight-bold">
                  Pout2Prot
                </span>
            </div>

            <v-spacer></v-spacer>

            <v-btn
                href="https://github.com/tivdnbos/proteingrouping"
                target="_blank"
                text
            >
                <span class="mr-2">Find us on GitHub</span>
                <v-icon>mdi-open-in-new</v-icon>
            </v-btn>
        </v-app-bar>

        <v-main>
            <router-view/>
        </v-main>
        <v-footer padless>
            <v-card flat tile class="grey lighten-3 text-center" style="width: 100%;">
                <v-card-text>
                    <div class="d-flex justify-center" style="width: 100%;">
                        <v-img src="@/assets/logo.png" max-width="75" max-height="75">
                        </v-img>
                    </div>
                    <v-divider class="my-2"></v-divider>
                    {{ new Date().getUTCFullYear() }} — <strong>Pout2Prot</strong>
                </v-card-text>
            </v-card>
        </v-footer>
    </v-app>
</template>

<script>
export default {
    name: 'App',

    components: {},

    data: () => ({
        //
    }),
};
</script>
