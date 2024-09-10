import numpy as np 
from sklearn.linear_model import LinearRegression
from sklearn.exceptions import NotFittedError

ACTIONS = ['UP', 'RIGHT', 'DOWN', 'LEFT', 'WAIT', 'BOMB']

class ols_model():
    def __init__(self) -> None:
        self.reward_predictior = []
        for a in ACTIONS:
            self.reward_predictior.append(LinearRegression())
        
        #self.gamestate_predictor = LinearRegression()
        self.old_state = np.empty(shape=(0,289))
        self.action = np.empty(shape=(0,1))
        self.reward = np.empty(shape=(0,1))
        #self.new_gamestate = np.empty(shape=(0,289))
        self.trained = False

    def choose_action(self, feature_array):
        if not self.trained:
            return np.random.choice(ACTIONS, p=[.2, .2, .2, .2, .1, .1])
        prediced_reward = np.zeros(shape=(6,))
        for i,predictor in enumerate(self.reward_predictior):
            try:
                prediced_reward[i] = predictor.predict(feature_array.reshape(1,-1))
            except(NotFittedError):
                pass
        return ACTIONS[np.argmax(prediced_reward)]
    
    def add_to_TS(self, new_transition):
        if new_transition is not None:
            self.old_state = np.row_stack((self.old_state, new_transition[0]))
            self.action = np.row_stack((self.action, new_transition[1]))
            self.reward= np.row_stack((self.reward, new_transition[3]))
            #self.new_gamestate = np.row_stack((self.new_gamestate, new_transition[2]))

    def train(self):
        for i,a in enumerate(ACTIONS):
            acces_list = (self.action == a ).reshape(-1)
            if np.count_nonzero(acces_list) > 0:
                ass_states = self.old_state[acces_list,:]
                ass_rewards = self.reward[acces_list,:]
                self.reward_predictior[i].fit(ass_states, ass_rewards)
        self.trained = True
