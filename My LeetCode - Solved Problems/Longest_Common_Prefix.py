#  Program created by Brayan Vera. Date 06/23/21

#  Program name: "Longest_Common_Prefix"
#  -This program returns the longest common prefix.
#  -This means that it returns the most common characters of all values entered.
#  -The program starts counting from the left to right.
#  Example:
#  ["hello","marshmallow"] = "" meaning nothing is similar.
#  ["hello","hellboy","helppp","heooo","httt"] = "h" is the only character among all strings.
#  ["1234","123go","123password"] = "123" is the common character among all strings.

def longest_common_prefix(strs):
    next_one = 1
    count_loop = 0
    counting = 0
    common_list = []
    end_list_val_counter = 0
    empty_string = ""
    if strs == ['']:
        return empty_string
    if len(strs) == 1:
        convert_to_str = strs[0]
        return convert_to_str
    if strs[counting] == '':
        return empty_string

    # For time efficiency, I have to determine the shortest length.
    store_first = strs[0]

    n = 1
    # To split all characters individually of a string entered.
    split_string1 = [store_first[index: index + n] for index in range(0, len(store_first), n)]
    len_first = len(split_string1)

    for grab2 in strs[next_one:]:
        next_one += 1
        end_list_val_counter += 1
        n = 1
        split_string2 = [grab2[index: index + n] for index in range(0, len(grab2), n)]
        len_next = len(split_string2)
        if len(split_string1) == 0 and len(split_string2) == 0:
            if len(strs) - 1 == end_list_val_counter:
                return empty_string
        if len(split_string2) == 0:
            return empty_string
        # This stores the shortest string length among all the strings entered.
        if len_first > len_next:
            len_first = len_next

    #print("The min len amon all the strings in the list is: {}".format(len_first))
    # To see which string is the shortest that stores the common values among all the strings.
    next_one = 1
    counting = 0
    while len_first != count_loop:
        end_list_val_counter = 0
        for grab_next in strs[next_one:]:
            end_list_val_counter += 1
            n = 1
            split_string3 = [grab_next[index: index + n] for index in range(0, len(grab_next), n)]
            #print("the next strings working", split_string3)
            if split_string1[counting] != split_string3[counting]:
                num_nocomma = ''.join(common_list)
                print("The common characters are: {}".format(num_nocomma))
                return num_nocomma
            if split_string1[counting] == split_string3[counting]:
                if len(strs) - 1 == end_list_val_counter:
                    #print("it got here")
                    common_list.append(split_string1[counting])
                    counting += 1
        count_loop += 1
    num_nocomma = ''.join(common_list)
    print("The common characters are: {}".format(num_nocomma))
    return num_nocomma

def main():
    strs = ["welcome","welldone","welldressed","wearefriends"]   # Enter desired strings in a list separated by a comma.
    longest_common_prefix(strs)

if __name__ == "__main__":
    main()