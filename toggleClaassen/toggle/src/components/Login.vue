<template>
  <v-container  fluid >
        <v-row class="px-16 mx-16 mt-10" >
            <v-text-field
                v-model="user.email"
                label="E-mail"
                required
            ></v-text-field>
        </v-row>
        <v-row class="px-16 mx-16 mt-10" >
            <v-text-field
                v-model="user.senha"
                label="Senha"
                required
                type="password"
            ></v-text-field>
        </v-row>
        <v-row class="px-16 mx-16 mt-10" >
            <v-btn v-bind:user="this.user" color="success" class="mr-4" @click="validate" >
                Entrar
            </v-btn>
        </v-row>
  </v-container>
</template>

<script>

  export default {
    data: () => ({
      valid: true,
      user: {email: '', senha: ''},
      
    }),

    methods: {
        validate () {
          //this.user.email == 'arquitetura@claassen.com.br' && this.user.senha == 'arquitetura1030' 
        },
    },
  }
</script>