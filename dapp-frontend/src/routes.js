import React from 'react';
import { Routes ,Route } from 'react-router-dom';
import LoginContainer from './containers/login';
import Home from './containers/Home';

export default function AppRouter() {
  //TODO: set up protected routes 
  return (
    <Routes>
      <Route exact path="/login">
        <LoginContainer />
      </Route>
      <Route exact path="/">
        <Home />
      </Route>
    </Routes>
  );
}
