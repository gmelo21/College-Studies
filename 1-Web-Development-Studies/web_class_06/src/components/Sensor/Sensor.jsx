import React, { useEffect, useState } from 'react';
import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
} from 'recharts';

export default function SensorChart() {
    const [chartData, setChartData] = useState([]);

    const myHeaders = new Headers();
    myHeaders.append("fiware-service", "smart");
    myHeaders.append("fiware-servicepath", "/");

    const fetchChartData = async () => {
        const requestOptions = {
            method: "GET",
            headers: myHeaders,
            redirect: "follow",
        };

        try {
            const [luminosityResponse, humidityResponse, temperatureResponse] = await Promise.all([
                fetch('/STH/v1/contextEntities/type/Lamp/id/urn:ngsi-ld:Lamp:EDGE4/attributes/luminosity?lastN=50', requestOptions),
                fetch('/STH/v1/contextEntities/type/Lamp/id/urn:ngsi-ld:Lamp:EDGE4/attributes/humidity?lastN=50', requestOptions),
                fetch('/STH/v1/contextEntities/type/Lamp/id/urn:ngsi-ld:Lamp:EDGE4/attributes/temperature?lastN=50', requestOptions),
            ]);

            if (!luminosityResponse.ok || !humidityResponse.ok || !temperatureResponse.ok) {
                throw new Error("Network response was not ok");
            }

            const luminosityData = await luminosityResponse.json();
            const humidityData = await humidityResponse.json();
            const temperatureData = await temperatureResponse.json();

            const combinedData = luminosityData.contextResponses[0].contextElement.attributes[0].values.map((item, index) => {
                const date = new Date(item.recvTime);
                const formattedTime = date.toLocaleTimeString('pt-PT', { timeZone: 'UTC' });

                return {
                    time: formattedTime,
                    luminosity: parseFloat(item.attrValue),
                    humidity: humidityData.contextResponses[0].contextElement.attributes[0].values[index]
                        ? parseFloat(humidityData.contextResponses[0].contextElement.attributes[0].values[index].attrValue)
                        : null,
                    temperature: temperatureData.contextResponses[0].contextElement.attributes[0].values[index]
                        ? parseFloat(temperatureData.contextResponses[0].contextElement.attributes[0].values[index].attrValue)
                        : null,
                };
            });

            setChartData(combinedData);

        } catch (error) {
            console.error(error);
        }
    };

    useEffect(() => {
        fetchChartData();
        const interval = setInterval(fetchChartData, 5000);

        return () => clearInterval(interval);
    }, []);

    return (
        <LineChart
            width={500}
            height={300}
            data={chartData}
            margin={{
                top: 5,
                right: 30,
                left: 20,
                bottom: 5
            }}
        >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="time" />
            <YAxis />
            <Tooltip />
            <Line
                type="monotone"
                dataKey="luminosity"
                stroke="#8884d8"
                activeDot={{ r: 8 }}
                animationDuration={0} // Disable animation
                isAnimationActive={false} // Ensure no animation occurs
            />
            <Line
                type="monotone"
                dataKey="humidity"
                stroke="#82ca9d"
                animationDuration={0} // Disable animation
                isAnimationActive={false} // Ensure no animation occurs
            />
            <Line
                type="monotone"
                dataKey="temperature"
                stroke="#ffc658"
                animationDuration={0} // Disable animation
                isAnimationActive={false} // Ensure no animation occurs
            />
        </LineChart>
    );
}
