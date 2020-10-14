def make_move(self, map):

        if not self.life:
            return
        if len(self.movement_path) == 0:
            if self.plant:
                self.plant = False
                map[int(self.posX / 4)][int(self.posY / 4)] = 3

        else:
            self.direction = self.movement_path[0]
            self.move(map, bombs, explosions, enemy)
