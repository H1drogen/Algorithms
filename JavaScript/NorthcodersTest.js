
function makeAlternatingArray(array) {
    // please complete this function ...
    let altArray = []
    for (let i = 0; i < array.length; i++) {
        if (i % 2 === 0) {
            altArray.push(array[i])
        }
    }
}

function countTheCapitals(string) {
    // write your code here
    let capitalLetters = 0
    for (let char of string) {
        if (char === char.toUpperCase()) {
            capitalLetters++
        }
    }
    return capitalLetters
}

countTheCapitals('Hello World')


function findKnifeAndFork(utensils) {
    ans = {
        knife: -1,
        fork: -1
    }
    for (let i = 0; i < utensils.length; i++){
        if (utensils[i] === 'knife') {
            ans['knife'] = i
        } else if (utensils[i] === 'fork') {
            ans['fork'] = i
        }
    }
    return ans
}

function truncateString(str, n) {
    // please complete this function ...
    if (str.length > n) {
        return str.slice(0,9) + '...'
    } else {
        return str
    }
}

// function countTheShouts(strings) {
//     // write your code here
//     let shouted = 0
//     for (let string of strings) {
//         if (string.pop() === '!') {
//             shouted++
//         }
//     }
//     return shouted
// }

// countTheShouts(['Hello!', 'How are you?', 'I am great!'])

function roundUpToNearestMultiple(n, x) {
    // write your code here
    if (x === 0) {
        return -1
    }
    let count = 0
    while (count < n) {
        count += x
    }
    return count
}

roundUpToNearestMultiple(21, 5)