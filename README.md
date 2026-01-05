# A* Pathfinding Visualizer (Pygame)

A simple interactive visualization of the **A\*** pathfinding algorithm built using **Python** and **Pygame**.  
This project allows users to place a start node, an end node, barriers, and visually see how A\* explores the grid to find the shortest path.

---

## Features

- Interactive grid-based environment
- Click to place:
  - **Start node**
  - **End node**
  - **Barriers (walls)**
- Real-time visualization of:
  - Open set
  - Closed set
  - Final shortest path
- Uses **Manhattan distance** as the heuristic
- No diagonal movement (4-directional grid)

---

## Controls

- **Left Mouse Button**
  - First click: place **start**
  - Second click: place **end**
  - Subsequent clicks: place **barriers**

- **Right Mouse Button**
  - Remove a node or barrier

- **SPACE**
  - Run the A* algorithm (start and end must be set)

- **C**
  - Clear the grid and reset everything

- **Close Window**
  - Exit the program

---

## Project Structure

