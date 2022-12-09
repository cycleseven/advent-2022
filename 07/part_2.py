import sys

class Node():
    def __init__(self, type, name, parent, size=None):
        self.type = type
        self.name = name
        self.parent = parent
        self.children = {}

        if self.type == 'file':
            self.size = size
        else:
            self.size = 0

        if self.parent is None:
            self.absolute_path = self.name
        elif self.parent.parent is None:
            self.absolute_path = self.parent.absolute_path + self.name
        else:
            self.absolute_path = self.parent.absolute_path + "/" + self.name

    def add_child_directory(self, name):
        assert self.type == 'dir'
        child = Node('dir', name, self)

        if child.absolute_path in self.children:
            return self.children[child.absolute_path]

        self.children[child.absolute_path] = child

        return child

    def add_child_file(self, name, size):
        assert self.type == 'dir'
        child = Node('file', name, self, size)

        if child.absolute_path in self.children:
            return self.children[child.absolute_path]

        self.children[child.absolute_path] = child

        # Directory size == total size of all child files
        current_directory = self
        while current_directory is not None:
            assert current_directory.type == 'dir'
            current_directory.size += size
            current_directory = current_directory.parent

        return child

    def get_children(self):
        return self.children.values()

root = None
current_directory = None

# Build the filesystem tree as we discover files + directories via the terminal output.
# Track parent/child relationships and sizes as we go.
for line in sys.stdin:
    if line.startswith("$ "):
        prompt, command, *args = line.split()

        if command == 'cd':
            target_directory = args[0]

            if target_directory == '/':
                if root is None:
                    root = Node('dir', '/', None)
                current_directory = root
            elif target_directory == '..':
                current_directory = current_directory.parent
            else:
                # In practice it looks like directories are always printed via ls
                # before switching to them with cd. But just in case there's a blind
                # cd, we should record that directory too.
                child = current_directory.add_child_directory(target_directory)
                current_directory = child

        continue

    # Cheeky assumption: all non-command lines a line of output from ls.
    # This works as long as the only commands are cd and ls, and cd doesn't print any output.
    if line.startswith("dir "):
        _, dirname = line.split()
        child = current_directory.add_child_directory(dirname)
    else:
        size, filename = line.split()
        current_directory.add_child_file(filename, int(size))

# Traverse the tree to discover directories with size <= 100000
# Using breadth-first traversal to visit each node once.

disk_capacity = 70_000_000
required_disk_space_for_update = 30_000_000
free_disk_space = disk_capacity - root.size
size_of_directory_to_delete = root.size
next_nodes_to_traverse = [root]

while len(next_nodes_to_traverse) > 0:
    current_node = next_nodes_to_traverse.pop(0)

    if current_node.type != 'dir':
        continue

    free_disk_space_if_deleted = free_disk_space + current_node.size

    if (
        free_disk_space_if_deleted >= required_disk_space_for_update
        and current_node.size < size_of_directory_to_delete
    ):
        size_of_directory_to_delete = current_node.size

    next_nodes_to_traverse += current_node.get_children()

print(size_of_directory_to_delete)
