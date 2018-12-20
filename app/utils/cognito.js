const AmazonCognitoIdentity = require('amazon-cognito-identity-js');
import AWS from 'aws-sdk';

let useremail = null;

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
                r('Please use the code send to you email ' + param.email + ' to verify');
            }
        });
    });
}

export function Confrim(username, code) {
    const userPool = new AmazonCognitoIdentity.CognitoUserPool(poolData);
    const userData = {
        Username: username,
        Pool: userPool
    };
    const cognitoUser = new AmazonCognitoIdentity.CognitoUser(userData);
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

export function Signin(param) {
    const authenticationData = {
        Username: param.email,
        Password: param.password,
    };
    const authenticationDetails = new AmazonCognitoIdentity.AuthenticationDetails(authenticationData);

    const poolData = {
        UserPoolId: 'us-east-1_801FlTzLQ', // Your user pool id here
        ClientId: '6g9iti8crqsf46hv9pv20p657m' // Your client id here
    };

    const userPool = new AmazonCognitoIdentity.CognitoUserPool(poolData);
    const userData = {
        Username: param.email,
        Pool: userPool
    };
    const cognitoUser = new AmazonCognitoIdentity.CognitoUser(userData);

    return new Promise((r, j) => {
        cognitoUser.authenticateUser(authenticationDetails, {
            onSuccess: function (result) {
                var accessToken = result.getAccessToken().getJwtToken();
                Session();
                r('Log in Successfully!');
            },
            onFailure: function (err) {
                j(err.message || JSON.stringify(err));
            },
        });
    });
}

export function Session() {
    const userPool = new AmazonCognitoIdentity.CognitoUserPool(poolData);
    const cognitoUser = userPool.getCurrentUser();
    if (cognitoUser != null) {
        cognitoUser.getSession(function (err, session) {
            if (err) {
                console.log(err.message || JSON.stringify(err));
                return;
            }
            AWS.config.credentials = new AWS.CognitoIdentityCredentials({
                IdentityPoolId:'us-east-1:e539a235-137f-408a-943b-872de5ef5be9',
                Logins: {
                    'cognito-idp.us-east-1.amazonaws.com/us-east-1_801FlTzLQ': session.getIdToken().getJwtToken()
                }
            }, { region: 'us-east-1' });
            let cred = AWS.config.credentials;
            cred.refresh(function (err) {
                if (err) console.log(err);
                else {
                    let accessKey = cred.accessKeyId;
                    let secretKey = cred.secretAccessKey;
                    let sessionToken = cred.sessionToken;
                    console.log('accessKey: ' + accessKey);
                    console.log('secretKey: ' + secretKey);
                    console.log('sessionToken:' + sessionToken);
                }
            });
        });
    }
}

export function getCurrentUser(){
    const userPool = new AmazonCognitoIdentity.CognitoUserPool(poolData);
    const cognitoUser = userPool.getCurrentUser();
    
    return new Promise((r, j) => {
        if (cognitoUser != null) {
            cognitoUser.getSession(function (err, session) {
                if (err) {
                    j(err.message || JSON.stringify(err));
                    return;
                }
                useremail = session.idToken.payload.email;
                r();
            });
        }else{
            j('No user Info');
        }
    });
}

export function getUserEmail() { 
    return useremail;
 }