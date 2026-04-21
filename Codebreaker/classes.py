import random

# responsible for running the game
class Game:
    def __init__(self, code, player, evaluator):
        self.code = code
        self.player = player
        self.evaluator = evaluator
        self.max_attempts = 8
        self.won = False

    def play(self):
        while self.player.attempts_used < self.max_attempts and not self.won:
            guess = self.player.make_guess()
            self.player.store_guess(guess)
            self.process_turn(guess)

    def process_turn(self, guess):
        exact, partial = self.evaluator.evaluate(self.code.get_code(), guess)
        attempts_used = self.player.get_attempts_used()
        attempts_remaining = self.max_attempts - attempts_used
        if self._check_win(exact):
            print("YOU WON!")
            self.won = True
        elif self._check_loss():
            print("You lost!")
        else:
            print(f"You have {exact} exact mathches, {partial} partial matches, and {attempts_remaining} attempts remaining.")


    def _check_win(self, exact_matches):
        if exact_matches == 4:
            return True
        else:
            return False

    def _check_loss(self):
        if self.player.attempts_used == self.max_attempts:
            return True
        else:
            return False

# responsible for the secret code
class Code:
    def __init__(self):
        self.value = None

    def generate_code(self):
        code_list = []
        while len(code_list) < 4:
            num = random.randint(1, 9)
            code_list.append(str(num))
        code = "".join(code_list)
        self.value = code

    def get_code(self):
        return self.value

# responsible for evaluating the matches in the code
class Evaluator:
    def evaluate(self, secret_code, guess):
        exact_matches = self._count_exact(secret_code, guess)
        total_partials = self._count_partial(secret_code, guess)
        partials = total_partials - exact_matches
        return exact_matches, partials

    def _count_exact(self, secret_code, guess):
        exact_matches = 0
        for index in range(len(secret_code)):
            if secret_code[index] == guess[index]:
                exact_matches += 1
        return exact_matches



    def _count_partial(self, secret_code, guess):
        partial_matches = 0
        for digit in secret_code:
            if digit in guess:
                partial_matches += 1
        return partial_matches

# responsible for making and storing guesses, and tracking attempts
class Player:
    def __init__(self):
        self.guesses = []
        self.attempts_used = 0
        self.guess = None

    def make_guess(self):
        self.guess = input("Make a guess:")
        return self.guess

    def store_guess(self, guess):
        self.guesses.append(guess)
        self.attempts_used += 1

    def get_attempts_used(self):
        return self.attempts_used