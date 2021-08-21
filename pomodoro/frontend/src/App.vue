<template>
  <v-app>
    <v-main>
      <Pomodoro/>
    </v-main>
  </v-app>
</template>

<script>
import Pomodoro from './components/Pomodoro';

export default {
  name: 'App',

  components: {
    Pomodoro,
  },

  data: () => ({
    //
  }),
};
</script>
