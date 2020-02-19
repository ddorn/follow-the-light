#version 330

in vec3 vert;
in vec2 tex_coord;

out vec2 f_tex_coord;

void main() {
    f_tex_coord = tex_coord;
    gl_Position = vec4(vert, 1.0);
}
