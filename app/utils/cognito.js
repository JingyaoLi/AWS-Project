var AmazonCognitoIdentity = require('amazon-cognito-identity-js');
import AWS from 'aws-sdk';

const poolData = {
    UserPoolId: 'us-east-1_801FITzLQ', // Your user pool id here
    ClientId: '6g9iti8crqsf46hv9pv20p657m' // Your client id here
}

export function Register(param) {
    const userPool = new AmazonCognitoIdentity.CognitoUserPool(poolData);
    const dataEmail = {
        Name: 'email',
        Value: param.email
    }
    let attributeList = [];
    const attributeEmail = new AmazonCognitoIdentity.CognitoUserAttribute(dataEmail);
    attributeList.push(attributeEmail);

    return new Promise((r, j) => {
        userPool.signUp(param.email, param.password, attributeList, null, function (err, result) {
            if (err) {
                j(err.message || JSON.stringify(err));
            } else {
                r('Please use the code send to you email '+ param.email +' to verify');
            }
        });
    });
}

export function Confrim(username, code) {
    var userPool = new AmazonCognitoIdentity.CognitoUserPool(poolData);

    var userData = {
        Username: username,
        Pool: userPool
    };

    var cognitoUser = new AmazonCognitoIdentity.CognitoUser(userData);

    return new Promise((r, j) => {
        cognitoUser.confirmRegistration(code, true, function (err, result) {
            if (err) {
                console.log(err);
                j(err.message || JSON.stringify(err));
            } else {
                r("Sign up Successfully!");
            }
        });
    });
}

