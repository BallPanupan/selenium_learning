const {Builder, By, Key, until} = require('selenium-webdriver');
const fs = require('fs');
let object = [];

function saveLog(data) {
    let milliseconds = new Date().getTime();
    let today = new Date();
    let date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
    let fileName = milliseconds + ".txt";

    fs.writeFile("log/"+fileName, data, function(err) {
        if (err) {
            console.log(err);
        }
    });
}

// process.exit(1)

(async function example() {
    let driver = await new Builder().forBrowser('chrome').build();
    let data = {};

    try {
        await driver.get('http://www.google.com/');
        await driver.getTitle();
        await driver.findElement(By.name('q')).sendKeys('webdriver', Key.RETURN);
        
        data['Title-Page'] = await driver.getTitle();

        object.push(data);

    } finally {
        saveLog(JSON.stringify(object, undefined, 4));
        
        await driver.quit();
    }

})();