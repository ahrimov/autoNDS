import logo from './logo.svg';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import { UploadPDF } from './UploadPDF';

function App() {
  return (
    <div className="App">
          <Router>
            <Routes>
                <Route path="/" element={<UploadPDF />} />
            </Routes>
        </Router>
      <UploadPDF />
    </div>
  );
}

export default App;
