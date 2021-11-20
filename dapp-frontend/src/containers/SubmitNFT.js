import React, { useContext } from 'react';
import { UserContext } from '../context/UserContext.js';
import LoginContainer from './Login';

const Submit = () => {
  const { user, login } = useContext(UserContext);
  //TODO: create form to upload NFT 

  return (
    <div></div>
  );
}

export default Submit;
