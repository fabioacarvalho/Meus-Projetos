import { createStore, combineReducers } from "redux";

const nfs = {
        num: 123456,
        fornecedor: 'Balaroti'
    }

const valores = [
    {
        item: "Areia Média",
        unidade: "m³",
        quantidade: 8,
        valor: 98
    },
    {
        item: "Brita 1",
        unidade: "m³",
        quantidade: 8,
        valor: 75
    },
    {
        item: "Cimento 50kg",
        unidade: "ud",
        quantidade: 8,
        valor: 31.9
    }
]

const reducers = combineReducers({
    notas: function(state, action) {
        return {
            nfs
        }
    },
    itens: function(state, action) {
        return {
            valores
        }
    }
})

function storeConfig() {
    return createStore(reducers)
}

export default storeConfig