# Find a sequence of transpositions of letters that transform
# the sequence MARINE (letters are numbered 0..5) to the sequence AIRMEN.
# Transpositions are represented by pairs of integers. For example, the pair (0,1) transforms MARINE to AMRINE.
# Transpositions are performed from left to right.
# You should define the sequence by writing something like
# this (the dots should be replaced by numbers, each pair in parentheses specifies one permutation,
# and these permutations are performed sequentially, from left to right):
# def sequence():
# return [(...,...),..., (...,...)]


def sequence(from_phrase='MARINE', to_phrase="AIRMEN"):
    to_phrase_dict = {x: i for i, x in enumerate(to_phrase)}
    seq = []
    from_phase_arr = list(from_phrase)
    pointer = 0
    while ''.join(from_phase_arr) != to_phrase:
        if pointer == len(from_phrase):
            pointer %= len(from_phrase)
        swap_with_index = to_phrase_dict[from_phase_arr[pointer]]
        if swap_with_index != pointer:
            from_phase_arr[swap_with_index], from_phase_arr[pointer] = from_phase_arr[pointer], from_phase_arr[
                swap_with_index]

            for i in range(pointer, swap_with_index):
                seq.append((i, i+1))
            for i in range(swap_with_index-1, pointer, -1):
                seq.append((i, i-1))
        pointer += 1

    return seq


print(sequence())
