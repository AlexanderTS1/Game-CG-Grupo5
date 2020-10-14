def make_move(self, map, bombs, explosions, enemy):

        if not self.life:
            return
        if len(self.movement_path) == 0:
            if self.plant:
                bombs.append(self.plant_bomb(map))
                self.plant = False
                map[int(self.posX / 4)][int(self.posY / 4)] = 3
            if self.algorithm is Algorithm.DFS:
                self.dfs(self.create_grid(map, bombs, explosions, enemy))
            else:
                self.dijkstra(self.create_grid_dijkstra(map, bombs, explosions, enemy))

        else:
            self.direction = self.movement_path[0]
            self.move(map, bombs, explosions, enemy)