<template>
    <v-container fluid>
        <!-- <v-btn @click="obterUsuario">Carregar</v-btn> -->

        <v-simple-table height="80vh">
            <template v-slot:default>
                <thead>
                    <tr>
                    <th class="text-left text-uppercase white--text">
                        Cliente
                    </th>
                    <th class="text-left text-uppercase white--text">
                        Etapa
                    </th>
                    <th class="text-left text-uppercase white--text">
                        Data
                    </th>
                    <th class="text-left text-uppercase white--text">
                        Tempo
                    </th>
                    <th class="text-left text-uppercase white--text">
                        Ark
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
                    <td>{{ item.arquiteto }}</td>
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

<style>
    th {
        background: #263238;
    }
</style>