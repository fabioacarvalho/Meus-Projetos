<template>
	<v-app>
		<v-content>
			<Header />
			<router-view></router-view>
		</v-content>
	</v-app>
</template>

<script>
import Header from './components/Header'

export default {
	components: { Header },
}
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

