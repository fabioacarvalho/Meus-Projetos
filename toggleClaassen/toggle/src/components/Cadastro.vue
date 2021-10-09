<template>
  <v-form v-model="valid">
    <v-container>
      <v-row>
        <v-col
          cols="12"
          md="8"
        >
          <v-text-field
            v-model="firstname"
            label="Nome Arquiteto"
            required
          ></v-text-field>
        </v-col>
        <v-col
          cols="12"
          md="4"
        >
          <v-btn color="primary">SALVAR ARK</v-btn>
        </v-col>
      </v-row>

      <v-row>
        <v-col
          cols="12"
          md="8"
        >
          <v-text-field
            v-model="lastname"
            label="Nome Etapa"
            required
          ></v-text-field>
        </v-col>
        <v-col
          cols="12"
          md="4"
        >
          <v-btn color="primary">SALVAR ETAPA</v-btn>
        </v-col>
      </v-row>

      <v-row>
        <v-col
          cols="12"
          md="8"
        >
          <v-text-field
            v-model="email"
            label="Nome Cliente"
            required
          ></v-text-field>
        </v-col>
        <v-col
          cols="12"
          md="4"
        >
          <v-btn color="primary">SALVAR CLIENTE</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
  export default {
    data: () => ({
      valid: false,
      firstname: '',
      lastname: '',
      email: '',

    }),
  }
</script>