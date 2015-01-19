'''
Feature value calculator for a single file/class
'''

__author__ = 'girish'


class FeatureCalculator(object):
    def __init__(self):
        self.featureTokens = {}
        self.featureTokens['acq'] = ['share', 'dlrs', 'numbers', 'stock', 'rights', 'company', 'purchase', 'acquire',
                                     'pct', 'buy', 'moves', 'reorganization', 'cost']
        self.featureTokens['crude'] = ['crude', 'oil', 'barrel', 'price', 'drill', 'seabed', 'shelf']
        self.featureTokens['earn'] = ['board', 'directors', 'stock', 'share', 'capital', 'meeting', 'annual', 'pct',
                                      'dlrs', 'quarterly', 'shareholder', 'profit', 'loss', 'income', 'growth',
                                      'earnings']
        self.featureTokens['grain'] = ['grain', 'car', 'mill', 'production', 'tonnes', 'harvest', 'agriculture',
                                       'storage', 'farm', 'crop', 'grow']
        self.featureTokens['interest'] = ['rate', 'pct', 'bank', 'finance', 'economy', 'government', 'fund', 'borrow',
                                          'invest', 'loan', 'debt', 'finance', 'bond', 'mortgage', 'credit', 'point']
        self.featureTokens['money-fx'] = ['money', 'market', 'bond', 'deposit', 'dollar', 'exchange', 'pct', 'finance',
                                       'forecast', 'bank']
        self.featureTokens['ship'] = ['ship', 'canal', 'transit', 'vessel', 'sea', 'coast', 'harbour', 'port',
                                      'carrier', 'buoy', 'bow']
        self.featureTokens['trade'] = ['price', 'currency', 'trade', 'dlrs']

    def extractWordSet(self, sentences):
        wordSet = set()
        for sentence in sentences:
            for token in sentence.split():
                wordSet.add(token)
        return wordSet

    def calculateFeatureSum(self, featClass, wordSet):
        featEst = 0
        for token in wordSet:
            featEst += self.estimateFeatForClass(token, featClass)
        return featEst

    def estimate(self, sentences, featClass):
        wordSet = self.extractWordSet(sentences)
        return self.calculateFeatureSum(featClass, wordSet)

    def estimateFeatForClass(self, token, featClass):
        for featureToken in self.featureTokens[featClass]:
            if token in featureToken:
                return 1

        return 0