/** Sets up Influx schemas */

const {CURRENCIES} = require('./constants');
const Influx = require('influx');

const DB_NAME = 'coin_predict';

const influx = new Influx.InfluxDB({
  host: 'localhost',
  database: DB_NAME,
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

// create db if it doesn't exist
influx.getDatabaseNames()
  .then(names => {
    if (!names.includes(DB_NAME)) {
      return influx.createDatabase(DB_NAME);
    }
  })
  .catch(error => {
    console.error(`Error creating Influx database ${DB_NAME}`);
  });

/** gets the first trade id
 * @param {string} currency The currency to get the first Trade Id for in the db
 */
influx.getFirstTradeId = currency => {
  const query = `SELECT * FROM "${currency}" LIMIT 2`;

  influx.queryRaw(query)
    .then(rawData => {
      console.log(rawData);
    })
    .catch(error => {
      console.error(`query '${query}' failed: ${error}`);
    });

  return null;
}

module.exports = influx;