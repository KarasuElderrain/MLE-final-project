# Main Tasks
1. On a game board without any crates or opponents, collect a number of revealed coins as quickly as possible. This task does not require dropping any bombs. The agent should learn how to navigate the board efficiently.
    1.1 Set rewards for subtasks
    1.2 Set up board symetrys to reduce game state size
2. On a game board with randomly placed crates yet without opponents, find all hidden coins and collect them within the step limit. The agent must drop bombs to destroy the crates. It should learn how to use bombs without killing itself, while not forgetting efficient navigation.  Escaping bombs is a crucial capability for good tournament performance, so place proper emphasis on this step.
3. On a game board with crates, try to hunt and blow up our predefined peaceful_agent (easy) and the coin_collector_agent (hard). The former agent does not drop bombs and moves randomly. The latter agent will drop bombs only for the purpose of collecting coins.
4. On a game board with crates, hold your own against one or more opposing agents (e.g. the fullstrength rule_based_agent, differents variants of your own design) and fight for the highest score. Experience shows that you must be able to beat the rule_based_agent in order to have any chance of winning the tournament.
 
