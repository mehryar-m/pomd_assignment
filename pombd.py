## pomd.py

from probability import *

## actions for & evidence from assignment
a1  =  ['up','up','up']
a2  =  ['up','up', 'up']
a3  =  ['right','right', 'up']
a4  =  ['up', 'right', 'right', 'right']

e1 = [2,2,2]
e2 = [1,1,1]
e3 = [1,1,'end']
e4 = [2,2,1,1]

# returns the probability ot being in current state, based on previous state and action
def get_probability(current_state,prev_state,action):
    return p_table[current_state][prev_state][action]

# returns the probability of the observation given state
def get_observation_prob(current_state, obs):
    return evidence[current_state][obs]

# normalize the probabilities
# ensures the probabilities sum to 1
def normalize(probabilities, total_sum):
    for key in probabilities:
        probabilities[key] = probabilities[key] / total_sum
    return probabilities

# returns the sum of the conditional probabilities. 
def getprob_sum(k, action, belief):
    probs = p_table[k]
    prob_sum = 0
    for key in probs: 
        prob_sum = prob_sum + get_probability(k,key,action)*belief[key]
    return prob_sum

def solve_pomd(belief, actions, observations):
    # put actions and observations in one nested array
    action_obs = [actions,observations]
    new_belief = belief # previous state
    final_belief = belief # state that will be manipulated
    for i in range(0,len(actions)):
        for key in new_belief:
            final_belief[key] = getprob_sum(key,action_obs[0][i],new_belief)*get_observation_prob(key,action_obs[1][i]) ## computes new belief
        total_sum = sum(final_belief.values())
        final_belief = normalize(final_belief,total_sum) # normalize the beliefs
        new_belief = final_belief # update our state to the new belief state we just calculated
    return final_belief

# compute the iterations =====================
# almost pretty print for the assignment 
def pretty_print(belief):
    for key, value in sorted(belief.iteritems()):
        print(key, value)

def main(): 
    iter_1 = solve_pomd(default_belief_state,a1,e1)
    iter_2 = solve_pomd(default_belief_state,a2,e2)
    iter_3 = solve_pomd(s0_1_belief_state,a3,e3)
    iter_4 = solve_pomd(s0_2_belief_state,a4,e4)
    print('============ Iteration 1')
    pretty_print(iter_1)
    print('============ Iteration 2')
    pretty_print(iter_2)
    print('============ Iteration 3')
    pretty_print(iter_3)
    print('============ Iteration 4')
    pretty_print(iter_4)

# run this whole beast    
main()

