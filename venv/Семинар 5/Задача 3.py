
# Создайте программу для игры в ""Крестики-нолики"".

game_matrix = [[None, None, None], [None, None, None], [None, None, None]]
game_is_on = True
while game_is_on:
    # Крестик - латинская буква X, нолик - латинская буква O
    # Ходы принимаются в формате [0][0] = "X" или [2][1] = "О"
    row = str(input("Введите номер строки: "))
    column = str(input("Введите номер столбца: "))
    character = str(input("Введите 0 или Х: "))

    exec(f"game_matrix[{row}][{column}] = \'{character} \'")
    for i in game_matrix:
        print(i)

    reference_matrix = [
        game_matrix[0],
        game_matrix[1],
        game_matrix[2],
        [i[0] for i in game_matrix],
        [i[1] for i in game_matrix],
        [i[2] for i in game_matrix],
        [game_matrix[0][0], game_matrix[1][1], game_matrix[2][2]],
        [game_matrix[0][2], game_matrix[1][1], game_matrix[2][0]]
    ]
    for item in reference_matrix:
        result = list(set(item))
        if len(result) == 1 and result[0] != None:
            print("Game over!")
            game_is_on = False
            break