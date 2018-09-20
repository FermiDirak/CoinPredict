const {CURRENCIES} = require('./constants');
const GDAX = require('gdax');

/**
 * Creates a gdax Socket
 * @param {callback} onStart Called when feed starts
 */
function createSocket(onStart, onTick) {
  const gdaxSocket = new GDAX.WebsocketClient(CURRENCIES);

  // used to mark if the stream has started
  let streamStarted = CURRENCIES.reduce((acc, currency) => {
    acc[currency] = false;
    return acc;
  } , {});

  gdaxSocket.on('message', (data) => {
    const currency = data.product_id;

    if (data.type === 'match') {
      if (!streamStarted[currency]) {
        streamStarted[currency] = true;

        onStart(data);
      }

      onTick(data);
    }
  });

  return gdaxSocket;
}


const gdaxClient = new GDAX.PublicClient();
const gdaxSocket = new GDAX.WebsocketClient(CURRENCIES);






module.exports = {createSocket, gdaxClient, gdaxSocket};