class SpotAnimation:
    def __init__(self):
        self._spot_center_x = 0.5
        self._spot_center_y = 0.5
        self._spot_radius = 0.05
        self._spot_delta_x = 0.007
        self._spot_delta_y = -0.004


    def spot_center(self):
        return self._spot_center_x, self._spot_center_y


    def spot_radius(self):
        return self._spot_radius


    def next_frame(self):
        self._spot_center_x += self._spot_delta_x
        self._spot_center_y += self._spot_delta_y

        self._spot_right_x = self._spot_center_x + self._spot_radius

        if self._spot_right_x >= 1.0:
            overshot_x = self._spot_right_x - 1.0
            self._spot_center_x -= overshot_x * 2
            self._spot_delta_x = -self._spot_delta_x

