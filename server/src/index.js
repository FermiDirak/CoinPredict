const dotenv = require('dotenv');
const WebSocket = require('ws');
const gdax = require('gdax');

dotenv.config();

const gdaxClient = new gdax.PublicClient();
const gdaxSocket = new gdax.WebsocketClient(['BTC-USD']);

// gdaxSocket.on('message', (data) => {
//   if (data.type === 'match') {
//     console.log(data);
//   }
// });

gdaxClient.getProductTrades('BTC-USD', { after: 10000100, limit: 100 }, (err, response, data) => {
  console.log(data);
});

