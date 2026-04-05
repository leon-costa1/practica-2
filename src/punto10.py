def kitchen_tournament():
    rounds = [
        {
            'theme': 'Entrada',
            'scores': {
                'Valentina': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
                'Mateo': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
                'Camila': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
                'Santiago': {'judge_1': 6, 'judge_2': 7, 'judge_3': 6},
                'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 8},
            }
        },

        {
            'theme': 'Plato principal',
            'scores': {
                'Valentina': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
                'Mateo': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
                'Camila': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
                'Santiago': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
                'Lucía': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
            }
        },

        {
            'theme': 'Postre',
            'scores': {
                'Valentina': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
                'Mateo': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
                'Camila': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
                'Santiago': {'judge_1': 7, 'judge_2': 7, 'judge_3': 6},
                'Lucía': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
            }
        },

        {
            'theme': 'Cocina internacional',
            'scores': {
                'Valentina': {'judge_1': 8, 'judge_2': 9, 'judge_3': 9},
                'Mateo': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
                'Camila': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
                'Santiago': {'judge_1': 8, 'judge_2': 9, 'judge_3': 7},
                'Lucía': {'judge_1': 7, 'judge_2': 7, 'judge_3': 8},
            }
        },

        {
            'theme': 'Final libre',
            'scores': {
                'Valentina': {'judge_1': 9, 'judge_2': 8, 'judge_3': 9},
                'Mateo': {'judge_1': 8, 'judge_2': 9, 'judge_3': 8},
                'Camila': {'judge_1': 7, 'judge_2': 7, 'judge_3': 7},
                'Santiago': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
                'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 7},
            }
        }
    ]

    def show_table(stats, final=""):
        stats_descendent = sorted(stats.items(),key= lambda score: score[1]["puntaje"], reverse=True)
        players = []
        scores = []
        for player in stats_descendent:
            players.append(player[0])
            scores.append(player[1])

        print(f"Tabla de posiciones {final}:")
        print(f"Cocinero\t{players[0]:^10}{players[1]:^10}{players[2]:^10}{players[3]:^10}{players[4]:^10}")
        print("-"*70)
        print(f"Puntaje \t{scores[0]["puntaje"]:^10}{scores[1]["puntaje"]:^10}{scores[2]["puntaje"]:^10}{scores[3]["puntaje"]:^10}{scores[4]["puntaje"]:^10}")
        print(f"Rondas ganadas \t{scores[0]["rondas ganadas"]:^10}{scores[1]["rondas ganadas"]:^10}{scores[2]["rondas ganadas"]:^10}{scores[3]["rondas ganadas"]:^10}{scores[4]["rondas ganadas"]:^10}")
        print(f"Mejor ronda \t{scores[0]["mejor ronda"]:^10}{scores[1]["mejor ronda"]:^10}{scores[2]["mejor ronda"]:^10}{scores[3]["mejor ronda"]:^10}{scores[4]["mejor ronda"]:^10}")
        print(f"Promedio \t{scores[0]["promedio"][0]:^10}{scores[1]["promedio"][0]:^10}{scores[2]["promedio"][0]:^10}{scores[3]["promedio"][0]:^10}{scores[4]["promedio"][0]:^10}")
        print("-"*70)

    def show_round(stats, number, theme, winner_name, winner_points):
        print(f"Ronda {number} - {theme}:")
        print(f"Ganador: {winner_name} ({winner_points} pts)")
        show_table(stats)
        print()

    def round_scores(scores):
        final_score = []
        for player,score in scores.items():
            player_points = [player, sum(score.values())]
            final_score.append(player_points)
        return final_score

    def calculate_winner(scores_list):
        points_list = [scores[1] for scores in scores_list]

        winner_points = max(points_list)
        winner_pos = points_list.index(winner_points)
        winner_name = scores_list[winner_pos][0]

        return winner_name, winner_points, winner_pos

    def upgrade_stats(stats,current_round, winner_pos):
        for index, dict_scores in enumerate(stats.values()):
            current_score = current_round[index][1]

            # actualiza el puntaje total
            dict_scores["puntaje"] += current_score

            # actualize si gana la ronda
            if index == winner_pos:
                dict_scores["rondas ganadas"] += 1

            # actualiza si obtuvo su mejor ronda
            if current_score > dict_scores["mejor ronda"]:
                dict_scores["mejor ronda"] = current_score

            # actualiza el promedio
            dict_scores["promedio"][1] += 1
            dict_scores["promedio"][0] = round(dict_scores["puntaje"] / dict_scores["promedio"][1],2)

    stats = {
        'Valentina': {
            "puntaje": 0,
            "rondas ganadas": 0,
            "mejor ronda": 0, 
            "promedio": [0,0],
        },
        'Mateo': {
            "puntaje": 0,
            "rondas ganadas": 0,
            "mejor ronda": 0, 
            "promedio": [0,0],
        },
        'Camila': {
            "puntaje": 0,
            "rondas ganadas": 0,
            "mejor ronda": 0, 
            "promedio": [0,0],
        },
        'Santiago': {
            "puntaje": 0,
            "rondas ganadas": 0,
            "mejor ronda": 0, 
            "promedio": [0,0],
        },
        'Lucía': {
            "puntaje": 0,
            "rondas ganadas": 0,
            "mejor ronda": 0, 
            "promedio": [0,0],
        },
    }

    for turn in enumerate(rounds,1):
        turn_scores = round_scores(turn[1]["scores"])
        winner_name, winner_points, winner_pos = calculate_winner(turn_scores)
        upgrade_stats(stats, turn_scores, winner_pos)
        show_round(stats, turn[0], turn[1]["theme"], winner_name, winner_points)

    show_table(stats, "final")

if __name__ == "__main__":
    kitchen_tournament()