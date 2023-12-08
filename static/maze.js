const Maze = {
  palette: ['#FFFFFF', '#000000', '#00ffff', '#ff00ff', '#AAAAAA'],
  drawMaze: (canvasId, labirin) => {
    const canvas = document.getElementById(canvasId);
    const ctx = canvas.getContext('2d');
    const boxSize = 23;

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    let x = 10,
      y = 10;

    for (let i = 0; i < labirin.length; i++) {
      for (let j = 0; j < labirin[i].length; j++) {
        ctx.fillStyle = Maze.palette[labirin[i][j]];
        ctx.fillRect(x, y, boxSize, boxSize);
        x += boxSize;
      }
      x = 10;
      y += boxSize;
    }
  },
  sleep: (ms) => {
    return new Promise((resolve) => setTimeout(resolve, ms));
  },
  exploreMaze: async (canvasId, labirin, row, col) => {
    const canvas = document.getElementById(canvasId);
    const ctx = canvas.getContext('2d');

    if (labirin[row][col] === 2) {
      return true;
    } else if (labirin[row][col] === 0) {
      labirin[row][col] = 3;
      Maze.drawMaze(canvasId, labirin);

      await Maze.sleep(250);

      if (
        row < labirin.length - 1 &&
        (await Maze.exploreMaze(canvasId, labirin, row + 1, col))
      ) {
        return true;
      }

      if (
        row > 0 &&
        (await Maze.exploreMaze(canvasId, labirin, row - 1, col))
      ) {
        return true;
      }

      if (
        col < labirin[row].length - 1 &&
        (await Maze.exploreMaze(canvasId, labirin, row, col + 1))
      ) {
        return true;
      }

      if (
        col > 0 &&
        (await Maze.exploreMaze(canvasId, labirin, row, col - 1))
      ) {
        return true;
      }

      labirin[row][col] = 4;
      Maze.drawMaze(canvasId, labirin);

      await Maze.sleep(250);
    }

    return false;
  },
};

export default Maze;
