import './Home.css'
import Header from '../components/Header'
import Box from '../components/Box'
import Table from '../components/Table'

const Home = props => {
    return (
        <div className="Home">
            <Header />
            <Box />
            <Table />
        </div>
    )
}

export default Home