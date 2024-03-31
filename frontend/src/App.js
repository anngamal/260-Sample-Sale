// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         {/* <img src={logo} className="App-logo" alt="logo" /> */}
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;

// import React, { useState, useEffect } from 'react';
// function App(){

//   const [data,setData] = useState([])

//   useEffect(() =>{
//     fetch('/members')
//     .then(res=>res.json())
//     .then(
//       data =>{
//         setData(data)
//         console.log(data)
//       }
//     )
//   },[])
//   return (
//     <div>
//       {(typeof data.members === 'undefined') ? (
//         <p>Loading...</p>
//       ) : (
//         data.members.map((member, i) => (
//           <p key={i}>{member}</p>
//         ))
//       )}
//     </div>
//   );
  
// }

// export default App;


// import React, { useState, useEffect } from 'react';

// function BagsComponent() {
//   const [bags, setBags] = useState([]);

//   useEffect(() => {
//     fetch('/bags')  
//       .then(response => response.json())
//       .then(data => {
//         console.log('Bags data:', data)
//         setBags(data)})
//       .catch(error => console.error('Error fetching bags:', error));
//   }, []);

//   return (
//     <div>
//       <h1>Bags</h1>
//       <ul>
//         {bags.map(bag => (
//           <li key={bag.id}>
//             <img src={bag.image_filename} alt={bag.name} />
//             <div>Name: {bag.name}</div>
//             <div>Color: {bag.color}</div>
            
//           </li>
//         ))}
//       </ul>
//     </div>
//   );
// }

// export default BagsComponent;


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
