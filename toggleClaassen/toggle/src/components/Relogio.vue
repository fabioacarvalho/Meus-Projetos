<template>
    <v-container fluid>
        <v-btn @click="obterUsuario">Carregar</v-btn>

        <v-simple-table height="300px">
            <template v-slot:default>
                <thead>
                    <tr>
                    <th class="text-left">
                        Cliente
                    </th>
                    <th class="text-left">
                        Etapa
                    </th>
                    <th class="text-left">
                        Data
                    </th>
                    <th class="text-left">
                        Tempo
                    </th>
                    </tr>
                </thead>
                <tbody>
                    <tr
                    v-for="item in desserts"
                    :key="item.name"
                    >
                    <td>{{ item.cliente }}</td>
                    <td>{{ item.etapa }}</td>
                    <td>{{ item.data }}</td>
                    <td>{{ item.tempoProjeto }}</td>
                    </tr>
                </tbody>
            </template>
        </v-simple-table>
    </v-container>
</template>

<script>
  export default {
    data () {
      return {
        desserts: [
          
        ],
      }
    },
    methods: {
        obterUsuario() {
            this.$http.get('tempo.json').then(res => { this.desserts = res.data })
        }
    },
    created() {
        this.obterUsuario()
    }
    
  }
</script>