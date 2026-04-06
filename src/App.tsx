import React, { useState } from 'react';
import ColorVisionTest from './components/color-vision-test';
import ThemeExporter from './components/theme-exporter';

function App() {
  const [diagnosis, setDiagnosis] = useState(null);

  // You'll pass the diagnosis from the test to the exporter
  // This is a simplified version - you'll need to manage state between components

  return (
    <div>
      <h1>Color Graft</h1>
      {!diagnosis ? (
        <ColorVisionTest />
      ) : (
        <ThemeExporter cvdType={diagnosis.cvd_type} severity={diagnosis.severity} />
      )}
    </div>
  );
}

export default App;
