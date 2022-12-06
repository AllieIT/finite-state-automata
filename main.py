from automatons.df_automaton import DFA
from automatons.nf_automaton import NFA

dfa = DFA(set(), ["0", "1"])

dfa.add_state("q_000", ["q_000", "q_001"], is_starting=True)
dfa.add_state("q_001", ["q_010", "q_011"])
dfa.add_state("q_010", ["q_100", "q_101"])
dfa.add_state("q_011", ["q_110", "q_111"])
dfa.add_state("q_100", ["q_000", "q_001"], is_accepting=True)
dfa.add_state("q_101", ["q_010", "q_011"], is_accepting=True)
dfa.add_state("q_110", ["q_100", "q_101"], is_accepting=True)
dfa.add_state("q_111", ["q_110", "q_111"], is_accepting=True)

# print(dfa.get_resulting_state("110111"))
# print(dfa.accepts_word("11011011"))
# print(dfa.get_all_accepted_words(5))

print("NFA -------------------------------------------------")
nfa = NFA(set(), ["0", "1"])

a = nfa.add_state("q_0", [{"q_0"}, {"q_0", "q_1"}], is_starting=True)
nfa.add_state("q_1", [{"q_2"}, {"q_2"}])
nfa.add_state("q_2", [{"q_3"}, {"q_3"}])
nfa.add_state("q_3", [set(), set()], is_accepting=True)
nfa.print()

print(nfa.get_all_accepted_words(5))

dfa = nfa.convert_to_dfa(map_states=False)
dfa.print()

dfa = DFA(set(), ["0", "1"])
dfa.add_state("q_0", ["q_0", "q_1"], is_starting=True)
dfa.add_state("q_1", ["q_1", "q_0"], is_accepting=True)
dfa.print()
