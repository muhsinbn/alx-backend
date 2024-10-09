// 4-redis_advanced_op.js

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
 * Sets value in a Redis hash
 */
function createHash() {
  const schools = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };

  for (const [city, value] of Object.entries(schools)) {
    client.hset('HolbertonSchools', city, value, print);
  }
}

/**
 * Displays the value of a given field in a Redis hash
 */
function displayHash() {
  client.hgetall('HolbertonSchools', (err, object) => {
    if (err) {
      console.error(err);
    } else {
      console.log(object);
    }
  });
}

// Function calls
createHash();
displayHash();
