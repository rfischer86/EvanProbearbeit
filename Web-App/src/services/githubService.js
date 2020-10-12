


import axios from 'axios'

export default class GithubService {

  serverURL = 'http://127.0.0.1:5000';
  response = 0;
  
  constructor() {} 
  
  getGroupRepos(repoName) {
    const headers = {
      'Content-Type': 'application/json'
    };
    return axios.get(this.serverURL + '/repo/'+ repoName, {headers})
  }
}
