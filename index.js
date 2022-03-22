const { Builder } = require("selenium-webdriver");
const chrome = require('selenium-webdriver/chrome');

async function main() {
    let options = new chrome.Options();
    let driver = await new Builder()
      .forBrowser('chrome')
      .setChromeOptions(options)
      .build();
    
    await driver.quit();
}
main();