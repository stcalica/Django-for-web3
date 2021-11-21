import React, { useContext } from 'react';
import { UserContext } from '../context/UserContext.js';
import { useLocation, useNavigate } from 'react-router-dom';

const LoginButton = () => {
  const { user, login } = useContext(UserContext);
  const navigate = useNavigate();
  const { state } = useLocation();

  const authenticate = (e) => {
    e.preventDefault();
    let token = login();
    console.log('token called for');
    console.dir(user);
    if(token){
      navigate(state.path || "/");
    }
  };

  return (
    <div className="login-container">
      <button onClick={authenticate}>Login</button>
    </div>
  );
}

export default LoginButton;
