#!/usr/bin/node

const the_request = require("request");
const epsNumber = process.argv[2];
const apiURL = "https://swapi-api.hbtn.io/api/films/";

the_request(apiURL + epsNumber, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log("Error code: " + response.statusCode);
  }
});
