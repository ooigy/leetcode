# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

# Note:

# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# One must use all the tickets once and only once.
# Example 1:

# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
# Example 2:

# Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
#              But it is larger in lexical order.

class Solution:
    def findItinerary(self, tickets: List[List[str]], path=["JFK"]) -> List[str]:
        # the idea should be to:
        # 1. sort the tickets into lex order
        # 2. Start with jfk, loop thru anything from jfk -> X
        # 2b. Will only move to another destination if first one hits a dead end

        if not tickets: return path
        tickets.sort(key=lambda x: x[1])
        for dest in [p for p in tickets if p[0] == path[-1]]:
            new_tickets = tickets.copy()
            new_tickets.remove(dest)
            res = self.findItinerary(new_tickets, path+[dest[1]])
            if res:
                return res