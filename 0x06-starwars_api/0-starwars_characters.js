#!/usr/bin/node

const request = require('request');

// Get movie ID from command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID');
  process.exit(1);
}

const BASE_URL = 'https://swapi.dev/api';

// Function to make HTTP request as Promise
function makeRequest(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

// Function to get character name from URL
async function getCharacterName(url) {
  try {
    const character = await makeRequest(url);
    return character.name;
  } catch (error) {
    console.error(`Error fetching character: ${error}`);
    return null;
  }
}

// Main function to get and print all characters
async function printMovieCharacters(movieId) {
  try {
    // Get movie data
    const movie = await makeRequest(`${BASE_URL}/films/${movieId}/`);
    
    // Get all character names in order
    const characterPromises = movie.characters.map(url => getCharacterName(url));
    const names = await Promise.all(characterPromises);
    
    // Print names (filtering out any null values from errors)
    names.filter(name => name !== null).forEach(name => console.log(name));
  } catch (error) {
    console.error(`Error: ${error}`);
    process.exit(1);
  }
}

// Execute the main function
printMovieCharacters(movieId);
