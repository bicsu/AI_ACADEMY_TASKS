import util
import wordsegUtil

class JointSegmentationInsertionProblem(util.SearchProblem):
    def __init__(self, query, bigramCost, possibleFills):
        self.query = query
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def start_state(self):
        return 0, wordsegUtil.SENTENCE_BEGIN

    def is_end(self, state):
        return state[0] == len(self.query)

    def succ_and_cost(self, state):
        pos, curr_word = state
        for i in range(pos + 1, len(self.query)+1):
            removed_word = self.query[pos:i]
            fills = self.possibleFills(removed_word)
            for i in fills:
                next_state = i,i
                cost = self.bigramCost(current_word, i)
                yield i, next_state, cost  

unigramCost, bigramCost = wordsegUtil.makeLanguageModels('leo-will.txt')
smoothCost = wordsegUtil.smoothUnigramAndBigram(unigramCost, bigramCost, 0.2)
possibleFills = wordsegUtil.makeInverseRemovalDictionary('leo-will.txt', 'aeiou')
problem = JointSegmentationInsertionProblem('mgnllthppl', smoothCost, possibleFills)

import dynamic_programming_search
dps = dynamic_programming_search.DynamicProgrammingSearch(verbose=1)

import uniform_cost_search
ucs = uniform_cost_search.UniformCostSearch(verbose=0)
print(ucs.solve(problem))