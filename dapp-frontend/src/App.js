import { BrowserRouter as Router } from 'react-router-dom';
import { UserProvider } from './context/UserContext.js';
import Login from './components/login';
import AppRouter from "./routes";

import './App.css';

function App() {
  return (
    <UserProvider>
      <Router />
      </UserProvider>
  );
}

export default App;
