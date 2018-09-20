require('dotenv').config();
const WebSocket = require('ws');
const {createSocket, gdaxClient, gdaxSocket} = require('./gdax');
const influx = require('./influx');
const {CURRENCIES, MIN_TRADE_ID} = require('./constants');

let firstTradeIds = {/* BTC, ETH */};
let lastTradeIds = {/* BTC, ETH */};

// evaluate firstTradeIds
CURRENCIES.forEach((currency, i) => {
  firstTradeIds[currency] = influx.getFirstTradeId(currency) || MIN_TRADE_ID;
});


/** called when stream starts coming in */
function onStart(data) {
  const currency = data.product_id;

  /// update last trade id
  lastTradeIds[currency] = data.trade_id;

  // for (let i = firstTradeIds[currency] + 100; i < lastTradeIds[currency] - 100; ++i) {
  //   gdaxClient.getProductTrades(currency, { after: i, limit: 100 }, (err, response, data) => {
  //     //do something with this data
  //   });
  // });

}

/** called every transactional tick */
function onTick(data) {
  const currency = data.product_id;

  console.log(data);

  /// update last trade id
  lastTradeIds[currency] = data.trade_id;

  console.log(firstTradeIds['BTC-USD'], lastTradeIds['BTC-USD'])

}

createSocket(onStart, onTick);