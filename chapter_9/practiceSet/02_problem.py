import random;

def game():
    print("You are playing the game..")
    score = random.randint(1, 62);
    # Fetch the highScore
    with open("highScore.txt") as f:
        highScore = f.read();
        if(highScore != ""):
            highScore = int(highScore);
        else:
            highScore = 0;

    print(f"Your score: {score}");
    if(score>highScore or highScore == ""):
        # write this highScore to the file
        with open("highScore.txt", "w") as f:
            f.write(str(score));
    
    return score;

game();