// 5-publisher.js

import redis from 'redis';

// Create a Redis client
const publisher = redis.createClient();

// Listen for the 'connect' event to confirm successful connection
publisher.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Listen for the 'error' event to handle connection errors
publisher.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

/**
 * Publishes a message to the channel after a specified time.
 * @param {string} message - The message to publish.
 * @param {number} time - The delay in milliseconds before publishing the message.
 */
function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    publisher.publish('holberton school channel', message);
  }, time);
}

// Function calls
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
