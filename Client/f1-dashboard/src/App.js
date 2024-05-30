import './App.css';
import React from 'react';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import Homepage from './Pages/Homepage';
import CircuitsComponent from './Pages/Circuit';
import CustomNavbar from './Components/Navbar';
import Footer from './Components/Footer';

export default function App() {
  return (
    <BrowserRouter>
      <CustomNavbar />
      <Routes>
        <Route path="/" element={<Homepage />} />
        <Route path="/circuits" element={<CircuitsComponent />} />
        {/* <Route path="/constructors" element={<Constructors />} /> */}
        {/* <Route path="/drivers" element={<Drivers />} /> */}
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}
