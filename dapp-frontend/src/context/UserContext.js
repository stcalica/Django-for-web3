import { createContext, useState } from 'react';
import Web3 from 'web3';
import APIClient from '../client/dapp-api';

const defaultValues = {
  user : null,
  authenticated: false,
  login: () => {},
};

export const UserContext = createContext(defaultValues);

export const UserProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [authenticated, isAuthenticated] = useState(false);

  const login = async () => {
      if (window.ethereum) {
          window.web3 = new Web3(window.ethereum);
          let address = window.web3.currentProvider.selectedAddress;
          console.log(`address: ${address}`);
          try {
              await window.ethereum.enable();
              let user = await APIClient('user', 'GET',  address);
              let nonce = user.nonce;
              const nonceHash = window.web3.eth.accounts.hashMessage(nonce)
              const singedNonce = await window.web3.eth.sign(nonceHash, address)
              console.log(singedNonce);
              let token = await APIClient('token', 'POST', address, {'nonce': singedNonce, 'public_address': address });
              console.log(token);
              setUser({...user, ...token});
              isAuthenticated(true);
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
      authenticated,
      user,
      login,
    }}>
      { children }
      </UserContext.Provider>
  );
}
