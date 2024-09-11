# -*- coding: utf-8 -*-
"""3A-LEDESMA-MP2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZZmwPs5dZZsYYSeQMZICNt2KKt7Wpz5N

## **Machine Problem: Implementing a Logic-Based Model in Python**

---

**Objective**

- Implement propositional and predicate logic in Python to understand the fundamental
operations of logic-based representation and its application in AI.

1. **Propositional Logic Operations**
"""

def AND(p, q):
    return p and q

def OR(p, q):
    return p or q

def NOT(p):
    return not p

def IMPLIES(p, q):
    return (not p) or q

"""- **Testing Propositional Logic Functions**"""

print(AND(True, False))  # Expected: False
print(OR(True, False))   # Expected: True
print(NOT(True))          # Expected: False
print(IMPLIES(True, False))  # Expected: False

"""2. **Evaluate Logical Statements**"""

def evaluate(statement, values):
    statement = statement.replace('and', ' and ').replace('or', ' or ').replace('not', ' not ').replace('=>', ' or not ')
    for var, val in values.items():
        statement = statement.replace(var, str(val))
    return eval(statement)

"""- **Testing the Evaluation Function**"""

print(evaluate('A and B', {'A': True, 'B': False}))  # Expected: False
print(evaluate('A or B', {'A': True, 'B': False}))   # Expected: True
print(evaluate('not A', {'A': True}))                 # Expected: False
print(evaluate('A => B', {'A': True, 'B': False}))    # Expected: False

"""3. **Extend to Predicate Logic**"""

def forall(predicate, domain):
    return all(predicate(x) for x in domain)

def exists(predicate, domain):
    return any(predicate(x) for x in domain)

"""- **Testing Predicate Logic Functions**"""

predicate = lambda x: x > 0
domain = [1, 2, 3, -1, -2]

print(forall(predicate, domain))  # Expected: False (because not all positive)
print(exists(predicate, domain))  # Expected: True (because is there are positive numbers)

"""4. **AI Agent Development**"""

class SimpleAIAgent:
    def __init__(self):
        self.condition = True  # Example condition

    def make_decision(self):
        if AND(self.condition, True):  # Simple logic
            return 'Take action A'
        else:
            return 'Take action B'

# Create an AI agent instance
agent = SimpleAIAgent()

# Make a decision
print(agent.make_decision())  # Expected: 'Take action A'

"""**PYTHON SCRIPTS: EXPLANATION IN THE FUNCTION**"""

# Implementation of Logic Functions and AI Agent

def and_operation(p, q):
    """Returns the result of the logical conjunction of p and q."""
    return p and q

def or_operation(p, q):
    """Returns the result of the logical disjunction of p and q."""
    return p or q

def not_operation(p):
    """Returns the result of the logical negation of p."""
    return not p

def implies_operation(p, q):
    """Returns the result of the logical implication from p to q."""
    return not p or q

def evaluate(statement, values):
    """
    Evaluates a logical expression based on the provided truth values.

    Args:
    statement (str): A logical expression represented as a string.
    values (dict): A dictionary that maps propositions to their truth values.

    Returns:
    bool: The truth value of the evaluated statement.
    """
    statement = statement.replace('and', ' and ').replace('or', ' or ').replace('not', ' not ').replace('=>', ' or not ')
    for var, val in values.items():
        statement = statement.replace(var, str(val))
    return eval(statement)

def forall(predicate, domain):
    """Checks if a predicate holds true for every element in the domain."""
    return all(predicate(x) for x in domain)

def exists(predicate, domain):
    """Checks if there is at least one element in the domain for which the predicate is true."""
    return any(predicate(x) for x in domain)

class SimpleAIAgent:
    def __init__(self):
        """Initializes the AI agent with a default condition."""
        self.condition = True  # Example condition

    def make_decision(self):
        """Makes a decision based on the current condition."""
        if and_operation(self.condition, True):  # Simple logic
            return 'Take action A'
        else:
            return 'Take action B'

# Example Usage
if __name__ == "__main__":
    # Testing logic functions
    print(and_operation(True, False))  # Expected: False
    print(or_operation(True, False))   # Expected: True
    print(not_operation(True))          # Expected: False
    print(implies_operation(True, False))  # Expected: False

    # Testing evaluation function
    print(evaluate('A and B', {'A': True, 'B': False}))  # Expected: False
    print(evaluate('A or B', {'A': True, 'B': False}))   # Expected: True

    # Testing predicate logic
    predicate = lambda x: x > 0
    domain = [1, 2, 3, -1, -2]
    print(forall(predicate, domain))  # Expected: False
    print(exists(predicate, domain))  # Expected: True

    # AI Agent Decision
    agent = SimpleAIAgent()
    print(agent.make_decision())  # Expected: 'Take action A'