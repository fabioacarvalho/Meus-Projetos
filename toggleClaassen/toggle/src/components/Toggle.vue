<template>
  
  <v-container fluid>


    <v-row>
      <v-col
        cols="12"
        md="4"
      >
        <v-btn color="success" to="/registro">REGISTRO MANUAL</v-btn>
      </v-col>
    </v-row>
    <br>
    <hr>
    <h1>TOGGL</h1>

    <v-container v-if="toggl == false">
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
      </v-container>
      <!-- TIMER -->
      <v-row class="ma-auto" v-if="timerView == false" >
        <v-btn color="secondary" @click="timer" :disabled="order.arquiteto == '' || order.etapa == '' || order.cliente == '' || order.data == ''">Iniciar</v-btn>
      </v-row>
      <v-card v-if="timerView == true" class="mx-auto" max-width="344" outlined >
        <v-list-item three-line>
          <v-list-item-content>
            <div class="text-overline mb-4">
              {{ 'Cliente: ' + order.cliente }}
            </div>
            <v-list-item-title class="text-h2 mb-1">
              {{ hora + ':' + minutos + ':' + segundos }}
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <!-- BOTÕES -->
        <v-card-actions>
          <v-btn color="red darken-4" outlined rounded text @click="stop">Sair</v-btn>
          <v-btn color="warning" outlined rounded text @click="pause">Parar</v-btn>
          <v-btn color="primary" outlined rounded text @click="salvar">Salvar</v-btn>
        </v-card-actions>
      </v-card>
      <br>
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
          timeInicio: '',
          timeFim: '',
          tempoProjeto: ''
        },
        activePicker: null,
        timerView: false,
        date: null,
        menu1: false,
        modal1: false,
        menu2: false,
        modal2: false,
        acesso: true,
        interval: {},
        segundos: 0,
        minutos: 0,
        hora: 0,
        valid: true,

        registro: false,
        toggl: false,
        
        emailRules: [
          v => !!v || 'E-mail is required',
          v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
        ],
        senhaRules: [
          v => !!v || 'Password is required'
        ],
        
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
          tempoProjeto: ''
        }
        this.minutos = 0
        this.segundos = 0
        this.hora = 0
        this.timerView = false
      },
      timer() {
        this.timerView = true
        /* if(this.minutos === 25) {
            this.minutos = 24
            this.segundos = 59
        } */

        var agora = new Date

        this.order.timeInicio = `${agora.getHours()}:${agora.getMinutes()}:${agora.getSeconds()}`


        this.interval = setInterval(() => {
            //this.segundos += 1
            if (this.segundos <= 59) {
                this.segundos += 1
            //return (this.segundos = 0)
            } 
            if(this.segundos == 60) {
                this.minutos +=1
                this.segundos = 0
            }
            if(this.minutos == 60) {
                this.hora += 1
                this.minutos = 0
            }

        }, 1000)
      },
      pause() {
        var agora = new Date

        this.order.timeFim = `${agora.getHours()}:${agora.getMinutes()}:${agora.getSeconds()}`

        this.order.tempoProjeto = `${this.hora}:${this.minutos}:${this.segundos}`
        
        clearInterval(this.interval)
        
      },
      stop() {
        clearInterval(this.interval)
        this.minutos = 0
        this.segundos = 0
        this.hora = 0
        this.timerView = false
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

<style>
  #timer {
    font-size: 10rem;

  }

  .timer-content {
    padding-top: 25px;
    align-content: center;
    justify-content: center;
  }

  p {
    align-items: center;
    padding: 10px 40px;
    background-color: rgb(228, 228, 228);
    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.15);
    border-radius: 10px;
    color: #37474F;
    font-family: Arial, Helvetica, sans-serif;
  }
</style>