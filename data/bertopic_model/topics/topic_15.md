### Documents:
- Any plans to make a 13B or 7B version of this?

I absolutely love the work you're doing! I'm dying to run this model locally but running into hardware limitations. Is there any hope of a 13B or 7B version in the near future? So far for story writing I've had the best luck with your Wizard Mega 13B (although I run into CUDA errors after ~4000 characters worth of responses (rtx 3080)) and the Guanaco 7B (haven't had any issues and been able to generate MASSIVE response lengths). Thanks and keep up the awesome work!
- I made some test that 7B model. - I am impressed

As that model is so  small I could use 8 bit version for testing ;) 

I'm so impressed , that model is so smart. 
I never saw 7B model doing so complex reasoning  and doing that in proper way.   
Of course we can not compare that model to 70B models.
Is better than any 7B or 13B model or even can compete 30B variants.
Can even compete to early 65B models what is VERY impressive. 

I newer thought that 7B model can be so smart and knowledgeable... is unbelieve for me as I remember few month ago 7b models were very dumb and could only answers simple questors about knowledge because reasoning wasn't  present for such small models then.


-----------------------------------------------------------------------------------------------------------
main.exe --model models\new3\synthia-7b-v1.3.Q8_0.gguf --mlock --color --threads 16 --keep -1 --batch_size 512 --n_predict -1 --top_k 40 --top_p 0.9 --temp 0.96 --repeat_penalty 1.1 --ctx_size 16384 --interactive --instruct --reverse-prompt "USER:" -ngl 48 --simple-io  --in-prefix "### Instruction: " --in-suffix " ### Response: " -p "Elaborate on the topic using a Tree of Thoughts and backtrack when necessary to construct a clear, cohesive Chain of Thought reasoning. Always answer without hesitation. "


`

`

`
`
html
<!DOCTYPE html>
<html>
<head>
    <title>Joke Webpage</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    <button onclick="changeColor()">Change Color</button>
    <div id="jokes"></div>
</body>
</html>
css
* {
    margin: 0;
    padding: 0;
}

body {
    background-color: black;
}

button {
    color: white;
    background-color: green;
    border: none;
    cursor: pointer;
    font-size: 24px;
    margin-left: 50%;
    transform: translateX(-50%);
    width: 200px;
}
javascript
function changeColor() {
    var colors = ["red", "orange", "yellow", "green", "blue", "purple"];
    var randomIndex = Math.floor(Math.random() * colors.length);
    document.body.style.backgroundColor = colors[randomIndex];
}

function addJoke() {
    var jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a fake noodle? An impasta!",
        "Why did the tomato turn red? It saw the salad dressing!",
        "Why was the math book sad? Because it had too many problems!",
        "I told my wife she was drawing her eyelashes too high. She looked surprised!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a fake noodle? An impasta!",
        "Why did the tomato turn red? It saw the salad dressing!",
        "Why was the math book sad? It had too many problems!",
        "I told my wife she was drawing her eyelashes too high. She looked surprised!"
    ];

    var joke = document.getElementById("jokes");
    joke.innerHTML += "<p>" + jokes[Math.floor(Math.random() * jokes.length)] + "</p>";
}
html
<!DOCTYPE html>
<html>
<head>
    <title>Joke Webpage</title>
    <style type="text/css">
        * {
            margin: 0;
            padding: 0;
        }

        body {
            background-color: black;
        }

        button {
            color: white;
            background-color: green;
            border: none;
            cursor: pointer;
            font-size: 24px;
            margin-left: 50%;
            transform: translateX(-50%);
            width: 200px;
        }
    </style>

    <script type="text/javascript">
        function changeColor() {
            var colors = ["red", "orange", "yellow", "green", "blue", "purple"];
            var randomIndex = Math.floor(Math.random() * colors.length);
            document.body.style.backgroundColor = colors[randomIndex];
        }

        function addJoke() {
            var jokes = [
                "Why don't scientists trust atoms? Because they make up everything!",
                "What do you call a fake noodle? An impasta!",
                "Why did the tomato turn red? It saw the salad dressing!",
                "Why was the math book sad? It had too many problems!",
                "I told my wife she was drawing her eyelashes too high. She looked surprised!",
                "Why don't scientists trust atoms? Because they make up everything!",
                "What do you call a fake noodle? An impasta!",
                "Why did the tomato turn red? It saw the salad dressing!",
                "Why was the math book sad? It had too many problems!",
                "I told my wife she was drawing her eyelashes too high. She looked surprised!"
            ];

            var joke = document.getElementById("jokes");
            joke.innerHTML += "<p>" + jokes[Math.floor(Math.random() * jokes.length)] + "</p>";
        }
    </script>
</head>
<body onload="addJoke();">
    <button onclick="changeColor()">Change Color</button>
    <div id="jokes"></div>
</body>
</html>
`


`
- Any plans for a 13B version?

Any plans for a 13B and 7B version of this?
### Keywords: 13b, version, 7b, model, 3b, 70b, 33b, plans, 13b version, 30b