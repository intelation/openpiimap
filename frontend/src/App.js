import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Home from './pages/Home';
import Countries from './pages/Countries';
import Frameworks from './pages/Frameworks';
import Categories from './pages/Categories';

function App() {
  return (
    <Router>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/countries">Countries</Link></li>
          <li><Link to="/frameworks">Frameworks</Link></li>
          <li><Link to="/categories">Categories</Link></li>
        </ul>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/countries" element={<Countries />} />
        <Route path="/frameworks" element={<Frameworks />} />
        <Route path="/categories" element={<Categories />} />
      </Routes>
    </Router>
  );
}

export default App;
