import './Table.css'
import { connect } from 'react-redux'

const Table = props => {

    const { num, forn } = props

    return (
        <div className="Table">
            <h1>Table</h1>
            <table className='TableElements'>
                <thead>
                    <th>Ação</th>
                    <th>NF</th>
                    <th>Fornecedor</th>
                    <th>Item</th>
                    <th>Valor</th>
                </thead>
                <tbody>
                    <div className='GroupBtn'>
                        <button className='Btn'> + </button>
                        <button className='Btn'> - </button>
                        <button className='Btn'> Ed </button>
                    </div>
                    <td>{num}</td>
                    <td>{forn}</td>
                    <td>cimento</td>
                    <td>R$25.50</td>
                </tbody>
                <tbody>
                    <div className='GroupBtn'>
                        <button className='Btn'> + </button>
                        <button className='Btn'> - </button>
                        <button className='Btn'> Ed </button>
                    </div>
                    <td>598765</td>
                    <td>Santa Felicidade</td>
                    <td>Areia</td>
                    <td>R$98.50</td>
                </tbody>
            </table>
        </div>
    )
}

function mapStateToProps(state) {
    return {
        num: state.notas.nfs.num,
        forn: state.notas.nfs.fornecedor
    }
}

export default connect(mapStateToProps)(Table)