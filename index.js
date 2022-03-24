const {Builder, By, Key, until} = require('selenium-webdriver');
const fs = require('fs');
let object = [];

function saveLog(data) {
    let milliseconds = new Date().getTime();
    let today = new Date();
    let date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
    // let fileName = milliseconds + ".txt";
    let fileName = "GetTable.json";
    
    fs.writeFile("log/"+fileName, data, function(err) {
        if (err) {
            console.log(err);
        }
    });
}

async function example(target) {
    let driver = await new Builder().forBrowser('chrome').build();
    let data = {};

    try {
        await driver.getTitle();
        await driver.get(target.url);
        
        data['Title-Page'] = await driver.getTitle();
        data['Element'] = await driver.findElement({className:'tableizer-table sortable'});

        let elements = await driver.findElements(By.className('tableizer-table sortable'));

        // console.log(driver);
        for(let e of elements) {
            console.log(await e.getText());
        }


    } finally {
        saveLog(JSON.stringify(object, undefined, 4));
        await driver.quit();
    }

}

// get target
let target = fs.readFileSync('target.json');
let targetList = JSON.parse(target);

targetList.map((data, index) => {
    // console.log(data)
    example(data);

});


// process.exit(1)