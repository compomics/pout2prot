<template>
    <v-app>
        <v-app-bar
            app
            color="primary"
            dark
        >
            <v-app-bar-nav-icon @click="navigationDrawer = !navigationDrawer"></v-app-bar-nav-icon>
            <v-toolbar-title>Pout2Prot</v-toolbar-title>

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

        <v-navigation-drawer app v-model="navigationDrawer">
            <v-list-item>
                <v-list-item-content>
                    <v-list-item-title class="title">
                        MegaGO
                    </v-list-item-title>
                    <v-list-item-subtitle>
                        Compute similarity
                    </v-list-item-subtitle>
                </v-list-item-content>
            </v-list-item>

            <v-divider></v-divider>

            <v-list dense nav class="py-0 mt-4">
                <div v-for="item of links" :key="item.title">
                    <v-list-item v-if="'link' in item" link :to="item.link">
                        <v-list-item-icon>
                            <v-icon>{{ item.icon }}</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                            <v-list-item-title>{{ item.title }}</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </div>
            </v-list>
        </v-navigation-drawer>

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
        links: [
            {
                icon: "mdi-home",
                title: "Home",
                link: "/"
            },
            {
                icon: "mdi-console",
                title: "Documentation",
                link: "/docs"
            }
        ],
        navigationDrawer: false
    }),
};
</script>
