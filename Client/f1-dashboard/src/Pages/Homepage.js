import React from 'react';
import { Outlet} from "react-router-dom";
import './Homepage.css';
import carImage from '../Images/Homepage/Car.png'; 
import track from '../Images/Homepage/Track.jpg'; 

const Homepage = () => {
  return (
    <>
      <div className="homepage">
        <div className="content">
          <div className="text-box">
            <h1>Explore comprehensive F1 data insights with the dynamic analysis dashboard</h1>
          </div>
          <div className="images">
            <img src={carImage} alt="Car" className="car-image" />
            <img src={track} alt="Track" className="circuit-image" />
          </div>
        </div>
      </div>
    <Outlet />
    </>
  );
};

export default Homepage;
