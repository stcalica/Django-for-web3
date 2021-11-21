import { createContext, useState } from 'react';
import Web3 from 'web3';
import APIClient from '../client/dapp-api';

const defaultValues = {
  user : null,
  login: () => {},
};

export const UserContext = createContext(defaultValues);


export const UserProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  const login = async () => {
    console.log('login called');
      if (window.ethereum) {
          window.web3 = new Web3(window.ethereum);
          let address = window.web3.currentProvider.selectedAddress;
          console.log(`address: ${address}`);
          try {
              await window.ethereum.enable();
              let user = await APIClient('user', 'GET', address);
              let nonce = user.nonce;
              const singedNonce = await window.web3.eth.sign(nonce, address)
              console.log(singedNonce);
              let token = await APIClient('token', 'POST', address, {'nonce': singedNonce});
              console.log(token);
              setUser({...user, ...token});
              return token;
          } catch (error) {
              console.log(error);
          }
      } else {
        console.log('please install a crypto wallet');
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
