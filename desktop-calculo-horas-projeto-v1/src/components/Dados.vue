<template>
    <div>
        <h1>Registro de Horas</h1>
		<b-alert show dismissible v-for="mensagem in mensagens" :key="mensagem.texto" :variant="mensagem.tipo">{{ mensagem.texto }}</b-alert>
		<b-card>
            <h4>Cadastro de tempoDosProjetos</h4>
			<b-form-group label="Código Obra:">
				<b-form-input id="textno" type="text" size="lg" v-model="tempoProjeto.codObra" placeholder="Informe o código da obra" required></b-form-input>
			</b-form-group>
			<b-form-group label="Nome Cliente:">
				<b-form-input id="textno" type="text" size="lg" v-model="tempoProjeto.nomecliente" placeholder="Informe seu nome" required></b-form-input>
			</b-form-group>
			<b-form-group label="Nome:">
				<b-form-input id="textno" type="text" size="lg" v-model="tempoProjeto.nome" placeholder="Informe seu nome" required></b-form-input>
			</b-form-group>
			<b-form-group label="Hora Inicio:">
				<b-form-input id="textno" type="time" size="lg" v-model="tempoProjeto.inicio" placeholder="Informe o horário de início" required></b-form-input>
			</b-form-group>
			<b-form-group label="Hora Fim:">
				<b-form-input id="textno" type="time" size="lg" v-model="tempoProjeto.fim" placeholder="Informe o horário de fim" required></b-form-input>
			</b-form-group>
			<b-form-group label="Tempo Parado:">
				<b-form-input type="time" size="lg" v-model="tempoProjeto.tempoParado" placeholder="Informe seu tempo parado" required></b-form-input>
			</b-form-group>
			<b-form-group label="Data:">
				<b-form-input type="date" size="lg" v-model="tempoProjeto.data" placeholder="Informe a data" required></b-form-input>
			</b-form-group>
			<hr>
			<b-button @click="salvarNovoRegistro" size="lg" variant="primary">Salvar</b-button>

			<b-button @click="obterListatempoDosProjetos" size="lg" variant="success" class="ml-4">Obter Registros</b-button>
            <b-button variant="danger" size="lg" class="ml-4" @click="limpar">Limpar</b-button>
		</b-card>
		<hr>
		<b-list-group>
			<b-list-group-item v-for="(dadosprojeto, id) in tempoDosProjetos" :key="id">
				<strong>Data:</strong> {{ dadosprojeto.data }} | <strong>Código Obra:</strong> {{ dadosprojeto.codObra }} | <strong>Nome:</strong> {{ dadosprojeto.nome }} | <strong>Nome Cliente:</strong> {{ dadosprojeto.nomecliente }} <br>
                <strong>Inicio:</strong> {{ dadosprojeto.inicio }} | <strong>Fim:</strong> {{ dadosprojeto.fim }} | <strong>Tempo Parado:</strong> {{ dadosprojeto.tempoParado }} | <strong>Id:</strong> {{ id }} <br>
				<b-button variant="warning" size="lg" @click="editartempoDosProjetos(id)">Editar</b-button>
				<b-button variant="danger" size="lg" class="ml-4" @click="excluir(id)">Excluir</b-button>
			</b-list-group-item>
		</b-list-group>
    </div>
</template>

<script>
export default {
    data() {
		return {
			mensagens: [],
			tempoDosProjetos: [],
			id: null,
			tempoProjeto: {
                codObra: '',
				nome: '',
                nomecliente: '',
                inicio: '',
                fim: '',
				tempoParado: '',
                data: ''
			}

		}
	},
    methods: {
        salvarNovoRegistro() {
            const metodo = this.id ? 'patch' : 'post'
            const finalUrl = this.id ? `/${this.id}.json` : '.json'
			
            this.$apitempodosporjetos[metodo](`/tempoDosProjetos${finalUrl}`, this.tempoProjeto).then(() => {
                this.limpar()
                this.obterListatempoDosProjetos()
                this.mensagens.push({
						texto: 'Novo Registro adicionado com sucesso!',
						tipo: 'success'
                })
            })
        },
        obterListatempoDosProjetos() {
            this.$apitempodosporjetos.get('tempoDosProjetos.json').then(res => {
				this.tempoDosProjetos = res.data // A resposta de insira no array tempoDosProjetos
			})
        },
        editartempoDosProjetos(id) {
            this.id = id
			this.tempoProjeto = { ...this.tempoDosProjetos[id]}
        },
        limpar() {
			this.tempoProjeto.codObra = ''
            this.tempoProjeto.nome = ''
            this.tempoProjeto.nomecliente = ''
            this.tempoProjeto.inicio = ''
            this.tempoProjeto.fim = ''
            this.tempoProjeto.tempoParado = ''
            this.tempoProjeto.data = ''
			this.id = null
			this.mensagens = []
		},
        excluir(id) {
			this.$apitempodosporjetos.delete(`/tempoDosProjetos/${id}.json`).then(() => {
				this.limpar()
				this.obterListatempoDosProjetos()
				})
			.catch(err => {
				this.mensagens.push({
					texto: 'Problema para excluir',
					tipo: 'danger'
				})
			})
		}
    }

}
</script>

<style>

</style>