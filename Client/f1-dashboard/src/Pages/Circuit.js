import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CircuitsComponent = () => {
    const [circuitNames, setCircuitNames] = useState([]);
    const [selectedCircuit, setSelectedCircuit] = useState('');
    const [circuitInfo, setCircuitInfo] = useState(null);

    useEffect(() => {
        fetchCircuitNames();
    }, []);

    const fetchCircuitNames = () => {
        axios.get('http://localhost:5000/circuits/names')
            .then(response => {
                setCircuitNames(response.data);
            })
            .catch(error => {
                console.error('Error fetching circuit names:', error);
            });
    };

    const handleSelectChange = (event) => {
        setSelectedCircuit(event.target.value);
    };

    const handleGetInfo = () => {
        axios.get(`http://localhost:5000/circuits?circuit_name=${encodeURIComponent(selectedCircuit)}`)
            .then(response => {
                setCircuitInfo(response.data);
            })
            .catch(error => {
                console.error('Error fetching circuit info:', error);
            });
    };

    return (
        <div>
            <h2>Circuits</h2>
            <div>
                <h3>Select Circuit</h3>
                <select value={selectedCircuit} onChange={handleSelectChange}>
                    <option value="">Select a Circuit</option>
                    {circuitNames.map((circuitName, index) => (
                        <option key={index} value={circuitName}>{circuitName}</option>
                    ))}
                </select>
                <button onClick={handleGetInfo}>Get Info</button>
                {circuitInfo && (
                    <div>
                        <h4>{circuitInfo["Circuit Name"]}</h4>
                        <p>Location: {circuitInfo.Location}</p>
                        <p>Country: {circuitInfo.Country}</p>
                        <p>Latitude: {circuitInfo.Latitude}</p>
                        <p>Longitude: {circuitInfo.Longitude}</p>
                        <p>Altitude: {circuitInfo.Altitude} meters</p>
                    </div>
                )}
            </div>
        </div>
    );
}

export default CircuitsComponent;
