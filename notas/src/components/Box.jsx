import './Box.css'

const Box = props => {
    return (
        <div className="Box">
            <div className="Insert">
                <div className="HeaderNf">
                    <p>Dados Fornecedor</p>
                    <input className="Input" type="text" placeholder="Fornecedor" />
                    <input className="Input" type="date" name="date" id="date" />
                    <input className="Input" type="number" placeholder='Numero Nota' />
                </div>
                <div className="BodyNf">
                    <p>Dados da Nota</p>
                    <input className="Input" type="text" placeholder="Insira o item da nota"/>
                    <input type="number" className="Input" placeholder="Quantidade" />
                    <input type="number" className="Input" placeholder="Valor Unitário" />
                    <button className="Btn"> + </button>
                </div>

            </div>
        </div>
    )
}

export default Box