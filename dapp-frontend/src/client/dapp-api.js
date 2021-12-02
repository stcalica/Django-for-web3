
const APIClient = async function callAPI(endpoint, method, address, data){
  let URL = `http://localhost:8000/api/${endpoint}/`;
  const context = {
    headers: {
          'Accept': "application/json",
          'Content-Type': "application/json"
          },
      method: method
  };

  let headers = {
    ...context,
  };

  if(data){
    headers = {
      ...headers,
      body: JSON.stringify(data),
    }
  } else {
    headers = {
      ...context,
      };
  }
  if(endpoint === 'user' && method === "GET"){
    URL += address;
  }

  try {
    console.log(`calling ${URL}`);
    return await fetch(URL, headers).then(response => response.json());
  } catch(err) {
    console.error(err);
    throw err;
  }
}

export default APIClient;
