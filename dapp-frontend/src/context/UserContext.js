import { createContext, useState } from 'react';
import Web3 from 'web3';
import APIClient from '../client/dapp-api';

const defaultValues = {
  user : null,
  login: () => {},
};

export const UserContext = createContext(defaultValues);


export const UserProvider = ({ children }) => {
  const [user, setUser] = useState({});

  const login = async () => {
      if (window.ethereum) {
          window.web3 = new Web3(window.ethereum);
          let address = window.web3.currentProvider.selectedAddress;
          console.log(`address: ${address}`);
          try {
              await window.ethereum.enable();
              let user = await APIClient('user', 'GET', address);
              let nonce = user.nonce;
              const singedNonce = await window.web3.eth.sign(nonce, address)
              let token = await APIClient('token', 'POST', address, {'nonce': singedNonce});
              setUser({...user, ...token});
              return token;
          } catch (error) {
              console.log(error);
          }
      }
    };


  return(
    <UserContext.Provider value={{
      ...defaultValues,
      user,
      login,
    }}>
      { children }
      </UserContext.Provider>
  );
}
