import React, { useContext } from 'react';
import { useLocation, Navigate } from 'react-router-dom'
import { UserContext } from '../context/UserContext.js';
import Login from '../containers/Login';

const ProtectedRoute = ({ children, ...props}) => {
  const { user } = useContext(UserContext);
  const location = useLocation();
  console.log("Protected Route");
  console.dir(location);
  console.log(user);
  return user ? children : <Navigate to="/login" replace state={{ path: location.pathname }} />;
}

export default ProtectedRoute;
