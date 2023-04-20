import pygame
import sys
import openai

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flashcard Viewer")

# Set up fonts
font = pygame.font.Font(None, 36)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Flashcards
flashcards = []

current_card = 0
show_answer = False

# Set up OpenAI API
api_key = "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"
openai.api_key = api_key

def generate_flashcard_data(prompt, num_cards=3):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=num_cards,
        stop=None,
        temperature=0.8,
    )

    flashcards = []

    for choice in response.choices:
        text = choice.text.strip()
        lines = text.split("\n")
        question = lines[0].strip()
        answer = lines[1].strip()
        flashcards.append({"question": question, "answer": answer})

    return flashcards

# Generate flashcards
prompt = "Create flashcards with the following topics:\n1. Capital cities\n2. Largest oceans\n3. Famous scientists\n\nFormat: Question and Answer"
flashcards = generate_flashcard_data(prompt)

def draw_flashcard(card, show_answer):
    screen.fill(WHITE)
    question_text = font.render(card["question"], True, BLACK)
    question_rect = question_text.get_rect(center=(screen_width // 2, screen_height // 2 - 100))
    screen.blit(question_text, question_rect)

    if show_answer:
        answer_text = font.render(card["answer"], True, BLACK)
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
        pygame.time.Clock().tick(30)

if __name__ == "__main__":
    run_flashcards()
