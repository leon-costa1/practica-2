def playlist_duration():
    playlist = [
        {"title": "Bohemian Rhapsody", "duration": "5:55"},
        {"title": "Hotel California", "duration": "6:30"},
        {"title": "Stairway to Heaven", "duration": "8:02"},
        {"title": "Imagine", "duration": "3:07"},
        {"title": "Smells Like Teen Spirit", "duration": "5:01"},
        {"title": "Billie Jean", "duration": "4:54"},
        {"title": "Hey Jude", "duration": "7:11"},
        {"title": "Like a Rolling Stone", "duration": "6:13"},
    ]
    
    suma_mins = 0
    suma_segs = 0
    duration_list = []
    
    for i in playlist:
        # Lista con [minutos, segundos]
        duration = i["duration"].split(":")
    
        minutes = int(duration[0])
        segs = int(duration[1])
    
        suma_mins += minutes
        suma_segs += segs
    
        # Lista con las duraciones
        duration_list.append((minutes*60)+segs)
    
    # calculo la cantidad de minutos que hay en los segundos y lo que sobra
    min_of_seg, suma_segs = divmod(suma_segs, 60)
    suma_mins += min_of_seg
    
    # Calculo la posicion del minimo y del maximo
    index_min = duration_list.index(min(duration_list))
    index_max = duration_list.index(max(duration_list))
    
    # Obtengo los valores minimo y maximo
    shortest = playlist[index_min]
    longest = playlist[index_max]
    
    print(f"Duracion total: {suma_mins}m {suma_segs}s")
    print(f"Cancion mas larga: \"{longest["title"]}\" ({longest["duration"]})")
    print(f"Cancion mas corta: \"{shortest["title"]}\" ({shortest["duration"]})")