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

* **Biconditional (↔)** is an implication that goes both directions. You can read it as "if and only if."  P ↔ Q is the same as P → Q and Q → P taken together. This means that we can infer more than we could with a simple implication. If P is false, then Q is also false.

| P     | Q     | P ↔ Q |
| ----- | ----- | ----- |
| false | false | true  |
| false | true  | false |
| true  | false | false |
| true  | true  | true  |

**Model**

The model is an assignment of a truth value to every proposition. To reiterate, propositions are statements about the world that can be either true or false. However, knowledge about the world is represented in the truth values of these propositions. The model is the truth-value assignment that provides information about the world.

**Knowledge Base (KB)**

the knowledge base is a set of sentences known by a knowledge-based agent. This is knowledge that the AI is provided about the world in the form of propositional logic sentences that can be used to make additional inferences about the world.

**Entailment (⊨)**

If α ⊨ β (α entails β), then in any world where α is true, β is true, too.



## Inference

Inference is the process of deriving new sentences from old ones.

For instance, in the Harry Potter example earlier, sentences 4 and 5 were inferred from sentences 1, 2, and 3.

There are multiple ways to infer new knowledge based on existing knowledge. First, we will consider the **Model Checking** algorithm.

* To determine if KB ⊨ α (in other words, answering the question: “can we conclude that α is true based on our knowledge base”)
  * Enumerate all possible models.
  * If in every model where KB is true, α is true as well, then KB entails α (KB ⊨ α).

Consider the following example:

P: It is a Tuesday. Q: It is raining. R: Harry will go for a run. KB: (P ∧ ¬Q) → R (in words, P and not Q imply R) P (P is true) ¬Q (Q is false) Query: R (We want to know whether R is true or false; Does KB ⊨ R?)

To answer the query using the Model Checking algorithm, we enumerate all possible models.

| P     | Q     | R     | KB   |
| ----- | ----- | ----- | ---- |
| false | false | false |      |
| false | false | true  |      |
| false | true  | false |      |
| false | true  | true  |      |
| true  | false | false |      |
| true  | false | true  |      |
| true  | true  | false |      |
| true  | true  | true  |      |

Then, we go through every model and check whether it is true given our Knowledge Base.

First, in our KB, we know that P is true. Thus, we can say that the KB is false in all models where P is not true.

| P     | Q     | R     | KB    |
| ----- | ----- | ----- | ----- |
| false | false | false | false |
| false | false | true  | false |
| false | true  | false | false |
| false | true  | true  | false |
| true  | false | false |       |
| true  | false | true  |       |
| true  | true  | false |       |
| true  | true  | true  |       |

Next, similarly, in our KB, we know that Q is false. Thus, we can say that the KB is false in all models where Q is true.

| P     | Q     | R     | KB    |
| ----- | ----- | ----- | ----- |
| false | false | false | false |
| false | false | true  | false |
| false | true  | false | false |
| false | true  | true  | false |
| true  | false | false |       |
| true  | false | true  |       |
| true  | true  | false | false |
| true  | true  | true  | false |

Finally, we are left with two models. In both, P is true and Q is false. In one model R is true and in the other R is false. Due to (P ∧ ¬Q) → R being in our KB, we know that in the case where P is true and Q is false, R must be true. Thus, we say that our KB is false for the model where R is false, and true for the model where R is true.

| P     | Q     | R     | KB    |
| ----- | ----- | ----- | ----- |
| false | false | false | false |
| false | false | true  | false |
| false | true  | false | false |
| false | true  | true  | false |
| true  | false | false | false |
| true  | false | true  | true  |
| true  | true  | false | false |
| true  | true  | true  | false |
