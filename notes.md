# Notes:

* fill_price: The market price of a security in practice

* Datacenter: US East N. Virginia (us-east-1)

* rest endpoint: https://api.pro.coinbase.com

* all requests/responses use content-type `application/json`

* ISO 8601 time format for all timestamps

* Decimal numbers passed as strings. Not integers

* 429 => too many requests

* stp: Self-trade prevention

* limit vs market orders:
  * limit: price & size - PREFERED
      to be filled at specified price or better
      (will be open indefinitely if not met)

  * market: Buy at market rate.
      Incurs _TAKER_FEES_

* stop orders become active when a market threshold is reached
  * loss: stops trades when market drops BELOW
  * entry: stops trades when market goes ABOVE

* quote_increment: The smallest accepted increment of currency. (1 penny)

Time in force:
* lol:  fill or kill
* IOC: Immediate or Cancel

* Open / Pending / Active

* base_min_size - base_max_size defines min/max order size


/products/product_id/book :

tuple[ price, size, aggregated # of orders ]


/product/product_id/ticker

shape {
  trade_id, // can be used to identify dropped trades
  price, // fill price of currency
  size, //requested amount
  bid:,
  ask,
  volume,
  time,
}

received means that the order has been received by the _matching engine_