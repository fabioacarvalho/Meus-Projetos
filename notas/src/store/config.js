import { createStore, combineReducers } from "redux";

const nfs = {
        num: 123456,
        fornecedor: 'Balaroti'
    }

const reducers = combineReducers({
    notas: function(state, action) {
        return {
            nfs
        }
    }
})

function storeConfig() {
    return createStore(reducers)
}

export default storeConfig