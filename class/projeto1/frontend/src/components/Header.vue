<template>
    <v-toolbar app color="blue-grey darken-3">
        <v-toolbar-title  class="headline text-uppercase mr-4">
            <span >Studio</span>
            <span class="font-weight-light" >Claassen</span>
        </v-toolbar-title>
        <v-toolbar-items >
            <v-btn class="white--text" flat to="/">Início</v-btn>
            <v-btn class="white--text" flat to="/pomodoro">Pomorodo</v-btn>
            <v-btn class="white--text" flat to="/dashboard">Dashboard</v-btn>
            <v-btn class="white--text" flat to="/table">Tabela</v-btn>
            <v-btn class="white--text" flat to="/table">Cadastro</v-btn>
        </v-toolbar-items>

        <v-spacer></v-spacer>

        <v-toolbar-items>

            <v-menu offset-y>
                <v-btn class="white--text" flat slot="activator"> Salvar & Carregar</v-btn>
                <v-list>
                    <v-list-tile >
                        <v-list-tile-title >Salvar Dados</v-list-tile-title>
                    </v-list-tile>
                    <v-list-tile >
                        <v-list-tile-title>Carregar Dados</v-list-tile-title>
                    </v-list-tile>
                </v-list>
            </v-menu>
            <v-layout align-center>
                <span class="text-uppercase grey--text text--darken-2"> {{  }}</span>
            </v-layout>
        </v-toolbar-items>
    </v-toolbar>
</template>

<script>
export default {

}
</script>

<style>
    span {
        color: white;
    }
</style>