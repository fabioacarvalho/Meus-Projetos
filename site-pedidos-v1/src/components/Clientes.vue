<template>
    <div>
        <h1>Clientes</h1>
		<b-alert show dismissible v-for="mensagem in mensagens" :key="mensagem.texto" :variant="mensagem.tipo">{{ mensagem.texto }}</b-alert>
		<b-card>
            <h4>Cadastro de Clientes</h4>
			<b-form-group label="Código Obra:">
				<b-form-input id="textno" type="text" size="lg" v-model="cliente.codObra" placeholder="Informe o código da obra" required></b-form-input>
			</b-form-group>
			<b-form-group label="Nome:">
				<b-form-input id="textno" type="text" size="lg" v-model="cliente.nome" placeholder="Informe seu nome" required></b-form-input>
			</b-form-group>
			<b-form-group label="Endereço:">
				<b-form-input id="textno" type="text" size="lg" v-model="cliente.endereco" placeholder="Informe seu endereço" required></b-form-input>
			</b-form-group>
			<b-form-group label="Contato:">
				<b-form-input id="textno" type="number" size="lg" v-model="cliente.telefone" placeholder="Informe seu número de telefone" required></b-form-input>
			</b-form-group>
			<b-form-group label="E-mail:">
				<b-form-input type="email" size="lg" v-model="cliente.email" placeholder="Informe seu email" required></b-form-input>
			</b-form-group>
			<b-form-group label="Data:">
				<b-form-input type="date" size="lg" v-model="cliente.data" placeholder="Informe a data" required></b-form-input>
			</b-form-group>
			<hr>
			<b-button @click="salvarNovoCliente" size="lg" variant="primary">Salvar</b-button>

			<b-button @click="obterListaClientes" size="lg" variant="success" class="ml-4">Obter Clintes</b-button>
            <b-button variant="danger" size="lg" class="ml-4" @click="limpar">Limpar</b-button>
		</b-card>
		<hr>
		<b-list-group>
			<b-list-group-item v-for="(dadoscliente, id) in clientes" :key="id">
				<strong>Data:</strong> {{ dadoscliente.data }} | <strong>Código Obra:</strong> {{ dadoscliente.codObra }} | <strong>Nome:</strong> {{ dadoscliente.nome }} <br>
                <strong>Endereço:</strong> {{ dadoscliente.endereco }} | <strong>Contato:</strong> {{ dadoscliente.telefone }} | <strong>E-mail:</strong> {{ dadoscliente.email }} | <strong>Id:</strong> {{ id }} <br>
				<b-button variant="warning" size="lg" @click="editarCliente(id)">Editar</b-button>
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
			clientes: [],
			id: null,
			cliente: {
                codObra: '',
				nome: '',
                endereco: '',
                telefone: '',
				email: '',
                data: ''
			}

		}
	},
    methods: {
        salvarNovoCliente() {
            const metodo = this.id ? 'patch' : 'post'
            const finalUrl = this.id ? `/${this.id}.json` : '.json'
            this.$http[metodo](`/clientes${finalUrl}`, this.cliente).then(() => {
                this.limpar()
                this.obterListaClientes()
                this.mensagens.push({
						texto: 'Novo clinete adicionado com sucesso!',
						tipo: 'success'
                })
            })
        },
        obterListaClientes() {
            this.$http.get('clientes.json').then(res => {
				this.clientes = res.data // A resposta de insira no array clientes
			})
        },
        editarCliente(id) {
            this.id = id
			this.cliente = { ...this.clientes[id]}
        },
        limpar() {
			this.cliente.codObra = ''
            this.cliente.nome = ''
            this.cliente.endereco = ''
            this.cliente.telefone = ''
            this.cliente.email = ''
            this.cliente.data = ''
			this.id = null
			this.mensagens = []
		},
        excluir(id) {
			this.$http.delete(`/clientes/${id}.json`).then(() => {
				this.limpar()
				this.obterListaClientes()
				})
			.catch(err => {
				this.mensagens.push({
					texto: 'Problema para excluir',
					tipo: 'danger'
				})
			})
		},
    }

}
</script>

<style>

</style>