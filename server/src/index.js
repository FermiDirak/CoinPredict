const dotenv = require('dotenv');
const WebSocket = require('ws');
const Influx = require('influx');
const GDAX = require('gdax');

dotenv.config();

const MIN_TRADE_ID = 10000000;
const CURRENCIES = ['BTC-USD', 'ETH-USD']

const gdaxClient = new GDAX.PublicClient();
const gdaxSocket = new GDAX.WebsocketClient(CURRENCIES);

const influx = new Influx.InfluxDB({
  host: 'localhost',
  database: 'coin_predict',
  schema: [
    {
      measurement: CURRENCIES[0],
      fields: {
        price: Influx.FieldType.FLOAT,
        size: Influx.FieldType.FLOAT,
        trade_id: Influx.FieldType.INTEGER,
      },
      tags: [
        'side',
      ]
    },
    {
      measurement: CURRENCIES[1],
      fields: {
        price: Influx.FieldType.FLOAT,
        size: Influx.FieldType.FLOAT,
        trade_id: Influx.FieldType.INTEGER,
      },
      tags: [
        'side',
      ],
    },
  ],
});

gdaxSocket.on('message', (data) => {
  if (data.type === 'match') {
    console.log(data);
  }
});



return 0;

// (async () => {

//   // iterate on trades starting from LAST_ENTRY or 10000000
//   // and populate tables with trade data for BTC-USD

//   CURRENCIES.forEach(async (currency) => {

//     // get the last entry from trades table
//     const lastTradeId = await getLastTradeId() || MIN_TRADE_ID;

//     const


//   });



// })();

// /** Gets the trade id of the last trade
//  * @return the last trade number or undefined if no entries exist
//  */
// async function getLastTradeId() {
//   let tradeIds = await influx.query(`select "trade_id" from "BTC-USD" limit 1`);

//   return undefined;
// }







// gdaxSocket.on('message', (data) => {
//   if (data.type === 'match') {
//     console.log(data);
//   }
// });

// gdaxClient.getProductTrades('BTC-USD', { after: 10000100, limit: 100 }, (err, response, data) => {
//   console.log(data);
// });
