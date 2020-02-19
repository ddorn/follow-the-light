#version 330

in vec2 f_tex_coord;
uniform sampler2D tex;


void main() {
    gl_FragColor = texture(tex, f_tex_coord);
}