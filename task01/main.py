class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, "-->", end="")
            current = current.next
        print('None')

    def reverse(self):
        prev = None
        current = self.head
        while current:
            print(current.data, "-->", end="")
            next_node = current.next  # Зберігаємо наступний елемент
            current.next = prev  # Змінюємо напрямок поточного вузла
            prev = current  # Переміщуємо prev вперед
            current = next_node  # Переміщуємо current вперед
        self.head = prev  # Змінюємо голову на останній елемент
        print('None')

    def merge_sort(self, head):
        if not head or not head.next:
            return head

        middle = self.get_middle(head)
        next_to_middle = middle.next

        # Розділяємо список на дві половини
        middle.next = None

        # Рекурсивно сортуємо обидві половини
        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        # Об'єднуємо відсортовані половини
        sorted_list = self.merge_sorted_lists(left, right)

        return sorted_list

    def get_middle(self, head):
        if not head:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sorted_merge(self, a, b):
        result = None

        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)

        return result

    def merge_sorted_lists(self, list1, list2):
        # Базові випадки
        if not list1:
            return list2
        if not list2:
            return list1

        # Рекурсивно зливаємо списки
        if list1.data <= list2.data:
            result = list1
            result.next = self.merge_sorted_lists(list1.next, list2)
        else:
            result = list2
            result.next = self.merge_sorted_lists(list1, list2.next)

        return result


def main():
    first_list = LinkedList()

    first_list.insert_at_beginning(5)
    first_list.insert_at_beginning(10)
    first_list.insert_at_beginning(15)
    first_list.insert_at_end(20)
    first_list.insert_at_end(25)
    print("Зв'язний список:")
    first_list.print_list()

    first_list.reverse()
    print("Зв'язний список після реверсування :")
    first_list.print_list()

    first_list.head = first_list.merge_sort(first_list.head)
    print("Зв'язний список відсортовано:")
    first_list.print_list()

    second_list = LinkedList()
    second_list.insert_at_beginning(59)
    second_list.insert_at_beginning(20)
    second_list.insert_at_beginning(35)

    merged_head = first_list.merge_sorted_lists(first_list.head, second_list.head)
    merged_list = LinkedList()
    merged_list.head = merged_head
    print("Зв'язний список відсортовано та замерджено:")
    first_list.print_list()


if __name__ == "__main__":
    main()

