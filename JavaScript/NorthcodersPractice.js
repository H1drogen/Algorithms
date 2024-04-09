
function findFirstOdd(numbers) {
    for (let nums in numbers) {
        if (nums % 2 === 1){
            return nums
        }
    }
    //The issue with your function findFirstOdd is that you're using a for...in loop to iterate over an array. The for...in loop in JavaScript is used to iterate over the enumerable properties of an object, not the elements of an array. When used with an array, it returns the indices (as strings), not the actual elements.
    // To fix this, you should use a for...of loop or a traditional for loop to iterate over the array
}

function findEvenLengthStrings(items) {
    for (let item of items){
        if (typeof item !== 'string' || item.length % 2 !== 0) {
            items.pop(item)
        }
    }
}
// need to use splice instead of pop
// be careful with typeof
findEvenLengthStrings([ 'apple', 'banana', 'pear', 'grape', 'kiwi' ])


function isThisAPalindrome(str) {
    // Your code goes here...
    for (i = 0; i < (str.length / 2); i++){
        if (str[i] === str[str.length - i - 1]){
            continue
        }
        else {
            return false
        }
    }
    return true
}
// don't forget the -1 in the second index
// don't forget let in your for loop


isThisAPalindrome('racecar')

function checkIsPrime(num) {
    switch (num) {
        case 1:
            return false
        case 2:
            return true
    }
    // Your code goes here...
    for (let i = num - 1; i = 2; i-- ) {
        if (num % i === 0) {
            return false
        }
    }
    return true
}

// don't forget to use the correct comparison operator in your for loop (i > 1 instead of i = 2)

function greetGuest(name) {
    capitalLetter = name[0].toUpperCase()
    return `Hello ${capitalLetter}${name.slice(1)}!`
}
// don't forget parenthesis on the toUpperCase method
// slice instead of splice for strings

greetGuest('alice')


function findTicketPrices(emailString) {
    // Your code goes here...
    for (let i = 0; i < emailString.length; i++) {
        if (isNaN(parseInt(emailString[i])) === false) {
            return true
        }
    }
    return false
}
// typeof will return 'string' for numbers in a string
// learned about isNaN function and parseInt function

findTicketPrices("Hello, I think I can pay 11 pounds, is that alright?");

function makeGuestList(person) {
    const firstName = person.name.split(' ')[0]
    const lastName = person.name.split(' ')[1]

    delete person.name
    person['firstName'] = firstName
    person['lastName'] = lastName

    return person
}

function isPartyViable(guests) {
    const numberOfGuests = guests.length
    let ticketSales = 0
    if (numberOfGuests >= 5) {
        for (let i = 0; i < guests.length; i++) {
            ticketSales += guests[i].paidForTicket
        }
        if (ticketSales >= 100) {
            return true
        }
    }
    return false
}


function orderSupplies(supplies, guests) {
    let value = 0
    for (const key in supplies) {
        value += supplies[key]
    }
    return value * guests
}

// use Object.values() method to get an array of all the values in the object

function calculateTaxiFare(seconds) {
    // Your code goes here...
    const minutes = parseInt(seconds / 60) + 1
    let price = 500
    if (minutes <= 3) {
        return price
    } else {
        price += (minutes - 3) * 70
        return price
    }
}

// use Math.ceil() to round up to the nearest minute

calculateTaxiFare(301)

function pickWinners(numbers) {
    // Your code goes here...
    let object = []
    for (let i = 1; i < numbers.length; i +=2){
        if (numbers[i] % 2 !== 0){
            object.push({
                'seat': i,
                'ticketCost': numbers[i]
            })
        }
    }
    return object
}

pickWinners([6, 7, 12, 49])

function gatherFeedback(feedbackArray) {
    let positive = 0
    let negative = 0
    let neutral = 0
    for (let i = 0; i < feedbackArray.length; i++) {
        let feedback = feedbackArray[i][1]
        if (feedback <= 3){
            negative += 1
        } else if (feedback > 3 && feedback <= 6) {
            neutral += 1
        } else {
            positive += 1
        }
    }
    return {
        'positive': positive,
        'negative': negative,
        'neutral': neutral
    }
}

gatherFeedback([['maddie', 10], ['jatinder', 3], ['rose', 6]]);


