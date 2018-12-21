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

export function getHostParty(param){
    return axios.get('https://72xl3f831d.execute-api.us-east-1.amazonaws.com/prod1/gethostedparties', {
        params: param
    });
}

export function getGuestParty(param){
    return axios.get('https://72xl3f831d.execute-api.us-east-1.amazonaws.com/prod1/getattendedparties', {
        params: param
    });
}

export function updatePartyDb(param){
    return axios.post('https://72xl3f831d.execute-api.us-east-1.amazonaws.com/prod1/updateparty', param);
}

export function attendParty(param){
    return axios.post('https://72xl3f831d.execute-api.us-east-1.amazonaws.com/prod1/attendparty', param);
}

export function cancelParty(param){
    return axios.post('https://72xl3f831d.execute-api.us-east-1.amazonaws.com/prod1/cancelparty', param);
}

export function rateParty(param){
    return axios.post('https://72xl3f831d.execute-api.us-east-1.amazonaws.com/prod1/ratingparty', param);
}

export function followUser(param){
    return axios.post('https://72xl3f831d.execute-api.us-east-1.amazonaws.com/prod1/followuser', param);
}

export function unfollowUser(param){
    return axios.post('https://72xl3f831d.execute-api.us-east-1.amazonaws.com/prod1/unfollow', param);
}

export function getDiscover(param){
    return axios.get('https://72xl3f831d.execute-api.us-east-1.amazonaws.com/prod1/friendcircle',{
        params: param
    });
}

export function searchPartyDb(param){
    return axios.get('https://72xl3f831d.execute-api.us-east-1.amazonaws.com/prod1/search', {
        params: param
    })
}

export function deleteParty(param){
    return axios.post('https://72xl3f831d.execute-api.us-east-1.amazonaws.com/prod1/deleteparty', param);
}