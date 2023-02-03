class Level:
      def __init__(self, matrix, pos):
            self.matrix = matrix
            self.rows = len(matrix)
            self.cols = len(matrix[0])
            self.playerY = pos[0]
            self.playerX = pos[1]
            self.timeLine = []