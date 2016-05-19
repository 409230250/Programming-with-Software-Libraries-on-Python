import animation_model
import tkinter


class SpotAnimationView:
    def __init__(self):
        self._animation = animation_model.SpotAnimation()

        self._root_window = tkinter.Tk()
        self._canvas = tkinter.Canvas(
            self._root_window, width = 500, height = 400,
            background = 'black')

        self._canvas.grid(
            row = 0, column = 0, padx = 5, pady = 5,
            sticky = tkinter.W + tkinter.E + tkinter.N + tkinter.S)

        self._canvas.bind('<Configure>', self._on_canvas_resize)
        self._canvas.bind('<Button-1>', self._on_canvas_click)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

        self._animation_running = False


    def start(self):
        self._root_window.mainloop()


    def _on_canvas_resize(self, event):
        self._redraw()


    def _on_canvas_click(self, event):
        if not self._animation_running:
            self._root_window.after(25, func=self._next_frame)

        self._animation_running = not self._animation_running


    def _next_frame(self):
        if self._animation_running:
            self._animation.next_frame()
            self._redraw()
            self._root_window.after(25, func=self._next_frame)


    def _redraw(self):
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        
        self._canvas.delete(tkinter.ALL)

        frac_centerx, frac_centery = self._animation.spot_center()
        frac_radius = self._animation.spot_radius()

        frac_topleftx = frac_centerx - frac_radius
        frac_toplefty = frac_centery - frac_radius
        frac_bottomrightx = frac_centerx + frac_radius
        frac_bottomrighty = frac_centery + frac_radius

        self._canvas.create_oval(
            frac_topleftx * width, frac_toplefty * height,
            frac_bottomrightx * width, frac_bottomrighty * height,
            fill = '#FF6600')



if __name__ == '__main__':
    SpotAnimationView().start()

