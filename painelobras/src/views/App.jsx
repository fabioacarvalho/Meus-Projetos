import './App.css'

import React, { useState} from "react";

import Body from "../components/Body";
import DataContext, { data } from '../data/DataContext'


const App = props => {

    const [state, setState] = useState(data)

    return (
        <DataContext.Provider value={{state, setState}}>
            <div className="App">
                
                <Body className="Body" />
                
            </div>
        </DataContext.Provider>
    )
}

export default App