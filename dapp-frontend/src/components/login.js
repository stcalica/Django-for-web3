import React, { useContext } from 'react';
import { UserContext } from '../context/UserContext.js';

const LoginButton = () => {
  const { user, login } = useContext(UserContext);

  const authenticate = (e) => {
    e.preventDefault();
    let token = login();
    console.log(user);
  };

  return (
    <div className="login-container">
      <button onClick={authenticate}>Login</button>
    </div>
  );
}

export default LoginButton;
