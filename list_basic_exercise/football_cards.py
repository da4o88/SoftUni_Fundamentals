cards = input()
team_A = []
team_B = []
game = True

for i in range(1, 11 + 1):
    team_A.append(i)
    team_B.append(i)

players_A = len(team_A)
players_B = len(team_B)
# Red Cards
red_cards = cards.split(' ')
# Players which have red card
team_A_red_cards_players = []
team_B_red_cards_players = []

for i in range(len(red_cards)):
    check_card = red_cards[i]
    # Split card in additional array with sign '-'
    team_red_cards = check_card.split('-')
    # Team check does have more than 7 players, index[0] is the team 'A' or 'B', index[1] is player number
    if players_A >= 7 and players_B >= 7:
        if team_red_cards[0] == 'A':
            if team_red_cards[1] in team_A_red_cards_players:
                continue
            else:
                players_A -= 1
                team_A_red_cards_players.append(team_red_cards[1])
        elif team_red_cards[0] == 'B':
            if team_red_cards[1] in team_B_red_cards_players:
                continue
            else:
                players_B -= 1
                team_B_red_cards_players.append(team_red_cards[1])
    else:
        game = False
        break

if game:
    print(f"Team A - {players_A}; Team B - {players_B}")
else:
    print(f"Team A - {players_A}; Team B - {players_B}")
    print("Game was terminated")
