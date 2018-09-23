require('dotenv').config();
const WebSocket = require('ws');
const {createSocket, gdaxClient, gdaxSocket} = require('./gdax');
const influx = require('./influx');
const {CURRENCIES, MIN_TRADE_ID} = require('./constants');
const {sleep} = require('./utils');

let firstTradeIds = {/* BTC, ETH */};
let lastTradeIds = {/* BTC, ETH */};

// evaluate firstTradeIds
CURRENCIES.forEach((currency, i) => {
  influx.getFirstTradeId(currency)
    .then(firstTradeId => {
      console.log(firstTradeId);
      firstTradeIds[currency] = firstTradeId;
    });
});

/** called on the very first tick */
async function onStart(data) {
  const currency = data.product_id;

  // update last trade id
  lastTradeIds[currency] = data.trade_id;

  await scrapeTrades();

  async function scrapeTrades() {

    for (let i = firstTradeIds[currency] + 100; i < lastTradeIds[currency] - 100; i += 100) {
      console.log(`currency ${currency} at trade id ${i}`);

      // getProductTrades is rate limited
      const data = await gdaxClient.getProductTrades(currency, {after: i, limit: 100});

      await sleep(200);

      influx.writePoints(
        data.map(datum => {
          return {
            measurement: currency,
            fields: {
              trade_id: datum.trade_id,
              price: datum.price,
              size: datum.size,
            },
            tags: {
              side: datum.side,
            },
            timestamp: '' + Date.parse(datum.time) + '000000',
          };
        })
      ).catch(err => {
        console.error(`Error saving data to InfluxDB! ${err.stack}`);
        process.exit();
      });
    }

    console.log(`done with currency ${currency}`);
  }

}

/** called every transactional tick */
async function onTick(data) {
  const currency = data.product_id;

  console.log(data);

  /// update last trade id
  lastTradeIds[currency] = data.trade_id;

  console.log(firstTradeIds['BTC-USD'], lastTradeIds['BTC-USD'])

}

createSocket(onStart, onTick);
