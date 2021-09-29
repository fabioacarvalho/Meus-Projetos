<template>
  <v-app>
    <v-app-bar
      app
      color="#263238"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="./assets/teste.png"
          transition="scale-transition"
          width="130"
        />
        

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src=""
          width="100"
        />
      </div>

      <v-spacer></v-spacer>

      <span class="mr-2"><strong>TOGGLE</strong> CLAASSEN</span>
    </v-app-bar>

    <v-main>
      <toggle/>
    </v-main>
  </v-app>
</template>

<script>
import Toggle from './components/Toggle.vue';

export default {
  name: 'App',

  components: {
    Toggle

  },

  data: () => ({
    //
  }),
};
</script>
