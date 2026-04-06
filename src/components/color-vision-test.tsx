import React, { useState } from 'react';
import axios from 'axios';

const ColorVisionTest: React.FC = () => {
  const [currentPlate, setCurrentPlate] = useState(0);
  const [responses, setResponses] = useState<string[]>([]);
  const [result, setResult] = useState(null);

  const plates = [
    { id: 1, colors: ['#FF0000', '#CC3333'], options: ['12', '8', 'Nothing'] },
    { id: 2, colors: ['#00FF00', '#33CC33'], options: ['5', '2', 'Nothing'] },
  ];

  const handleAnswer = async (answer: string) => {
    const newResponses = [...responses, answer];
    if (newResponses.length < plates.length) {
      setResponses(newResponses);
      setCurrentPlate(currentPlate + 1);
    } else {
      const res = await axios.post('/api/diagnostic/result', { responses: newResponses });
      setResult(res.data);
    }
  };

  if (result) {
    return (
      <div>
        <h2>Your Diagnosis: {result.cvd_type.toUpperCase()}</h2>
        <p>Severity: {Math.round(result.severity * 100)}%</p>
        <button onClick={() => window.location.reload()}>Retake Test</button>
      </div>
    );
  }

  return (
    <div>
      <h3>Plate {currentPlate + 1} of {plates.length}</h3>
      <div style={{ display: 'flex', gap: '20px', margin: '20px' }}>
        {plates[currentPlate].colors.map((color, i) => (
          <div key={i} style={{ width: '100px', height: '100px', backgroundColor: color }} />
        ))}
      </div>
      {plates[currentPlate].options.map(opt => (
        <button key={opt} onClick={() => handleAnswer(opt)} style={{ margin: '5px' }}>
          {opt}
        </button>
      ))}
    </div>
  );
};

export default ColorVisionTest;
