import React from 'react';
import './Footer.css';
import repo from '../Images/Repo.png';
import linkedin from '../Images/In.png';
import email from '../Images/Mail.png';
import git from '../Images/Git.png';
import { Navbar, Nav } from 'react-bootstrap';

const Footer = () => {
  return (
    <footer className="footer-custom">
      <div className="footer-content">
        <div className="footer-section">
          <div className="footer-title">About the project</div>
          <Navbar.Brand href="https://github.com/AshiHaque/F1-Race-Performance-Analysis-Dashboard" className="footer-image">
            <img
              src={repo}
              width="30"
              height="30" 
              alt="Repository link Logo"
            />
          </Navbar.Brand>
        </div>
      
        <div className="footer-section footer-middle">
          F1 Data Analysis Dashboard
        </div>
        
        <div className="footer-section">
          <div className="footer-title">Contact Me</div>
          <div className="footer-icons">
            <Navbar.Brand href="https://www.linkedin.com/in/mirashifulhaque/" className="footer-image">
              <img
                src={linkedin}
                width="30"
                height="30" 
                alt="Linkedin Profile Logo"
              />
            </Navbar.Brand>

            <Navbar.Brand href="mailto:mirashifulhaque@gmail.com" className="footer-image">
              <img
                src={email}
                width="30"
                height="30" 
                alt="Email Logo"
              />
            </Navbar.Brand>

            <Navbar.Brand href="https://github.com/AshiHaque" className="footer-image">
              <img
                src={git}
                width="30"
                height="30" 
                alt="Github Portfolio Logo"
              />
            </Navbar.Brand>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
