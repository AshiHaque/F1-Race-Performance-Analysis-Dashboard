import React from 'react';
import { Navbar, Nav } from 'react-bootstrap';
import './Navbar.css';
import logo from '../Images/Logos/Logo.png';
import { Outlet, NavLink } from "react-router-dom";

const CustomNavbar = () => {
  return (
    <>
      <Navbar expand="lg" className="navbar-custom">
        <NavLink to="/" className="navbar-brand-custom">
          <img
            src={logo}
            width="60"
            height="60" 
            className="d-inline-block align-top"
            alt="F1 Dashboard Logo"
          />
        </NavLink>
        <div className="navbar-title"> <NavLink to="/" className="nav-title-link">F1 Dashboard</NavLink></div>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="ml-auto navbar-links">
            <NavLink to="/circuits" className="nav-link-custom" activeClassName="active">Circuits</NavLink>
            <NavLink to="/constructors" className="nav-link-custom" activeClassName="active">Constructors</NavLink>
            <NavLink to="/drivers" className="nav-link-custom" activeClassName="active">Drivers</NavLink>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
      <Outlet />
    </>
  );
};

export default CustomNavbar;
