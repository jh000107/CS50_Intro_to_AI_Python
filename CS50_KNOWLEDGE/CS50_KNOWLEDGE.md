# Lecture 1

## Knowledge

**Knowledge-Based Agents**

These are agents that reason by operating on internal representations of knowledge.

what does "reasoning based on knowledge to draw a conclusion" mean?

Harry Potter example. Consider the following sentences:

1. If it didn't rain, Harry visited Hagrid today.
2. Harry visited Hagrid or Dumbledore today, but not both.
3. Harry visited Dumbledore today.

Based on these three sentences, using 2 and 3, we know that

4. Harry did not visit Hagrid.

Now looking at sentence 1, we can conclude that

5. It rained today.

To come to this conclusion, we used logic, and today's lecture explores how AI can use logic to reach to new conclusions based on existing information.

**Sentence**

A sentence is an assertion about the world in a knowledge representation language. A sentence is how AI stores knowledge and uses it to infer new information.

## Propositional Logic

Propositional logic is based on propositions, statements about the world that can be either true or false, as in sentences 1-5 above.

**Propositional Symbols**

Propositional symbols are most often letters (P, Q, R) that are used to represent a proposition.

**Logical Connectives**

Logical connectives are logical symbols that connect propositional symbols in order to reason in a more complex way about the world.

- **Not (¬)** inverses the truth value of the proposition. 

| P     | ¬P    |
| ----- | ----- |
| false | true  |
| true  | false |

- **And (∧)** connects two different propositions. When these two proposition, P and Q are connected by ∧, the resulting proposition P ∧ Q is true only in the case that both P and Q are true.

| P     | Q     | P ∧ Q |
| ----- | ----- | ----- |
| false | false | false |
| false | true  | false |
| true  | false | false |
| true  | true  | true  |

- **Or (∨)** is true as as long as either of its arguments is true. This means that for P ∨ Q to be true, at least one of P or Q has to be true.

| P     | Q     | P ∨ Q |
| ----- | ----- | ----- |
| false | false | false |
| false | true  | true  |
| true  | false | true  |
| true  | true  | true  |

There are two types of Or: an inclusive Or and an exclusive Or. An exclusive Or requires only one of its arguments to be true and not both. In the case of Or (∨), the intention is an inclusive Or.

