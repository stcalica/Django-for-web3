const APIClient = async function callAPI(endpoint, method, address, data){
  let url = '';
  if (endpoint == 'user') {
    url = (method === 'GET') ? `http://127.0.0.1:8000/api/user/${address}` : `http://127.0.0.1:8000/api/user/`;
  }

  if (endpoint == 'token') {
    url = `http://127.0.0.1:8000/api/token/`;
  }
  let headers = {};
  if (method === 'GET'){
    headers = {
        headers: {
            'Accept': "application/json",
            'Content-Type': "application/json"
            },
        method: 'GET',
    };
    } else {
    headers =  {
          headers: {
              'Accept': "application/json",
              'Content-Type': "application/json"
              },
          method: 'POST',
          body: JSON.stringify({
            'public_address': address
          }),
      };
  }
  try {
    return await fetch(url, headers).then(response => response.json());
  } catch(err) {
    console.error(err);
    throw err;
  }

};

window.addEventListener('load', async () => {
    // Modern dapp browsers...
    if (window.ethereum) {
        window.web3 = new Web3(ethereum);
        let address = web3.currentProvider.selectedAddress
        try {
            // Request account access if needed
            await ethereum.enable();
            //add code for login here -- ask for nonce and sign and return
            let user = await APIClient('user', 'GET', address);
            //TODO: if not DoesNotExist  then create user
            let nonce = user.nonce;
            const singedNonce = await web3.eth.sign(nonce, address)
            //then ask for token
            let token = await APIClient('token', 'POST', address, {'nonce': singedNonce});

        } catch (error) {
            // User denied account access...
            console.log(error);
        }
    }
    // Non-dapp browsers...
    else {
        console.log('Non-Ethereum browser detected. You should consider trying MetaMask!');
    }
});
