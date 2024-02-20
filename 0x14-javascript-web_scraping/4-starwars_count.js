#!/usr/bin/node
const the_request = require("request");
the_request(process.argv[2], function (error, response, body) {
  if (!error) {
    const resp_data = JSON.parse(body).results;
    console.log(
      resp_data.reduce((count, movie) => {
        return movie.characters.find((character) => character.endsWith("/18/"))
          ? count + 1
          : count;
      }, 0)
    );
  }
});
