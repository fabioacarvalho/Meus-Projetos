<template>
  <v-container >
    <h1>REGISTRO</h1>
    <v-container v-if="timerView == false" fluid>
      <v-row>
        <v-col cols="12">
          <v-combobox
            v-model="order.arquiteto"
            :items="items"
            label="Arquiteto"
            outlined
            dense
          ></v-combobox>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12">
          <v-combobox
            v-model="order.etapa"
            :items="valoresEtapa"
            label="Etapa"
            outlined
            dense
          ></v-combobox>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12">
          <v-combobox v-model="order.cliente" :items="valoresCliente" label="Cliente" outlined dense ></v-combobox>
        </v-col>
      </v-row>
      <v-row >
        <v-menu
          ref="menu2"
          v-model="menu2"
          :close-on-content-click="false"
          transition="scale-transition"
          offset-y
          min-width="auto"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="order.data"
              label="Data do Registro"
              prepend-icon="mdi-calendar"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
            v-model="order.data"
            :active-picker.sync="activePicker"
            :max="(new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10)"
            min="1950-01-01"
          ></v-date-picker>
        </v-menu>
      </v-row>
      <v-row>
        <v-text-field 
          v-model="order.tempoProjeto"
          label="Tempo Projeto"
          prepend-icon="mdi-clock-time-four-outline"
          type="time"
        ></v-text-field>
      </v-row>
      <v-row class="ma-auto" >
        <v-btn color="secondary" @click="salvar" :disabled="order.arquiteto == '' || order.etapa == '' || order.cliente == '' || order.data == '' || order.tempoProjeto == '' ">Registrar</v-btn>
      </v-row>
      
    </v-container>
  </v-container>
</template>


<script>
  export default {
    data () {
      return {
        order: {
          arquiteto: '',
          cliente: '',
          etapa: '',
          data: '',
          tempoProjeto: ''
        },
        activePicker: null,
        timerView: false,
        date: null,
        menu1: false,
        modal1: false,
        menu2: false,
        modal2: false,
      }
    },
    methods: {
      salvar() {
        this.$http.post(`/tempo.json`, this.order)
          .then(() => {
            this.clear()

          })
      },
      clear() {
        this.order = {
          arquiteto: '',
          cliente: '',
          etapa: '',
          data: '',
          tempoProjeto: ''
        }

      },
    },
    computed: {
        items() {
            return this.$store.state.items
        },
        valoresEtapa() {
            return this.$store.state.valoresEtapa
        },
        valoresCliente() {
            return this.$store.state.valoresCliente
        },
    }
  
  }
</script>