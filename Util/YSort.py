def partition(nodes: list, low: int, high: int):
    index = (low - 1)
    pivot = nodes[high]

    for j in range(low, high):
        if nodes[j].get_position().y <= pivot.get_position().y:
            index = index + 1
            nodes[index], nodes[j] = nodes[j], nodes[index]

    nodes[index + 1], nodes[high] = nodes[high], nodes[index + 1]
    return index + 1


def quickSort(nodes: list, low: int, high: int):
    if len(nodes) == 1:
        return nodes
    if low < high:
        pi = partition(nodes, low, high)
        quickSort(nodes, low, pi - 1)
        quickSort(nodes, pi + 1, high)


class YSort:

    def __init__(self, node_list):
        self.__node_list = node_list

    def get_ySort(self):
        quickSort(self.__node_list, 0, len(self.__node_list) - 1)
        return self.__node_list
