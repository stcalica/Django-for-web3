import React, { useContext } from 'react';
import LoginButton from '../components/login';
import { useNavigate } from 'react-router-dom';

const LoginContainer = () => {

  return (
    <div className="login-container">
      <LoginButton />
    </div>
  );
}

export default LoginContainer;
