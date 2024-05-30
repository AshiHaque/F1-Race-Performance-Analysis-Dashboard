import React from 'react';
import CustomNavbar from '../Components/Navbar';
import Footer from '../Components/Footer';
import './Homepage.css';
import carImage from '../Images/Car.png'; 
import circuit from '../Images/Circuit.jpg'; 

const Homepage = () => {
  return (
    <div className="homepage">
      <CustomNavbar />
      <div className="content">
        <div className="text-box">
          <h1>Explore comprehensive F1 data insights with the dynamic analysis dashboard</h1>
        </div>
        <div className="images">
          <img src={carImage} alt="Car" className="car-image" />
          <img src={circuit} alt="Track" className="circuit-image" />
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default Homepage;
