import React, { useContext } from 'react';
import { UserContext } from '../context/UserContext.js';
import LoginContainer from './Login';

const Purchase = ({nft, ...props}) => {
  const { user, login } = useContext(UserContext);
  //TODO: get specific NFT from listing page or from URL
  
  return (
    <div></div>
  );
}

export default Purchase;
