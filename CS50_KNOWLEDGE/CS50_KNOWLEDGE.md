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

> * The exclusive Or is often shortened to XOR and a common symbol for it is ⊕).



* **Implication (→)** represents a structure of "if P then Q." P is called the **antecedent** and Q is called the *consequent*.

When the **antecedent** is true, the whole implication is true in the case that the **consequent** is true (that makes sense: if it is raining and I’m indoors, then the sentence “if it is raining, then I’m indoors” is true). When the **antecedent** is true, the implication is false if the **consequent** is false (if I’m outside while it is raining, then the sentence “If it is raining, then I’m indoors” is false). However, when the **antecedent** is false, the implication is always true, regardless of the **consequent**. This can sometimes be a confusing concept. Logically, we can’t learn anything from an implication (P → Q) if the **antecedent** (P) is false. Looking at our example, if it is not raining, the implication doesn’t say anything about whether I’m indoors or not. I could be an indoors type and never walk outside, even when it is not raining, or I could be an outdoors type and be outside all the time when it is not raining. When the antecedent is false, we say that the implication is *trivially* true.

| P     | Q     | P → Q |
| ----- | ----- | ----- |
| false | false | true  |
| false | true  | true  |
| true  | false | false |
| true  | true  | true  |
