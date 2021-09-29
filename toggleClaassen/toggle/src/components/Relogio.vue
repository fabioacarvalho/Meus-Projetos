<template>
    <v-row>
        <v-col cols="11" sm="5" >
            <v-dialog ref="dialog" v-model="modal1" :return-value.sync="time" persistent width="290px" >
                <template v-slot:activator="{ on, attrs }">
                <v-text-field v-model="timeInicio" label="Horario Início" prepend-icon="mdi-clock-time-four-outline" readonly v-bind="attrs" v-on="on" ></v-text-field>
                </template>
                <v-time-picker v-if="modal1" v-model="timeInicio" full-width >
                <v-spacer></v-spacer>
                <v-btn text color="primary" @click="modal1 = false" > Cancel </v-btn>
                <v-btn text color="primary" @click="$refs.dialog.save(timeInicio)" >  OK </v-btn>
                </v-time-picker>
            </v-dialog>
        </v-col>
        
        <v-col cols="11" sm="5" >
            <v-dialog ref="dialog" v-model="modal2" :return-value.sync="time" persistent width="290px" >
                <template v-slot:activator="{ on, attrs }">
                <v-text-field v-model="timeFim" label="Horario Fim" prepend-icon="mdi-clock-time-four-outline" readonly v-bind="attrs" v-on="on" ></v-text-field>
                </template>
                <v-time-picker v-if="modal2" v-model="timeFim" full-width >
                <v-spacer></v-spacer>
                <v-btn text color="primary" @click="modal2 = false" > Cancel </v-btn>
                <v-btn text color="primary" @click="$refs.dialog.save(timeFim)" >  OK </v-btn>
                </v-time-picker>
            </v-dialog>
        </v-col>
    </v-row>
</template>

<script>
  export default {
    data () {
      return {
        timeInicio: null,
        timeFim: null,
        menu1: false,
        modal1: false,
        menu2: false,
        modal2: false,
      }
    },
  }
</script>