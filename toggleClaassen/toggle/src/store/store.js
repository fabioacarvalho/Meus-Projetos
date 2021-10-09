import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        acesso: true,
        items: [
            'Cristina',
            'Carol',
            'Isabely',
            'Guilherme',
            'Karen'
        ],
        valoresEtapa: [
            'Levantamento/Briefing/Digitalização',
            'PM - Processo Criativo',
            'PM - Renderização + Apresentação',
            'Adequações',
            'Projeto Legal',
            'Projeto Executivo',
            'Projeto Executivo Mobiliário',
            'Assessoria para compras',
        ],
        valoresCliente: [
            'Rafael Melcher',
            'Altemisa Carneiro',
            'Luis Gabriel ',
            'Andrea e Paulo',
            'Anderson Primo',
            'Rafael Gamballi',
            'Lincoln Taylor',
            'Letícia Locatelli',
            'Nelson Carvalho',
            'Caio Luiz Vital',
            'Carlos Zimmer',
            'Dulce Osinski',
            'Paulo Vizzotto',
            'Eunice Chavinski',
            'Ana Maria Schwarz',
            'Bruno Carvalho',
            'Renata de Paula',
            'runo Peruzzo de Pádua',
            'aniel Bucheb',
            'oris Karam',
            'aroline Borba',
            'ábio Cunha',
            'eivid Dias',
            'Vânia Muniz Nequer',
            'Jair de Azevedo',
            'ristiane Magliari',
            'Bruno Prazeres',
        ],
    }
})