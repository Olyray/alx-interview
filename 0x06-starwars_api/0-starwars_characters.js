#!/usr/bin/node

const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  request(`${API_URL}/films/${movieId}/`, (err, _, body) => {
    if (err) {
      return console.error(err);
    }

    const charactersURLs = JSON.parse(body).characters;
    const characterPromises = charactersURLs.map(url => {
      return new Promise((resolve, reject) => {
        request(url, (error, __, characterBody) => {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(characterBody).name);
          }
        });
      });
    });

    Promise.all(characterPromises)
      .then(names => {
        names.forEach(name => console.log(name));
      })
      .catch(error => console.error(error));
  });
}
