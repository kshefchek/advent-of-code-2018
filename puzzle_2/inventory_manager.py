from typing import List, Tuple


def checksum_ids(id_list: List) -> int:
    """
    create a checksum by counting the number of IDs containing exactly two
    of any letter and then separately counting those with exactly three of
    any letter, and multiplying those two counts together
    :param id_list: List of ids
    :return: int - checksum
    """
    two_count = 0
    three_count = 0

    for box_id in id_list:
        has_two = False  # id contains exactly two of any letter
        has_three = False  # id contains exactly three of any letter

        for char in box_id:
            if has_two and has_three:
                break

            if not has_two and len(box_id) - len(box_id.replace(char, '')) == 2:
                two_count += 1
                has_two = True

            if not has_three and len(box_id) - len(box_id.replace(char, ''))  == 3:
                three_count += 1
                has_three = True
    return two_count * three_count


def pairwise_alignment(reference_id:str, query_id: str) -> Tuple[int, str]:
    """
    given two input strings, return their hamming distance and alignment
    with an asterix substituting any mismatches,
    fghij and fguij -> (1, fg*ij)
    """
    if len(reference_id) != len(query_id):
        raise ValueError("ids are not equal length")

    hamming_distance = 0
    alignment = ""
    for ref_el, query_el in zip(reference_id, query_id):
        if ref_el == query_el:
            alignment += ref_el
        else:
            hamming_distance += 1
            alignment += '*'

    return hamming_distance, alignment
