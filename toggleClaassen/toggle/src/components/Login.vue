<template>
  <v-container  fluid >
    <v-container >
      <v-img class="mx-auto" src="../assets/Logo-Claassen.png" max-width="100px"></v-img>
    </v-container>
    <v-container  fluid class="mt-2">
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
        <v-btn color="success" class="mr-4"  @click="signIn" >
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
        user: {email: '', senha: ''},
      }
    },
    methods: {
      signIn () {
        console.log(this.user)
        if(this.user.email == 'arquitetura@claassen.com.br' && this.user.senha == 'arquitetura1030') {
          this.$store.state.acesso = true
        } else if (this.user.email == 'engenharia@claassen.com.br' && this.user.senha == 'engenharia1030') {
          this.$store.state.acesso = true
        } else {
          alert('Usuario invalido!!')
        }
      },
    },
    computed: {
      acesso() {
        return this.$store.state.acesso
      }
    }
  };
</script>
