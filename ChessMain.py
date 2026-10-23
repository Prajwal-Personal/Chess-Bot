import pygame
import ChessEngine

pygame.init()

width = 400
height = 400
squareSize = 400 // 8
maxFPS = 15

# loading all the images
pieceImages = dict()
pieces = ["bp","wp","bR","wR","bN","wN","bB","wB","bQ","wQ","bQ","wK","bK"]
for x in pieces:
    pieceImages[x] = pygame.transform.scale(
        pygame.image.load("images/" + x + ".png"),
        (squareSize, squareSize)
    )

def main():
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))
    gameState = ChessEngine.GameState()
    running = True

    while(running):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                running = False

        pygame.display.flip()

        drawGameState(screen, gameState)
        clock.tick(maxFPS)

# Handles all the graphical interface
def drawGameState(screen, gameState):
    drawBoard(screen)
    drawPieces(screen, gameState.board)

# Draws the squares in board
def drawBoard(screen):
    light = pygame.Color(200,200,200)
    dark = pygame.Color(50,50,50)
    for row in range(8):
        for col in range(8):
            color = light if ((row+col)&1)==0 else dark
            pygame.draw.rect(screen, color, pygame.Rect(
                col * squareSize,
                row * squareSize,
                squareSize,
                squareSize
            ))

# Handles drawing the pieces on the board
def drawPieces(screen, board):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if(piece == "--"):
                continue
            else:
                screen.blit(pieceImages[piece], pygame.Rect(
                    col * squareSize,
                    row * squareSize,
                    squareSize,
                    squareSize
                ))

if __name__=="__main__":
    main()