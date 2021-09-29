<template>
  <v-container fluid>
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
        <v-combobox
          v-model="order.cliente"
          :items="valoresCliente"
          label="Cliente"
          
          outlined
          dense
        ></v-combobox>
      </v-col>
    </v-row>

    <v-row >
      <v-menu
        ref="menu"
        v-model="menu"
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
          @change="save"
        ></v-date-picker>
      </v-menu>
    </v-row>

    <!-- RELÓGIO -->

    <v-row>
      <v-col cols="11" sm="5" >
        <v-dialog ref="dialog" v-model="modal1" :return-value.sync="time" persistent width="290px" >
          <template v-slot:activator="{ on, attrs }">
          <v-text-field v-model="order.timeInicio" label="Horario Início" prepend-icon="mdi-clock-time-four-outline" readonly v-bind="attrs" v-on="on" ></v-text-field>
          </template>
          <v-time-picker v-if="modal1" v-model="order.timeInicio" full-width >
          <v-spacer></v-spacer>
          <v-btn text color="primary" @click="modal1 = false" > Cancel </v-btn>
          <v-btn text color="primary" @click="$refs.dialog.save(order.timeInicio)" >  OK </v-btn>
          </v-time-picker>
        </v-dialog>
      </v-col>
      
      <v-col cols="11" sm="5" >
          <v-dialog ref="dialog" v-model="modal2" :return-value.sync="time" persistent width="290px" >
              <template v-slot:activator="{ on, attrs }">
              <v-text-field v-model="order.timeFim" label="Horario Fim" prepend-icon="mdi-clock-time-four-outline" readonly v-bind="attrs" v-on="on" ></v-text-field>
              </template>
              <v-time-picker v-if="modal2" v-model="order.timeFim" full-width >
              <v-spacer></v-spacer>
              <v-btn text color="primary" @click="modal2 = false" > Cancel </v-btn>
              <v-btn text color="primary" @click="$refs.dialog.save(order.timeFim)" >  OK </v-btn>
              </v-time-picker>
          </v-dialog>
      </v-col>
    </v-row>

    <v-row>
      <v-btn color="primary" @click="salvar">Salvar</v-btn>
    </v-row>

  
    
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
          timeInicio: '',
          timeFim: '',
        },
        items: [
          'Cristina',
          'Carol',
          'Isabely',
          'Guilherme',
          'Karen'
        ],
        valoresEtapa: [
          'Levantamento/Briefing/Digitalização',
          'PM - Processo Criativo',
          'PM - Renderização + Apresentação',
          'Adequações',
          'Projeto Legal',
          'Projeto Executivo',
          'Projeto Executivo Mobiliário',
          'Assessoria para compras',
        ],
        valoresCliente: [
          'Rafael Melcher',
          'Altemisa Carneiro',
          'Luis Gabriel ',
          'Andrea e Paulo',
          'Anderson Primo',
          'Rafael Gamballi',
          'Lincoln Taylor',
          'Letícia Locatelli',
          'Nelson Carvalho',
          'Caio Luiz Vital',
          'Carlos Zimmer',
          'Dulce Osinski',
          'Paulo Vizzotto',
          'Eunice Chavinski',
          'Ana Maria Schwarz',
          'Bruno Carvalho',
          'Renata de Paula',
          'runo Peruzzo de Pádua',
          'aniel Bucheb',
          'oris Karam',
          'aroline Borba',
          'ábio Cunha',
          'eivid Dias',
          'Vânia Muniz Nequer',
          'Jair de Azevedo',
          'ristiane Magliari',
          'Bruno Prazeres',
        ],
        activePicker: null,
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
          timeInicio: '',
          timeFim: '',
        }
      }
    }
  }
</script>

<style>

</style>