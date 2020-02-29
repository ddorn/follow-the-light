#version 330

in vec2 vert;
out vec2 f_pos;

void main() {
    f_pos = vert;
    gl_Position = vec4(vert, 0.0, 1.0);
}
