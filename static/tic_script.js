let buttons = document.getElementsByClassName("btn");
let restart = document.getElementById("button_restart");
let label_result = document.getElementById("label_result");
let button_easy = false;
let button_hard = false;

function check() {
    label_result.innerText = "Your Sign: O"
    button_easy = document.getElementById("button_easy").checked;
    button_hard = document.getElementById("button_hard").checked;
}

restart.addEventListener('click', (event) => {
    let difficulty;
    if (button_easy || button_hard) {
        difficulty = button_easy ? "easy" : "hard";

        fetch('/tictactoe', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "changed_button": "",
                "changed_choice": "",
                "restart": "True",
                "difficulty": difficulty
            })
        })
            .then(resp => resp.json())
            .then(data => {
                    for (let i = 0; i < buttons.length; i++) {
                        buttons[i].innerText = '';
                    }
                    label_result.innerText = "Your Sign: O"
                }
            )
            .catch(error => {
                console.error(error);
            });
    }
});

for (let i = 0; i < buttons.length; i++) {
    let button = buttons[i]
    button.addEventListener('click', function(){
        if(button.innerText === '') {
            let difficulty;
            if (button_easy || button_hard) {
                difficulty = button_easy ? "easy" : "hard";
                button.innerText = 'O';

                fetch('/tictactoe', {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        "changed_button": button.id,
                        "changed_choice": 'O',
                        "restart": "False",
                        "difficulty": difficulty
                    })
                })
                    .then(resp => resp.json())
                    .then(data => {
                            for (let i = 0; i < buttons.length; i++) {
                                buttons[i].innerText = data['buttons'][i]['choice'];
                            }
                            let winner = data['winner'];
                            if (winner === 'X')
                                label_result.innerText = 'You Lost!'
                            else if (winner === 'O')
                                label_result.innerText = "You Won!"
                            else if (winner === 'Tie')
                                label_result.innerText = "That's a Tie!"
                            else
                                label_result.innerText = "Your Sign: O"
                        }
                    )
                    .catch(error => {
                        console.error(error);
                    });
            }
        }
    });

}