
import React, { useState, useEffect } from 'react';

function BagsComponent() {
  const [bags, setBags] = useState([]);

  useEffect(() => {
    fetch('/bags')  
      .then(response => response.json())
      .then(data => {
             console.log('Bags data:', data)
             setBags(data)})
      .catch(error => console.error('Error fetching bags:', error));
  }, []);

  return (
    <div>
      <h1>Bags</h1>
      <ul>
        {bags.map(bag => (
          <li key={bag.id}> {/* Assign a unique key prop */}
            <img src={bag.image_filename} alt={bag.name} width="500px" height="200px" />
            <h3>Name: {bag.name}</h3>
            <div>Color: {bag.color}</div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default BagsComponent;
