import React from 'react';
import { Navbar, Nav } from 'react-bootstrap';
import './Navbar.css';
import logo from '../Images/Logo.png';

const CustomNavbar = () => {
  return (
    <Navbar expand="lg" className="navbar-custom">
      <Navbar.Brand href="#home" className="navbar-brand-custom">
        <img
          src={logo}
          width="60"
          height="60" 
          className="d-inline-block align-top"
          alt="F1 Dashboard Logo"
        />
      </Navbar.Brand>
      <div className="navbar-title"><Nav.Link href="#home">F1 Dashboard</Nav.Link></div>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="ml-auto navbar-links">
          <Nav.Link href="#circuits">Circuits</Nav.Link>
          <Nav.Link href="#constructors">Constructors</Nav.Link>
          <Nav.Link href="#drivers">Drivers</Nav.Link>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
};

export default CustomNavbar;
