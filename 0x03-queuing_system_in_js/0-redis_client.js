// 0-redis_client.js

import { createClient } from 'redis';

const client = createClient(); // we create a Redis client

// Listen for the 'connect' event to confirm successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Listen for the 'error' event to handle connection errors
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});
