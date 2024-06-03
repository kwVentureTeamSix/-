def solution(genres, plays):
    answer = []
    genre_play_count = {}  # 장르별 총 재생 횟수
    genre_songs = {}  # 장르별 노래 정보 (노래 인덱스와 재생 횟수)

    # 각 장르의 총 재생 횟수와 노래 정보 초기화
    for i in range(len(plays)):
        genre = genres[i]
        play_count = plays[i]

        # 장르별 총 재생 횟수 누적
        genre_play_count[genre] = genre_play_count.get(genre, 0) + play_count

        # 장르별 노래 정보 추가
        if genre not in genre_songs:
            genre_songs[genre] = []
        genre_songs[genre].append((i, play_count))

    # 장르별 총 재생 횟수로 내림차순 정렬
    sorted_genres = sorted(genre_play_count.items(), key=lambda x: x[1], reverse=True)
    
    
    # 정렬된 장르 순서대로 노래 선택
    for genre, _ in sorted_genres:
        # 해당 장르의 노래를 재생 횟수로 내림차순 정렬
        sorted_songs = sorted(genre_songs[genre], key=lambda x: x[1], reverse=True)
        # 상위 2곡의 노래 인덱스를 answer 리스트에 추가
        answer.extend([song[0] for song in sorted_songs[:2]])

    return answer
