
function fnction(height, weight) {
    let bmi = weight / height ** 2
    switch (bmi) {
        case bmi < 18.5:
            return 'Underweight'
        case bmi < 24.9:
            return 'Normal'
        case bmi < 29.9:
            return 'Overweight'
        case bmi < 34.9:
            return 'Obese'
        case bmi >= 35:
            return 'Extremely Obese'
    }
}

fnction('1.75', '70')