from typing import Dict

import pygame


class BaseInput:
    def update(self, event):
        raise NotImplemented

    @property
    def value(self):
        raise NotImplemented


class Button(BaseInput):
    def __init__(self, *controls):
        self.controls = controls
        self.pressed = False

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in self.controls:
                self.pressed = True
        elif event.type == pygame.KEYUP:
            if event.key in self.controls:
                self.pressed = False

    @property
    def value(self):
        return self.pressed * 1.0


class Axis(BaseInput):
    def __init__(self, left, right):
        if not isinstance(left, (list, tuple)):
            left = [left]
        if not isinstance(right, (list, tuple)):
            right = [right]

        self.left = left
        self.right = right

        self._left_pressed = 0
        self._right_pressed = 0

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in self.left:
                self._left_pressed = 1.0
            if event.key in self.right:
                self._right_pressed = 1.0
        elif event.type == pygame.KEYUP:
            if event.key in self.left:
                self._left_pressed = 0.0
            if event.key in self.right:
                self._right_pressed = 0.0

    @property
    def value(self):
        # One of them is zero
        if self._left_pressed * self._right_pressed == 0:
            return -self._left_pressed + self._right_pressed
        else:
            return 0.0


class Inputs:
    def __init__(self, **inputs):
        self.inputs: Dict[str, BaseInput] = inputs

    def update(self, event):
        for inp in self.inputs.values():
            inp.update(event)

    def __getitem__(self, item):
        try:
            return self.inputs[item]
        except KeyError:
            print("Trying to get input", item, "but available inputs are", *self.inputs)
            raise
