import axios from 'axios';

export function testApi(){
    let param = {
        "guestEmail": "jl9075@nyu.edu"
      }
    return axios.get('https://72xl3f831d.execute-api.us-east-1.amazonaws.com/prod1/getattendedparties', {
        params: param
    });
}

export function SignUpDb(param){
    return axios.post('https://72xl3f831d.execute-api.us-east-1.amazonaws.com/prod1/createuser', param);
}

export function DisplayHome(param){
    return axios.get('https://72xl3f831d.execute-api.us-east-1.amazonaws.com/prod1/search', {
        params: param
    });
}

export function getUserInfo(param){
    return axios.get('https://72xl3f831d.execute-api.us-east-1.amazonaws.com/prod1/getuser', {
        params: param
    });
}

export function updataUserInfo(param){
    return axios.post('https://72xl3f831d.execute-api.us-east-1.amazonaws.com/prod1/updateuser', param);
}

export function createPartyDb(param){
    return axios.post('https://72xl3f831d.execute-api.us-east-1.amazonaws.com/prod1/createparty', param);
}

export function getParty(param){
    return axios.get('https://72xl3f831d.execute-api.us-east-1.amazonaws.com/prod1/getpartybyidanduser', {
        params: param
    });
}