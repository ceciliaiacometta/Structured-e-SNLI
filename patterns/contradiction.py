from .abstract import AbstractPattern
from .entailment import *

class NotRephrasingPattern(RephrasingPattern):
    def __init__(self):
        super().__init__()
        self.patterns = {
            ' '.join(k.split()[0:1] + ['not'] + k.split()[1:]): v
            for k, v in self.patterns.items()
        }
        self.relationship = '≢'

class NotImplicationPattern(ImplicationPattern):
    def __init__(self):
        super().__init__()
        base_implication_patterns = {
            r"imply that": "imply",
            r"imply": "imply",
            r"suggest that": "suggest",
            r"suggest": "suggest",
            r"indicate that": "indicate",
            r"indicate": "indicate",
            r"result in": "result",
            r"entail that": "entail",
            r"entail": "entail",
            r"infer": "infer",
            r"infer as": "infer",
            r"mean": "mean"
        }

        self.relationship = '↛'

        self.patterns = AbstractPattern._generate_negative_patterns(base_implication_patterns)

class NotEquivalencePattern(EquivalencePattern):
    def __init__(self):
        super().__init__()
        self.patterns = {
            ' '.join( ['not'] + k.split()): v
            for k, v in self.patterns.items()
        }

class NotClassificationPattern(ClassificationPattern):
    def __init__(self):
        super().__init__()
        self.patterns = {
            ' '.join(['not'] + k.split()): v
            for k, v in self.patterns.items()
        }
        self.relationship = '⊈'

class XORPattern(AbstractPattern):

    def __init__(self):
        self.patterns = {
            r"or": "or"
        }
        self.relationship = '⊕'

    def _generate_structured_explanation(self, anchor_word: str, doc: Doc, pattern_tokens: Span, highlights: List[str]) -> StructuredExplanation:

        either_token = next((tok for tok in doc if tok.text.lower() == "either"), None)
        or_token = next((tok for tok in doc if tok.text.lower() == "or"), None)

        if not either_token or not or_token:
            return None

        if either_token.i > or_token.i:
            return None

        left_term = [
            tok for tok in doc[either_token.i + 1:or_token.i] if not tok.is_punct
        ]

        right_term = [
            tok for tok in doc[or_token.i + 1:] if not tok.is_punct
        ]

        left_string = " ".join(tok.text for tok in left_term).strip()
        right_string = " ".join(tok.text for tok in right_term).strip()

        left_string, right_string = AbstractPattern._get_grounded_terms(left_string, right_string, highlights)

        if not left_string or not right_string:
            raise ValueError("No grounded terms found")

        return StructuredExplanation(self.relationship, [left_string, right_string])
