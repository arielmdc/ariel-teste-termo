class TermoGame:
    def __init__(self, solution):
        self.solution = solution.lower()
        self.attempts = 0
        self.max_attempts = 6

    def check_word(self, attempt):
        attempt = attempt.lower()
        if len(attempt) != len(self.solution):
            raise ValueError("Attempt length does not match solution length")

        feedback = ['black'] * len(self.solution)
        solution_chars = list(self.solution)
        attempt_chars = list(attempt)

        # Primeiro, marcar todos os 'green'
        for i in range(len(attempt)):
            if attempt[i] == self.solution[i]:
                feedback[i] = 'green'
                solution_chars[i] = None
                attempt_chars[i] = None

        # Em seguida, marcar os 'yellow'
        for i in range(len(attempt)):
            if attempt_chars[i] is not None and attempt_chars[i] in solution_chars:
                feedback[i] = 'yellow'
                solution_chars[solution_chars.index(attempt_chars[i])] = None

        self.attempts += 1
        return feedback

    def is_solved(self, feedback):
        return all(color == 'green' for color in feedback)

    def can_attempt(self):
        return self.attempts < self.max_attempts
