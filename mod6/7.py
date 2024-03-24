class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def restore_tree(log_file_path):
    # Словарь для хранения узлов дерева
    nodes = {}

    # Чтение файла логов
    with open(log_file_path, 'r') as file:
        for line in file:
            # Разбор строки лога
            node_val, left_val, right_val = map(int, line.split())

            # Получение или создание узла
            node = nodes.get(node_val, BinaryTreeNode(node_val))
            nodes[node_val] = node

            # Установка левого потомка
            if left_val != -1:
                left_node = nodes.get(left_val, BinaryTreeNode(left_val))
                nodes[left_val] = left_node
                node.left = left_node

            # Установка правого потомка
            if right_val != -1:
                right_node = nodes.get(right_val, BinaryTreeNode(right_val))
                nodes[right_val] = right_node
                node.right = right_node

    # Возвращаем корень дерева (первый узел в файле логов)
    return nodes[0]

log_file_path = f"" # Путь до файла с логами
restore_tree(log_file_path)