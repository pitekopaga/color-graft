import React, { useState } from 'react';
import axios from 'axios';

const ThemeExporter: React.FC<{ cvdType: string; severity: number }> = ({ cvdType, severity }) => {
  const [format, setFormat] = useState('css');

  const exportTheme = async () => {
    const basePalette = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00'];
    const res = await axios.post('/api/transform/palette', {
      palette: basePalette,
      cvd_type: cvdType,
      severity: severity
    });
    
    const transformed = res.data.transformed_palette;
    
    if (format === 'css') {
      const css = `:root {\n  --primary: rgb(${transformed[0].join(',')});\n  --secondary: rgb(${transformed[1].join(',')});\n}`;
      downloadFile(css, 'theme.css', 'text/css');
    } else if (format === 'vscode') {
      const vscodeTheme = {
        name: `cvd-${cvdType}-theme`,
        colors: { "editor.foreground": `#${rgbToHex(transformed[0])}` }
      };
      downloadFile(JSON.stringify(vscodeTheme, null, 2), 'theme.json', 'application/json');
    }
  };

  const downloadFile = (content: string, filename: string, mimeType: string) => {
    const blob = new Blob([content], { type: mimeType });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = filename;
    link.click();
  };

  const rgbToHex = (rgb: number[]) => 
    rgb.map(c => c.toString(16).padStart(2, '0')).join('');

  return (
    <div>
      <select value={format} onChange={(e) => setFormat(e.target.value)}>
        <option value="css">CSS Variables</option>
        <option value="vscode">VS Code Theme</option>
      </select>
      <button onClick={exportTheme}>Export Theme</button>
    </div>
  );
};

export default ThemeExporter;
