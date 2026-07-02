# HashMap + Heap + Follow Graph.
import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId):
        heap = []
        users = self.following[userId] | {userId}
        for uid in users:
            for t, tid in self.tweets[uid][-10:]:
                heapq.heappush(heap, (t, tid))
                if len(heap) > 10:
                    heapq.heappop(heap)

        return [tid for _, tid in sorted(heap, reverse=True)]

    def follow(self, followerId, followeeId):
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.following[followerId].discard(followeeId)
