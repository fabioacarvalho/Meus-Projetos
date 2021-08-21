<template>
    
    <v-container align-center class="text-center">
        <v-layout id="progress" align-center>
            <v-progress-circular  :rotate="360" :size="300" :width="15" :value="grafico" color="teal" > {{ minutos + ':' + segundos }} </v-progress-circular>
        </v-layout>
        <br>
        <v-layout align-center>
            <v-btn @click="timerSegundo" color="primary" depressed elevation="5" icon large outlined > > </v-btn>
            <v-btn @click="pause" color="primary" depressed elevation="5" icon large outlined > || </v-btn>
            <v-btn @click="stop" color="primary" depressed elevation="5" icon large outlined > [] </v-btn>
        </v-layout>
        
    </v-container>
</template>

<script>
  export default {
    data () {
      return {
        interval: {},
        segundos: 0,
        minutos: 25,
        grafico: 100
      }
    },
    beforeDestroy () {
      clearInterval(this.interval)
    },
    methods: {
        timerSegundo() {
            //this.timerMinuto()
            if(this.minutos === 25) {
                this.minutos = 24
                this.segundos = 59
            }
            
            this.interval = setInterval(() => {
                this.segundos -= 1
                if (this.segundos <= 0) {
                    this.minutos -= 1
                    this.segundos = 59
                    this.grafico -= 4
                //return (this.segundos = 0)
                } 
                if(this.minutos <= 0) {
                    this.minutos = 5
                    this.segundos = 0
                    alert('Descanse por 5 minutos!')
                    this.stop()
                }

            }, 1000)

            
        },
        pause() {
            clearInterval(this.interval)
        },
        stop() {
            clearInterval(this.interval)
            this.minutos = 25
            this.segundos = 0
            this.grafico = 100
        },
    },
    mounted () {
      
    },
  }
</script>

<style>
    .v-progress-circular {
        margin: 2rem;
        font-size: 5rem;
    }

    #progress {
        justify-items: center;
        align-content: center;
        align-items: center;
    }
</style>