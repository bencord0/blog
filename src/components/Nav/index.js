import React from 'react';
import { Link } from 'react-router-dom';

import './index.css';

function Nav() {
  return (
    <div className="Nav">
      <div className="Nav-brand">
        <Link to="/">Fragments</Link>
      </div>
      <div className="Nav-collapse">
        <Link to="/">Home</Link>
      </div>
      <div className="Nav-collapse">
        <Link to="/about/">About</Link>
      </div>
      <div className="Nav-collapse">
        <Link to="/archive/">Archive</Link>
      </div>
      <div className="Nav-collapse tagline">
        <p>small, unrelated items: sometimes broken</p>
      </div>
    </div>
  );
}

export default Nav;
