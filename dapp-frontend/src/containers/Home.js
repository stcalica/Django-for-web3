import React, { useContext } from 'react';
import { UserContext } from '../context/UserContext.js';

const Home = () => {
  const { user } = useContext(UserContext);
  return (
    <h2> Welcome to Moneyshot </h2>
  );
}

export default Home;
