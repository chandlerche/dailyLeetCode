class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        inLevelFriends = set()
        inLevelFriends.add(id)
        newLevelFriends = friends[id]
        for i in range(2, level + 1):
            for y in newLevelFriends: 
                inLevelFriends.add(y)
            temp = set() 
            for x in newLevelFriends: 
                for y in friends[x]: 

                    if(y not in inLevelFriends):
                        temp.add(y) 

            newLevelFriends = list(temp)
        hashMap ={}
        for x in newLevelFriends:
            for y in watchedVideos[x]:
                if(y not in hashMap):
                    hashMap[y] = 1
                else:
                    hashMap[y] = hashMap[y] + 1
        videos = list(hashMap.items())
        videos.sort(key = lambda x: (x[1], x[0]))
        return [video[0] for video in videos]