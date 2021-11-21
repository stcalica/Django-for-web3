import React from 'react';
import { Routes, Route } from 'react-router-dom';
import LoginContainer from './containers/Login';
import ProtectedRoute from './components/ProtectedRoute';
import Home from './containers/Home';

export default function AppRouter() {
  //TODO: set up protected routes
  return (
    <Routes>
      <Route exact path="/" element={<ProtectedRoute><Home /></ProtectedRoute>} />
      <Route exact path="/login" element={<LoginContainer />} />
    </Routes>
  );
}
