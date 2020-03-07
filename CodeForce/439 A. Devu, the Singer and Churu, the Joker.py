def devu_singer_charu_joker():
    songs, duration = [int(x) for x in input().split(' ')]
    song_durations = [int(x) + 10 for x in input().split(' ')]
    song_durations[-1] = song_durations[-1] - 10

    no_ok_jokes_on_break = (songs - 1) * 2

    sum_of_song_duration = sum(song_durations)
    if sum_of_song_duration > duration:
        return -1
    else:
        return no_ok_jokes_on_break + ((duration - sum_of_song_duration) // 5)


if __name__ == '__main__':
    while True:
        print(devu_singer_charu_joker())
