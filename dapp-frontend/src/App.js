import Login from './components/login';
import { UserProvider } from './context/UserContext.js';

import './App.css';


function App() {
  return (
    <UserProvider>
      <Login />
      </UserProvider>
  );
}

export default App;
