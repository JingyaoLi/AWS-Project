import axios from 'axios';

export function testApi(){
    let param = {
        "guestEmail": "jl9075@nyu.edu"
      }
    return axios.get('https://72xl3f831d.execute-api.us-east-1.amazonaws.com/prod1/getattendedparties', {
        params: param
    });
}