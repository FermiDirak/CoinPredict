const dotenv = require('dotenv');
const express = require('express');
const WebSocket = require('ws');
const gdax = require('gdax');


dotenv.config();
const app = express();

const gdaxClient = new gdax.PublicClient();
const gdaxSocket = new gdax.WebsocketClient(['BTC-USD']);

gdaxSocket.on('message', (data) => {
  if (data.type === 'match') {
    console.log(data);
  }
});


/* ---------------------------- server listening --------------------------- */

const port = process.env.PORT || 5000;

app.listen(port, () => {
  console.log(`server connected on port ${port}`);
});