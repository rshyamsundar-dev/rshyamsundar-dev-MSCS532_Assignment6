"""Matrix implementation using nested lists."""


class Matrix:
    """Simple matrix implementation."""

    def __init__(self, rows: int, cols: int, default=0):
        """Create a rows × cols matrix."""
        self.rows = rows
        self.cols = cols
        self.data = [
            [default for _ in range(cols)]
            for _ in range(rows)
        ]

    def get(self, row: int, col: int):
        """Return the value at (row, col)."""
        self._validate_indices(row, col)
        return self.data[row][col]

    def set(self, row: int, col: int, value):
        """Update the value at (row, col)."""
        self._validate_indices(row, col)
        self.data[row][col] = value

    def insert_row(self, index: int, values=None):
        """Insert a new row."""
        if index < 0 or index > self.rows:
            raise IndexError("Row index out of range")

        if values is None:
            values = [0] * self.cols

        if len(values) != self.cols:
            raise ValueError("Incorrect number of columns")

        self.data.insert(index, values)
        self.rows += 1

    def delete_row(self, index: int):
        """Delete a row."""
        if index < 0 or index >= self.rows:
            raise IndexError("Row index out of range")

        self.data.pop(index)
        self.rows -= 1

    def display(self):
        """Print the matrix."""
        for row in self.data:
            print(row)

    def _validate_indices(self, row, col):
        """Validate row and column indices."""
        if not (0 <= row < self.rows):
            raise IndexError("Row index out of range")

        if not (0 <= col < self.cols):
            raise IndexError("Column index out of range")


if __name__ == "__main__":
    matrix = Matrix(3, 3)

    matrix.set(0, 0, 5)
    matrix.set(1, 1, 10)
    matrix.set(2, 2, 15)

    print("Original Matrix:")
    matrix.display()

    print("\nElement at (1,1):", matrix.get(1, 1))

    matrix.insert_row(1, [7, 7, 7])

    print("\nAfter inserting a row:")
    matrix.display()

    matrix.delete_row(2)

    print("\nAfter deleting row 2:")
    matrix.display()