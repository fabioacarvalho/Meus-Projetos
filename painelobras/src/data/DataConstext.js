import React from "react";

export const data = {
    fornecedores: {
        nome: 'Construção',
        tel: '9876543210',
        email: 'fasads@dasdsa.com'
    }
}


const DataContext = React.createContext(data)

export default DataContext