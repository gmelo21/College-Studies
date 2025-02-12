import { useState, useEffect } from 'react'
import Sensor from '../../components/Sensor/Sensor'

const Home = () => {
    const [temperature, setTemperature] = useState([])

    useEffect(() => {
        fetch("http://localhost:5000/temperature/")
            .then((res) => {
                return res.json();
            })
            .then((res) => {
                setTemperature(res)

            }).catch((error) => {
                console.log(error)
            })
    })


    return (
        <>
            <h1>Sensor values: </h1>
            <Sensor data={temperature} />
        </>
    )
}

export default Home