from collections import Counter

def hashtag_analisys():
    def create_hashtag_list():
        hash_list = []

        for post in posts:
            for word in post.split():
                if word.startswith("#"):
                    hash_list.append(word)
        return hash_list

    def show_trending(trending):
        result = "Hashtags trending (más de una aparición):"
        for hashtag,times in trending:
            result += f"\n\t{hashtag}: {times}"

        print(result)

    posts = [
        "Arrancando el lunes con energía #Motivación #NuevaSemana",
        "Terminé mi primer proyecto en Python #Python #Programación #OrgullosoDeMi",
        "No puedo creer el final de la serie #SinSpoilers #SerieAdicta",
        "Nuevo video en el canal sobre #InteligenciaArtificial y #Python",
        "Entrenamiento de hoy completado #Fitness #Motivación #NoPainNoGain",
        "Leyendo sobre #InteligenciaArtificial y el futuro del trabajo #Tecnología",
        "Arranqué a estudiar #Programación por mi cuenta #Python #Autodidacta",
        "Finde de lluvia, maratón de series #SerieAdicta #Relax",
        "Workshop de #InteligenciaArtificial en la universidad #Tecnología #Programación"
    ]
    
    hashtag_list = create_hashtag_list()

    total_appearence = Counter(hashtag_list).most_common()

    total_hashtag = len(total_appearence)

    trending = [item for item in total_appearence if item[1] >= 2]

    show_trending(trending)
    print(f"Total de hashtags unicos: {total_hashtag}")

if __name__ == "__main__":
    hashtag_analisys()