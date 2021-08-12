<template>
    <v-container>
        <v-content>
            <v-row>
                <v-select v-model="obra" :items="listaObra" :error-messages="errors" label="Obra" data-vv-name="select" required></v-select>
                <v-select v-model="email" :items="person" :error-messages="errors" label="Arquiteto" data-vv-name="select" required></v-select>
                <v-select v-model="etapa" :items="items" :error-messages="errors" label="Etapa" data-vv-name="select" required></v-select>
            </v-row>
            <v-row>
                <v-btn @click="timer" class="white--text" depressed color="blue-grey darken-3" > Iniciar </v-btn>
                <v-btn @click="pause" depressed color="amber" > Pausar </v-btn>
                <v-btn @click="stop" depressed color="grey lighten-1" > Parar </v-btn>
                <v-btn @click="setData" class="white--text" depressed color="green lighten-1" > Registrar </v-btn>
            </v-row>
        </v-content>

        <v-layout class="timer-content" v-if="timerView">
                <row>
                    <p id="timer" > {{ hora + ':' + minutos + ':' + segundos }} </p>
                </row>
        </v-layout>

        <v-data-table
            :headers="headers"
            :items="desserts"
            :items-per-page="5"
            item-key="name"
            class="elevation-1"
            :footer-props="{
            showFirstLastPage: true,
            firstIcon: 'mdi-arrow-collapse-left',
            lastIcon: 'mdi-arrow-collapse-right',
            prevIcon: 'mdi-minus',
            nextIcon: 'mdi-plus'
            }"
        ></v-data-table>
        
    </v-container>  
</template>

<script>
export default {
    data: () => ({
        obra: '',
        etapa: '',
        email: '',
        listaObra: [
            'Obra 1',
            'Obra 2',
            'Obra 3',
        ],
        person: [
            'arquiteto(a)1',
            'arquiteto(a)2',
        ],
        items: [
            'Reunião Cliente',
            'Visita Obra',
            'Escopo Projeto',
            'Interiores',
        ],
        interval: {},
        segundos: 0,
        minutos: 0,
        hora: 0,
        timerView: false,
        data: [],
        fields: [
            { key: 'id', label: 'Código', sortable: true },
            { key: 'name', label: 'Nome', sortable: true },
            { key: 'description', label: 'Descrição', sortable: true },
            { key: 'actions', label: 'Ações'}
        ],
        headers: [
        {
            text: 'Dessert (100g serving)',
            align: 'start',
            value: 'name',
        },
        { text: 'Category', value: 'category' },
        ],
        desserts: [],
      
    }),
    methods: {
        timer() {
            this.timerView = true
            /* if(this.minutos === 25) {
                this.minutos = 24
                this.segundos = 59
            } */
            
            this.interval = setInterval(() => {
                //this.segundos += 1
                if (this.segundos <= 59) {
                    this.segundos += 10
                //return (this.segundos = 0)
                } 
                if(this.segundos == 60) {
                    this.minutos +=10
                    this.segundos = 0
                }
                if(this.minutos == 60) {
                    this.hora += 1
                    this.minutos = 0
                }

            }, 1000)

            
        },
        pause() {
            clearInterval(this.interval)
        },
        stop() {
            clearInterval(this.interval)
            this.minutos = 0
            this.segundos = 0
            this.hora = 0
            this.timerView = false
        },
        setData() {
            alert('Registrado: ' + this.obra + ', ' + this.email + ', ' + this.etapa + ` total: ${this.hora}h:${this.minutos}min:${this.segundos}s`)
            this.stop()
        },
        save() {
            this.desserts.push({ name: this.obra, category: this.etapa })
        }
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