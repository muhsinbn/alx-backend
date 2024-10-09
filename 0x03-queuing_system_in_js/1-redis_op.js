// 1-redis_client.js

import { createClient, print } from 'redis';

const client = createClient(); // we create a Redis client

// Listen for the 'connect' event to confirm successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Listen for the 'error' event to handle connection errors
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

/**
 * Sets a new key-value pair in the Redis database
 * @param {string} schoolName - The key name
 * @param {string} value - The value to set
 */

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print); // print logs the result of the operation
}

/**
 * Displays the value of a given key
 * @param {string} schoolName - The key name
 */

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(err);
    } else {
      console.log(reply);
    }
  });
}

// Function calls
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
