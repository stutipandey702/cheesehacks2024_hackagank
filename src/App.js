import React, { useState } from 'react';
import './App.css';

function App() {
  const [skinType, setSkinType] = useState('');
  const [concern, setConcern] = useState('');
  const [budget, setBudget] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    alert(`Skin Type: ${skinType}\nConcern: ${concern}\nBudget: ${budget}`);
  };

  return (
    <div className = "app-container">
      <h1 className="heading"> Hello! I'm your Skincare Helper!</h1>
      <p className="intro-text">Let's find the perfect product for you</p>

      <form className="chat-form" onSubmit={handleSubmit}>
        <div className="chat-question">
          <label htmlFor="skin-type">What is your skin type?</label>
          <select 
            id="skin-type" 
            value={skinType} 
            onChange={(e) => setSkinType(e.target.value)} 
            required
          >
            <option value="">Select your skin type</option>
            <option value="Oily">Oily</option>
            <option value="Dry">Dry</option>
            <option value="Combination">Combination</option>
            <option value="Sensitive">Sensitive</option>
          </select>
        </div>

        <div className="chat-question">
          <label htmlFor="concern">What is your main skincare concern?</label>
          <select 
            id="concern" 
            value={concern} 
            onChange={(e) => setConcern(e.target.value)} 
            required
          >
            <option value="">Select your concern</option>
            <option value="Acne">Acne</option>
            <option value="Wrinkles">Wrinkles</option>
            <option value="Hyperpigmentation">Hyperpigmentation</option>
            <option value="Dryness">Dryness</option>
          </select>
        </div>

        <div className="chat-question">
          <label htmlFor="budget">What's your budget?</label>
          <select 
            id="budget" 
            value={budget} 
            onChange={(e) => setBudget(e.target.value)} 
            required
          >
            <option value="">Select your budget</option>
            <option value="Under $20">Under $20</option>
            <option value="$20 - $50">$20 - $50</option>
            <option value="$50 - $100">$50 - $100</option>
            <option value="Above $100">Above $100</option>
          </select>
        </div>

        <button type="submit" className="submit-btn">Get Recommendations</button>
      </form>
    </div>
  );
}

export default App;

