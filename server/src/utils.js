/** Sleeps process for ms milliseconds
 * @param {number} ms The number of milliseconds to sleep
 * @return {Promise} A promise that resolves after ms milliseconds
 */
let sleep = ms => new Promise(resolve => setTimeout(resolve, ms));

module.exports = { sleep };