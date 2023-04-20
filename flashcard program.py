import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flashcard Viewer")

# Set up fonts
font = pygame.font.Font(None, 36)

def create_flashcards():
    num_flashcards = int(input("Enter the number of flashcards: "))
    flashcards = []

    for i in range(num_flashcards):
        print(f"Flashcard {i + 1}:")
        question = input("  Enter the question: ")
        answer = input("  Enter the answer: ")
        flashcards.append({"question": question, "answer": answer})

    return flashcards

# Flashcards
flashcards = create_flashcards()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flashcard Viewer")

# Set up fonts
font = pygame.font.Font(None, 36)

# Flashcards
flashcards = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the largest ocean?", "answer": "Pacific Ocean"},
    {"question": "Who developed the theory of relativity?", "answer": "Albert Einstein"},
]

current_card = 0
show_answer = False

def draw_flashcard(card, show_answer):
    screen.fill((255, 255, 255))
    question_text = font.render(card["question"], True, (0, 0, 0))
    question_rect = question_text.get_rect(center=(screen_width // 2, screen_height // 2 - 100))
    screen.blit(question_text, question_rect)

    if show_answer:
        answer_text = font.render(card["answer"], True, (0, 0, 0))
        answer_rect = answer_text.get_rect(center=(screen_width // 2, screen_height // 2 + 100))
        screen.blit(answer_text, answer_rect)

def run_flashcards():
    global current_card, show_answer

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    current_card = (current_card + 1) % len(flashcards)
                    show_answer = False
                elif event.key == pygame.K_LEFT:
                    current_card = (current_card - 1) % len(flashcards)
                    show_answer = False
                elif event.key == pygame.K_SPACE:
                    show_answer = not show_answer

        draw_flashcard(flashcards[current_card], show_answer)
        pygame.display.flip()

if __name__ == "__main__":
    run_flashcards()
