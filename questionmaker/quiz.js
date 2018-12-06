function generateQuiz(questions, quizContainer, resultsContainer, submitButton) {

    function showQuestions(questions, quizContainer) {
        var output = [];
        var answers;

        // for each question...
        for (var i = 0; i < questions.length; i++) {

            // first reset the list of answers
            answers = [];

            // true false
            if (questions[i].type == 'tf') {
                // ...add an html radio button
                answers.push(
                    '<label>' +
                    '<input type="radio" name="question' +
                    i +
                    '" value="' +
                    't' +
                    '">' +
                    'True' +
                    '</label>'
                );
                answers.push(
                    '<label>' +
                    '<input type="radio" name="question' +
                    i +
                    '" value="' +
                    'f' +
                    '">' +
                    'False' +
                    '</label>'
                );

                // add this question and its answers to the output
                output.push(
                    '<div class="question">' + "True or False: " + questions[i].question + '</div>' +
                    '<div class="answers">' + answers.join('') + '</div>'
                );
            }
            // multiple choice
            else if (questions[i].type == 'mc') {
                // for each available answer to this question...
                for (var letter in questions[i].answers) {

                    // ...add an html radio button
                    answers.push(
                        '<label>' +
                        '<input type="radio" name="question' +
                        i +
                        '" value="' +
                        letter +
                        '">' +
                        letter +
                        ': ' +
                        questions[i].answers[letter] +
                        '</label>' + '<br>'
                    );
                }

                // add this question and its answers to the output
                output.push(
                    '<div class="question">' + questions[i].question + '</div>' +
                    '<div class="answers">' + answers.join('') + '</div>'
                );
            }
        }

        // finally combine our output list into one string of html and put it on the page
        quizContainer.innerHTML = output.join('');
    }

    // show the questions
    showQuestions(questions, quizContainer);

    function showResults(questions, quizContainer, resultsContainer) {

        // gather answer containers from our quiz
        var answerContainers = quizContainer.querySelectorAll('.answers');

        // keep track of user's answers
        var userAnswer = '';
        var numCorrect = 0;

        // for each question...
        for (var i = 0; i < questions.length; i++) {

            // find selected answer
            userAnswer = (answerContainers[i].querySelector('input[name=question' + i + ']:checked') || {}).value;

            // if answer is correct
            if (userAnswer === questions[i].correctAnswer) {
                // add to the number of correct answers
                numCorrect++;

                // color the answers green
                answerContainers[i].style.color = 'lightgreen';
            }
            // if answer is wrong or blank
            else {
                // color the answers red
                answerContainers[i].style.color = 'red';
            }
        }

        // show number of correct answers out of total
        resultsContainer.innerHTML = numCorrect + ' out of ' + questions.length;
    }
    // when user clicks submit, show results
    submitButton.onclick = function() {
        showResults(questions, quizContainer, resultsContainer);
    }
}

var quizContainer = document.getElementById('quiz');
var resultsContainer = document.getElementById('results');
var submitButton = document.getElementById('submit');

function show_selected(value) {
        if (typeof value == 'undefined'){
        console.log("Invalid quiz")
        quizContainer.innerHTML = "Invalid quiz option!"
        resultsContainer.innerHTML = ""
        document.getElementById("submit").classList.add('show');
    }
    else {
        generateQuiz(value, quizContainer, resultsContainer, submitButton);
        document.getElementById("submit").classList.remove('show');
    }
}

function get_selected() {

    var selector = document.getElementById('quizselect');
    // var value = selector[selector.selectedIndex].value;
    var value = selector[selector.selectedIndex].value;
    var value = window[value];
    show_selected(value);
}

document.getElementById('selectbtn').addEventListener('click', get_selected);