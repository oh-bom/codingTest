# 출처: https://davinci-ai.tistory.com/32 [DAVINCI - AI:티스토리]

genres=["classic", "pop", "classic", "classic", "pop"]
plays=[500, 600, 150, 800, 2500]

def solution(genres, plays):
    song = dict()
    sum_play = dict()
    n = len(genres)
    answer = []

    for i in range(n):
        genre=genres[i]
        num_play=plays[i]
        
        if genre in song:
            # song[genre].append([num_play,i]) #TODO 틀렸던 이유-> num_play는 내림차순, i는 오름차순 하기위해
            # song[genre].sort(reverse=True)
            song[genre].append([-num_play, i])  # 재생 수에 음수를 곱해 내림차순을 고려
            song[genre].sort() #reverse 오름차순 default
        else:
            song[genre]=[[-num_play,i]]
        
        if genre in sum_play:
            sum_play[genre]+=num_play
        else:
            sum_play[genre]=num_play
    
    # song=sorted(song,key=lambda x:song[x],reverse=True)
    sum_play=sorted(sum_play.items(),key=lambda x:x[1],reverse=True)
    
    for genre,_ in sum_play:
        
        song_list=song[genre]
        if len(song_list)==1:song_list=song_list[:1]
        else: song_list=song_list[:2]
        
        for s in song_list:
            answer.append(s[1])
            
    return answer
    

    
solution(genres,plays)