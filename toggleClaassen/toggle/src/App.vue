<template>
  <v-app>
    <Header v-if="acesso == true" />
	<Login v-if="acesso == false" />
    <v-main v-if="acesso == true">
			<v-container>
				<transition name="slide" mode="out-in">
					<router-view></router-view>
				</transition>
			</v-container>
		</v-main>
  </v-app>
</template>

<script>
import Header from './components/Header.vue'
import Login from './components/Login.vue'

export default {
  name: 'App',
  components: {
    Login,
    Header,
  },
  computed: {
	acesso() {
		return this.$store.state.acesso
	}
  }
};
</script>

<style>
  @keyframes slide-in {
		from { transform: translateY(-30px); opacity: 0; }
		to { transform: translateY(0px); opacity: 1; }
	}

	@keyframes slide-out {
		from { transform: translateY(0px); opacity: 1; }
		to { transform: translateY(-30px); opacity: 0; }
	}

	.slide-enter-active {
		animation: slide-in 0.3s ease;
	}

	.slide-leave-active {
		animation: sldie-out 0.3s ease;
	}

</style>
