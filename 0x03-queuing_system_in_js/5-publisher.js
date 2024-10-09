// 5-subscriber.js

import { createClient } from 'redis';

const subscriber = createClient(); // we create a Redis client

// listen to the "connect" event to confirm successful connection
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

// listen for the 'error' event to handle connection errors
subscriber.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

// subscribe to the holberton school channel
subscriber.subscribe('holberton school');

// handle messages received from the channel
subscriber.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe(channel);
    subscriber.quit();
  }
});
