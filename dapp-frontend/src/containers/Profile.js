import React, { useContext } from 'react';
import { UserContext } from '../context/UserContext.js';
import LoginContainer from './Login';

const Profile = () => {
  const { user, login } = useContext(UserContext);
  //TODO: pull out user and list all owned NFTs
  //TODO: send request to become creator

  return (
    <div></div>
  );
}

export default Profile;
