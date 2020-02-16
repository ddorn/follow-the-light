#version 330

in vec2 vert;
in vec3 v_color;
out vec3 f_color;
out vec2 bulb_pos;

void main() {
    bulb_pos = vec2(vert.x*1.5 - 0.5, vert.y * 1.5);
    gl_Position = vec4(vert, 0.0, 1.0);
    f_color = v_color;
}
