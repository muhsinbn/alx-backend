// 2-redis_client.js

import { createClient, print } from 'redis';
import { promisify } from 'util';

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

// let's promisify the client.get method
const getAsync = promisify(client.get).bind(client);

/**
 * Displays the value of a given key using the promisified getAsync function
 * Using async/await
 * @param {string} schoolName - The key name
 */

async function displaySchoolValue(schoolName) {
  try {
    const result = await getAsync(schoolName);
    console.log(result);
  } catch (error) {
    console.error(error);
  }
}

// Function calls
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
