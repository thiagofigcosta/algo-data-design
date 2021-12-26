import unittest

import algo_data_design.problems
import algo_data_design.utils.input as u_input

test = unittest.TestCase()


def info():
    print("Coin change")
    print("For a given list of coins and a target amount, compute the minimum amount of coins that need to be summed")
    print("in order to achieve the target amount. It is assumable that amount of coins of each kind are infinite.")
    print("If its not possible to solve, return -1")
    print("Examples:")
    print('\t[1,2,5], 11 -> 3')
    print('\t[2], 3 -> -1')
    print('\t[1], 0 -> 0')


def run_greedy(coins, amount):
    # Time complexity: O(n*log(n)), where n is the amount of coins
    # Space complexity: O(1)
    # This approach does not give the correct solution
    amount_of_coins = 0
    coins.sort(reverse=True)
    for coin in coins:
        if coin <= amount:
            while coin <= amount and amount > 0:  # use the biggest coin until can't do it anymore
                amount_of_coins += 1
                amount -= coin
            if amount <= 0:
                break
    if amount == 0:
        return amount_of_coins
    else:
        return -1


def run_backtracking(coins, amount):
    # Time complexity: O(2^n), where n is the amount of coins
    # Space complexity: O(2^n) ???
    # This approach tries every solution repeating computation, it is slow
    # Top down, the choice binary tree grows from the expected solution to every possible scenario,
    # solves the problem in natural order
    if amount == 0:
        return 0

    def __count_coins_recursively(_coins, _amount, coin_index):
        # we have a binary tree with all possible choices, the branches represents the inclusion of the current coin on
        # the solution or its absence on it. When removing a coin from the solution we move on to the next coin
        if _amount == 0:  # the coins combination matched the amount
            return 0  # there is a solution
        if coin_index >= len(_coins):  # could not combine coins, so there is no solution
            return float('inf')
        if _coins[coin_index] <= _amount:
            # add 1 to the amount of coins and subtract the coin value from the target amount
            include_branch = 1 + __count_coins_recursively(_coins, _amount - _coins[coin_index], coin_index)
        else:
            # if the coin is bigger than amount, there is no solution
            include_branch = float('inf')  # the is no way to use a bigger coin, move to the exclusive branch
        # keep the target amount and move on to the next coin
        exclude_branch = __count_coins_recursively(_coins, _amount, coin_index + 1)
        return min(include_branch, exclude_branch)  # get the best outcome

    amount_of_coins = __count_coins_recursively(coins, amount, 0)
    if amount_of_coins == float('inf'):
        amount_of_coins = -1
    return amount_of_coins


def run_dp_top_down(coins, amount):
    # Time complexity: O(n*m), where n is the amount of coins
    # Space complexity: O(n*m)
    # This approach tries every solution, but only start another recursive branch if the result isn't known yet
    # Top down, the choice binary tree grows from the expected solution to every possible scenario,
    # solves the problem in natural order
    if amount == 0:
        return 0

    def __count_coins_recursively(_coins, _amount, coin_index, _cache):
        # we have a binary tree with all possible choices, the branches represents the inclusion of the current coin on
        # the solution or its absence on it. When removing a coin from the solution we move on to the next coin
        if _amount == 0:  # the coins combination matched the amount
            return 0
        if coin_index >= len(_coins):  # could not combine coins, so there is no solution
            return float('inf')
        if _coins[coin_index] <= _amount:
            # subtract the coin value from the target amount
            new_amount = _amount - _coins[coin_index]
            if (new_amount, coin_index) in cache:  # if the result is already known just use it
                result = cache[(new_amount, coin_index)]
            else:  # otherwise ask for its computation
                result = __count_coins_recursively(_coins, new_amount, coin_index, _cache)
            include_branch = 1 + result  # add 1 to the amount of coins
        else:
            include_branch = float('inf')  # the is no way to use a bigger coin, move to the exclusive branch
        # keep the target amount and move on to the next coin
        new_coin_index = coin_index + 1
        if (_amount, new_coin_index) in cache:  # if the result is already known just use it
            result = cache[(_amount, new_coin_index)]
        else:  # otherwise ask for its computation
            result = __count_coins_recursively(_coins, _amount, new_coin_index, _cache)
        exclude_branch = result
        result = min(include_branch, exclude_branch)
        cache[(_amount, coin_index)] = result  # store the result on the cache
        return result

    cache = {}
    amount_of_coins = __count_coins_recursively(coins, amount, 0, cache)
    if amount_of_coins == float('inf'):
        amount_of_coins = -1
    return amount_of_coins


def run_dp_bottom_up(coins, amount):
    # Time complexity: O(n*m), where n is the amount of coins and m is the amount sum
    # Space complexity: O(n*m)
    # Bottom up, solves simple problems first and then go the complex one, navigate the tree of choices from
    # the simplest case till the complex one, storing the known solutions to avoid recomputing
    uninitialized = None
    if amount == 0:
        return 0

    # This dynamic programming matrix stores the solution on its cells, the rows represents how many kinds coins are
    #  being used in the solution while the columns store all kinds of sums
    dp_cache = []
    for i in range(len(coins) + 1):  # plus one to store the base case
        row = [uninitialized for _ in range(amount + 1)]  # plus one to store the base case
        dp_cache.append(row)
    for j in range(1, amount + 1, 1):  # initialize with base case, if there is no coin, there is no solution
        dp_cache[0][j] = float('inf')

    for i in range(len(coins) + 1):  # initialize with base case, if there the amount is zero, the solution is 0
        dp_cache[i][0] = 0

    for cur_amount in range(1, amount + 1, 1):  # solving from the simplest case till the original problem
        for i in range(1, len(coins) + 1):  # from using only the first coin to all of them
            coin = coins[i - 1]
            exclude_branch = dp_cache[i - 1][cur_amount]
            if coin <= cur_amount:
                # if the current coin is smaller than the current amount, check if it is "cheaper" to use this coin
                # to ignore it and use the the minimum calculated for this amount using fewer kinds of coins
                include_branch = 1 + dp_cache[i][cur_amount - coin]
                dp_cache[i][cur_amount] = min(include_branch, exclude_branch)
            else:
                # if the current coin is bigger than current amount,
                # just pick the minimum calculated for this amount using fewer kinds of coins
                dp_cache[i][cur_amount] = exclude_branch
    amount_of_coins = dp_cache[len(coins)][amount]  # the solution is sitting on lower right corner
    if amount_of_coins == float('inf'):
        amount_of_coins = -1
    return amount_of_coins


def main():
    if algo_data_design.problems.NO_PROMPT:
        solution = 1
    else:
        print('Choose a solution to run:')
        print('\t1 - Dynamic Programming - Bottom up')
        print('\t2 - Dynamic Programming - Top down')
        print('\t3 - Recursive - Top down (Slow)')
        print('\t4 - Greedy (Some wrong results)')
        solution = u_input.input_number(greater_or_eq=1, lower_or_eq=4)
    if solution == 1:
        run = run_dp_bottom_up
    elif solution == 2:
        run = run_dp_top_down
    elif solution == 3:
        run = run_backtracking
    elif solution == 4:
        run = run_greedy
    else:
        raise Exception('Unknown solution')
    info()
    test.assertEqual(3, run([1, 2, 5], 11))
    test.assertEqual(-1, run([2], 3))
    test.assertEqual(0, run([1], 0))
    test.assertEqual(1, run([1], 1))
    test.assertEqual(20, run([186, 419, 83, 408], 6249))
    print('All tests passed')


if __name__ == "__main__":
    main()
