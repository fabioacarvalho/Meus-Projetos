<template>
    <v-toolbar max-height="65" color="#263238" >
        <v-toolbar-title class=" mr-4">
            <img src="../assets/teste.png" width="180px" alt="png">
            <!-- <span class="font-weight-light white--text" >Plan</span> -->
        </v-toolbar-title>
        <v-toolbar-items >
            <v-btn color="#263238" class="white--text" text to="/">Início</v-btn>
            <v-btn color="#263238" class="white--text" text to="/relatorio">Relatorio</v-btn>
            <v-btn color="#263238" class="white--text" text to="/cadastro">Cadastros</v-btn>
            <v-btn color="#263238" class="white--text" text to="/dashboard">Dashboard</v-btn>
        </v-toolbar-items>

        <v-spacer></v-spacer>

        <v-toolbar-items>
            <v-btn color="#263238" class="white--text" text @click="signOut" >SAIR</v-btn>
        </v-toolbar-items>
    </v-toolbar>
</template> 

<script>

export default {
    name: 'Header',
    data() {
        return {

        }
    },
    methods: {
        signOut() {
            this.$store.state.acesso = false
        }
    },
    computed: {
      acesso() {
        return this.$store.state.acesso
      }
    }
}
</script>

<style>

</style>
