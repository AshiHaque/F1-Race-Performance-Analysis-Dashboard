import React, { useState, useEffect } from 'react';
import { Row, Col, Card, Form } from 'react-bootstrap';
import { Outlet} from "react-router-dom";
import axios from 'axios';

const CircuitsComponent = () => {
  const [circuitNames, setCircuitNames] = useState([]);
  const [selectedCircuit, setSelectedCircuit] = useState('');
  const [circuitInfo, setCircuitInfo] = useState(null);

  useEffect(() => {
    fetchCircuitNames();
  }, []);

  const fetchCircuitNames = async () => {
    try {
      const response = await axios.get('http://localhost:5000/circuits/names');
      setCircuitNames(response.data);
    } catch (error) {
      console.error('Error fetching circuit names:', error);
    }
  };

  const handleSelectChange = (event) => {
    setSelectedCircuit(event.target.value);
  };

  const handleGetInfo = async () => {
    try {
      const response = await axios.get(`http://localhost:5000/circuits?circuit_name=${encodeURIComponent(selectedCircuit)}`);
      setCircuitInfo(response.data);
    } catch (error) {
      console.error('Error fetching circuit info:', error);
    }
  };

  return (
    <>
      <div className="circuits-container">
        <h2>Circuits</h2>
        <Row>
        <Col xs={12} md={6}>
            <Card className="circuit-selection">
                <Card.Body>
                    <h3>Select Circuit</h3>
                    <Form.Select className="circuit-selection-form" size="lg" value={selectedCircuit} onChange={handleSelectChange}>
                        <option value="">Select a Circuit</option>
                        {circuitNames.map((circuitName, index) => (
                            <option key={index} value={circuitName}>{circuitName}</option>
                        ))}
                    </Form.Select>
                    <button onClick={handleGetInfo}>Get Info</button>
                </Card.Body>
            </Card>
        </Col>
          {circuitInfo && (
            <Col xs={12} md={6}>
              <Card className="circuit-info">
                <Card.Img variant="top" src="https://your-image-placeholder.jpg" alt="Circuit Image" />
                <Card.Body>
                  <Card.Title>{circuitInfo["Circuit Name"]}</Card.Title>
                  <Card.Text>
                    <p>Location: {circuitInfo.Location}</p>
                    <p>Country: {circuitInfo.Country}</p>
                    <p>Latitude: {circuitInfo.Latitude}</p>
                    <p>Longitude: {circuitInfo.Longitude}</p>
                    <p>Altitude: {circuitInfo.Altitude} meters</p>
                  </Card.Text>
                </Card.Body>
              </Card>
            </Col>
          )}
        </Row>
      </div>
      <Outlet />
    </>
  );
};

export default CircuitsComponent;
