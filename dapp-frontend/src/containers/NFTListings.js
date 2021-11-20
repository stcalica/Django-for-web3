import React, { useContext } from 'react';
import { UserContext } from '../context/UserContext.js';
import LoginContainer from './Login';

const Listings = () => {
  const { user, login } = useContext(UserContext);
  //TODO: list all NFTs relevant to our smart contract

  return (
    <div></div>
  );
}

export default Listings;
