
function doWeStockIt() {
    // Only change the code below this line
    const inStock = true;
    const description = 'This is a "lovely" ball of brown wool';
    const amount = 4.5;
    //
    // Don't change the code below this line
    return [
        inStock,
        description,
        amount
    ];
}

const opinion = 'I love ${codingLanguage}'


// const dog = {
//     sound: "Woof"
//     legs: 4
//     isGoodBoy: true
//     dogNames:["Pluto","Scooby","Spot"]
// }

function createPirate() {
    const pirateProfile = {
        realName: 'Edward Teach',
        shipName: 'La Concorde',
        treasure: {
            gems: 10,
            piecesOf8: 7,
            goldCoins: 150
        }
    };
    pirateProfile[2] = 'Blackbeard'
    delete pirateProfile.realName
    pirateProfile.treasure.piecesof8 = 8
    pirateProfile.shipName = 'Queen Anne\'s Revenge'
    return pirateProfile;
}

createPirate()

