<template>
  <v-app>
    <v-app-bar
      app
      color="#263238"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="./assets/teste.png"
          transition="scale-transition"
          width="130"
        />
        

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src=""
          width="100"
        />
      </div>

      <v-spacer></v-spacer>

      <span v-if="acesso == true" class="mr-2"><strong><a @click="acesso = false">SAIR</a></strong></span>
    </v-app-bar>

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

    <v-container v-if="acesso == true">
      <v-main  class="mx-5">
        <Login />
        <Toggle />
      </v-main>
    </v-container>
  </v-app>
</template>

<script>
import Toggle from './components/Toggle.vue';

export default {
  name: 'App',
  components: {
    Toggle,

  },
  data () {
    return {
      acesso: false,
      user: {email: '', senha: ''},
    }
  },
  methods: {
    signIn () {
    console.log(this.user)
    if(this.user.email == 'arquitetura@claassen.com.br' && this.user.senha == 'arquitetura1030') {
      this.acesso = true
    } else {
      alert('Usuario invalido!!')
    }
  },
  }
};
</script>
