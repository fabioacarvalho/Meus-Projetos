<template>
    <!-- <v-col v-for="item in desserts" :key="item.name"> -->
    <v-sparkline
        :value="value"
        :gradient="gradient"
        :smooth="radius || false"
        :padding="padding"
        :line-width="width"
        :stroke-linecap="lineCap"
        :gradient-direction="gradientDirection"
        :fill="fill"
        :type="type"
        :auto-line-width="autoLineWidth"
        auto-draw
    ></v-sparkline>
</template>

<script>

    const gradients = [
        '#FFF'
    ]

  export default {
    data: () => ({
      width: 2,
      radius: 10,
      padding: 8,
      lineCap: 'round',
      gradient: gradients[5],
      value: [0, 2, 5, 9, 5, 10, 3, 5, 0, 0, 1, 8, 2, 9, 0],
      gradientDirection: 'top',
      gradients,
      fill: false,
      type: 'trend',
      autoLineWidth: false,
      desserts: [],

    }),
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