<template>
  <v-container  fluid >
        <v-container v-if="acesso == false" fluid class="mt-10">
      <v-row class="px-16 mx-16 mt-10" >
        <v-text-field
          v-model="user.email"
          :rules="emailRules"
          label="E-mail"
          required
        ></v-text-field>
      </v-row>
      <v-row class="px-16 mx-16 mt-10" >
        <v-text-field
          v-model="user.senha"
          :rules="senhaRules"
          label="Senha"
          required
          type="password"
        ></v-text-field>
      </v-row>
      <v-row class="px-16 mx-16 mt-10" >
        <v-btn color="success" class="mr-4" @click="signIn" >
          Entrar
        </v-btn>
      </v-row>
    </v-container>
  </v-container>
</template>

<script>
  export default {
    name: 'Login',
    data () {
      return {
        acesso: true,
        user: {email: '', senha: ''},
      }
    },
    methods: {
      signIn () {
      console.log(this.user)
      if(this.user.email == 'arquitetura@claassen.com.br' && this.user.senha == 'arquitetura1030') {
        this.acesso = true
      } else if (this.user.email == 'engenharia@claassen.com.br' && this.user.senha == 'engenharia1030') {
        this.acesso = true
      } else {
        alert('Usuario invalido!!')
      }
    },
    }
  };
</script>
