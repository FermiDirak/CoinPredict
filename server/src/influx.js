/** Sets up Influx schemas */

const {CURRENCIES} = require('./constants');
const Influx = require('influx');


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

module.exports = influx;