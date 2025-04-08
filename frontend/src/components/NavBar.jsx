import React, { useState } from "react";
import "../css/NavBar.css";

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => setIsOpen(!isOpen);

  return (
    <nav className="navbar">
      <div className="navbar-container">
        <div className="logo">PDF Summariser</div>
      </div>
    </nav>
  );
};

export default Navbar;