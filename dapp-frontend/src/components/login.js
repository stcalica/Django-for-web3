import React, { useContext } from 'react';
import { UserContext } from '../context/UserContext.js';
import { useLocation, useNavigate } from 'react-router-dom';

const LoginButton = () => {
  const { user, login, authenticated } = useContext(UserContext);
  const navigate = useNavigate();
  const { state } = useLocation();

  const authenticate = (e) => {
    e.preventDefault();
    console.log(user);
    if(authenticated){
      navigate(state.path || "/");
    }
    else{
      let token = login();
      console.dir(user);
      if(token){
        console.log(user);
        navigate(state.path || "/");
      }
    }
  };

  return (
    <div className="login-container">

    {
      authenticated ? (
      ( <h1> Already Logged In </h1> )
      ) : (
        ( <button onClick={authenticate}>Login</button> )
      )
    }
    </div>
  );
}

export default LoginButton;
