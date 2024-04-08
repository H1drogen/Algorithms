

function sayHello(country, time) {
    let greeting;
    // In JavaScript, the expression 0 <= time < 12 doesn't work as expected because it doesn't evaluate the way it would in some other languages like Python.
    // In JavaScript, this expression is evaluated from left to right. So, 0 <= time < 12 is actually interpreted as (0 <= time) < 12.
    // First, 0 <= time is evaluated. This results in a boolean value, either true (if time is greater than or equal to 0) or false.  Then, this boolean value is compared with 12. In JavaScript, true is loosely equal to 1 and false is loosely equal to 0. So if time is greater than or equal to 0, true < 12 is evaluated, which is always true. If time is less than 0, false < 12 is evaluated, which is also always true.
    // To get the desired result, you should separate the conditions like this: 0 <= time && time < 12.
    if (0 <= time < 12) {
        switch (country) {
            case 'Spain':
            case 'Mexico':
                greeting = 'buenos dias'
                break;
            case 'France':
                greeting = 'bon matin'
        }
    } else if (12 <= time < 24) {
        switch (country) {
            case 'Spain':
            case 'Mexico':
                greeting = 'buenos noches'
                break;
            case 'France':
                greeting = 'bon soir'
        }
    } else {
        greeting = null
    }
}

const daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

const weekend = []
weekend.slice(5)
console.log(weekend)

function createToDoList() {
    const toDoList = [];
    // Do not alter any code above here

    toDoList.push(['Clean the house', 10], ['Walk the dog', 15], ['Do the shopping', 20], ['Cook dinner', 30], ['Wash the car', 45]);

    // Do not alter any code below here
    return toDoList;
}

// for (let i = 0; i <= 21; i++) {
//     if (i % 3 === 0):
//     console.log(i)
// }
//
// const numbers = [2, 4, 5, 6, 9, 10, 11, 12]
// // Start writing your code below
// for (let i = 0; i < numbers.length; i++){
//     if numbers[i] % 2 === 0 {
//         console.log(numbers[i])
//     }
// }


function findEfficientBulbs(serialNumbers) {
    console.log(serialNumbers);
    const efficientSerialNumbers = [];

    for (let i = 0; i < serialNumbers.length; i++) {
        let serialNumber = serialNumbers[i]
        if ((serialNumber % 2 !== 0) && (serialNumber.length === 6)){
            efficientSerialNumbers.push(serialNumber)
        }
    }

    return efficientSerialNumbers;
}
// to find the length of a number, convert it to String and then use the length property
console.log(findEfficientBulbs([ 123456, 234567, 345678, 456789 ]))


function countCats() {
    const tutorPetTypes = {
        'Sarah': ['cat'],
        'Jim': ['dog', 'dog'],
        'Joe': ['mouse'],
        'Róisín': ['cat', 'cat', 'cat', 'cat', 'cat', 'dog'],
        'Edd': ['lizard', 'cat'],
        'Lewis': ['bearded dragon', 'tortoise']
    }

    let totalCats = 0
// Start typing below this line
    for (const key in tutorPetTypes) {
        pets = tutorPetTypes[key]
        for (let i = 0; i < pets.length; i++) {
            if (pets[i] === 'cat') {
                totalCats++
            }
        }
    }
}
countCats()