import React, { useContext } from 'react';
import { UserContext } from '../context/UserContext.js';
import LoginContainer from './Login';

const Home = () => {
  const { user, login } = useContext(UserContext);


  const HomeContainer = () => (
    <h2> Welcome, Moneyshot </h2>
  );

  return (
    {
      user ? <HomeContainer /> : <LoginContainer />
    }
  );
}

export default Home;
