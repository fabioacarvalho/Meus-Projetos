<template>
    <v-toolbar max-height="65" color="#263238" app>
        <v-toolbar-title class=" mr-4">
            <img src="../assets/teste.png" width="180px" alt="png">
            <!-- <span class="font-weight-light white--text" >Plan</span> -->
        </v-toolbar-title>
        <v-toolbar-items >
            <v-btn color="#263238" class="white--text" flat to="/">Início</v-btn>
            <v-btn color="#263238" class="white--text" flat to="/relatorio">Relatorio</v-btn>
            <v-btn color="#263238" class="white--text" flat to="/">Cadastros</v-btn>
        </v-toolbar-items>

        <v-spacer></v-spacer>

        <v-toolbar-items>
            <v-btn color="#263238" class="white--text" flat >SAIR</v-btn>
        </v-toolbar-items>
    </v-toolbar>
</template>

<script>
export default {
    name: 'Header',
    data() {
        
    },
}
</script>

<style>

</style>
