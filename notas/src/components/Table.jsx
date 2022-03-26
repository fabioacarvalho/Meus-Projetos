import './Table.css'
import { connect } from 'react-redux'

const Table = props => {

    const { dados } = props
    
    const list = dados.map(dado => {
        return (
            <tbody>
                <td>{dado.item}</td> <td>{dado.unidade}</td> <td>{dado.quantidade}</td> <td>R$ {dado.valor}</td><td>R$ {dado.valor * dado.quantidade}</td>
            </tbody>
        );
    })


    return (
        <div className="Table">
            <h1>Table</h1>
            <table>
                <thead>
                    <th>Item</th>
                    <th>Unidade</th>
                    <th>Quantidade</th>
                    <th>Valor</th>
                    <th>Total</th>
                </thead>
                {list}
            </table>
]        </div>
    )
}

function mapStateToProps(state) {
    return {
        dados: state.itens.valores
    }
}

export default connect(mapStateToProps)(Table)